
# TF1 Hub format

At its launch in 2018, TensorFlow Hub offered a single type of asset: TF1 Hub
format for import into TensorFlow 1 programs.

This page explains how to use TF1 Hub format in TF1 (or the TF1 compatibility
mode of TF2) with the `hub.Module` class and associated APIs. (The typical use
is to build a `tf.Graph`, possibly inside a TF1 `Estimator`, by combining one or
more models in TF1 Hub format with `tf.compat.layers` or `tf.layers`).

Users of TensorFlow 2 (outside TF1 compatibility mode) must use
[the new API with `hub.load()` or `hub.KerasLayer`](tf2_saved_model.md). The new
API loads the new TF2 SavedModel asset type, but also has limited
[support for loading TF1 Hub format into TF2](migration_tf2.md).

## Using a model in TF1 Hub format

### Instantiating a model in TF1 Hub format

A model in TF1 Hub format is imported into a TensorFlow program by creating a
`hub.Module` object from a string with its URL or filesystem path, such as:

```python
m = hub.Module("path/to/a/module_dir")
```
**Note:** See more information regarding other valid handle types [here](tf2_saved_model.md#model_handles).

This adds the module's variables to the current TensorFlow graph.
Running their initializers will read their pre-trained values from disk.
Likewise, tables and other state is added to the graph.

### Caching Modules

When creating a module from a URL, the module content is downloaded and cached
in the local system temporary directory. The location where modules are cached
can be overridden using `TFHUB_CACHE_DIR` environment variable. For details, see
[Caching](caching.md).

### Applying a Module

Once instantiated, a module `m` can be called zero or more times like a Python
function from tensor inputs to tensor outputs:

```python
y = m(x)
```

Each such call adds operations to the current TensorFlow graph to compute
`y` from `x`. If this involves variables with trained weights, these are
shared between all applications.

Modules can define multiple named *signatures* in order to allow being applied
in more than one way (similar to how Python objects have *methods*).
A module's documentation should describe the available
signatures. The call above applies the signature named `"default"`. Any
signature can be selected by passing its name to the optional `signature=`
argument.

If a signature has multiple inputs, they must be passed as a dict, with the keys
defined by the signature. Likewise, if a signature has multiple outputs, these
can be retrieved as a dict by passing `as_dict=True`, under the keys defined by
the signature (the key `"default"` is for the single output returned if
`as_dict=False`). So the most general form of applying a Module looks like:

```python
outputs = m(dict(apples=x1, oranges=x2), signature="fruit_to_pet", as_dict=True)
y1 = outputs["cats"]
y2 = outputs["dogs"]
```

A caller must supply all inputs defined by a signature, but there is no
requirement to use all of a module's outputs.
TensorFlow will run only those parts of the module that end up
as dependencies of a target in `tf.Session.run()`. Indeed, module publishers may
choose to provide various outputs for advanced uses (like activations of
intermediate layers) along with the main outputs. Module consumers should
handle additional outputs gracefully.

### Trying out alternative modules

Whenever there are multiple modules for the same task, TensorFlow Hub
encourages to equip them with compatible signatures (interfaces)
such that trying different ones is as easy as varying the module handle
as a string-valued hyperparameter.

To this end, we maintain a collection of recommended
[Common Signatures](common_signatures/index.md) for popular tasks.


## Creating a New Module

### Compatibility note

The TF1 Hub format is geared towards TensorFlow 1. It is only partially
supported by TF Hub in TensorFlow 2. Please do consider publishing in the new
[TF2 SavedModel](tf2_saved_model.md) format instead.

The TF1 Hub format is similar to the SavedModel format of TensorFlow 1 on a
syntactic level (same file names and protocol messages) but semantically
different to allow for module reuse, composition and re-training (e.g.,
different storage of resource initializers, different tagging conventions for
metagraphs). The easiest way to tell them apart on disk is the presence or
absence of the `tfhub_module.pb` file.

### General approach

To define a new module, a publisher calls `hub.create_module_spec()` with a
function `module_fn`. This function constructs a graph representing the module's
internal structure, using `tf.placeholder()` for inputs to be supplied by
the caller. Then it defines signatures by calling
`hub.add_signature(name, inputs, outputs)` one or more times.

For example:

```python
def module_fn():
  inputs = tf.placeholder(dtype=tf.float32, shape=[None, 50])
  layer1 = tf.layers.dense(inputs, 200)
  layer2 = tf.layers.dense(layer1, 100)
  outputs = dict(default=layer2, hidden_activations=layer1)
  # Add default signature.
  hub.add_signature(inputs=inputs, outputs=outputs)

...
spec = hub.create_module_spec(module_fn)
```

The result of `hub.create_module_spec()` can be used, instead of a path,
to instantiate a module object within a particular TensorFlow graph. In
such case, there is no checkpoint, and the module instance will use the
variable initializers instead.

Any module instance can be serialized to disk via its `export(path, session)`
method. Exporting a module serializes its definition together with the current
state of its variables in `session` into the passed path. This can be used
when exporting a module for the first time, as well as when exporting a fine
tuned module.

For compatibility with TensorFlow Estimators, `hub.LatestModuleExporter` exports
modules from the latest checkpoint, just like `tf.estimator.LatestExporter`
exports the entire model from the latest checkpoint.

Module publishers should implement a [common
signature](common_signatures/index.md) when possible, so that consumers can
easily exchange modules and find the best one for their problem.

### Real example

Take a look at our [text embedding module exporter](https://github.com/tensorflow/hub/blob/master/examples/text_embeddings/export.py)
for a real-world example of how to create a module from a common text embedding
format.


## Fine-Tuning

Training the variables of an imported module together with those of the model
around it is called *fine-tuning*. Fine-tuning can result in better quality, but
adds new complications. We advise consumers to look into fine-tuning only after
exploring simpler quality tweaks, and only if the module publisher recommends
it.

### For Consumers

To enable fine-tuning, instantiate the module with
`hub.Module(..., trainable=True)` to make its variables trainable and
import TensorFlow's `REGULARIZATION_LOSSES`. If the module has multiple
graph variants, make sure to pick the one appropriate for training.
Usually, that's the one with tags `{"train"}`.

Choose a training regime that does not ruin the pre-trained weights,
for example, a lower learning rate than for training from scratch.

### For Publishers

To make fine-tuning easier for consumers, please be mindful of the following:

*   Fine-tuning needs regularization. Your module is exported with the
    `REGULARIZATION_LOSSES` collection, which is what puts your choice of
    `tf.layers.dense(..., kernel_regularizer=...)` etc. into what the consumer
    gets from `tf.losses.get_regularization_losses()`. Prefer this way of
    defining L1/L2 regularization losses.

*   In the publisher model, avoid defining L1/L2 regularization via the `l1_`
    and `l2_regularization_strength` parameters of `tf.train.FtrlOptimizer`,
    `tf.train.ProximalGradientDescentOptimizer`, and other proximal optimizers.
    These are not exported alongside the module, and setting regularization
    strengths globally may not be appropriate for the consumer. Except for L1
    regularization in wide (i.e. sparse linear) or wide & deep models, it should
    be possible to use individual regularization losses instead.

*   If you use dropout, batch normalization, or similar training techniques, set
    their hyperparameters to values that make sense across many expected uses.
    The dropout rate may have to be adjusted to the target problem's propensity
    to overfitting. In batch normalization, the momentum (a.k.a. decay
    coefficient) should be small enough to enable fine-tuning with small
    datasets and/or large batches. For advanced consumers, consider adding a
    signature that exposes control over critical hyperparameters.
