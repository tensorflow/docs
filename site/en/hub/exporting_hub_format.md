
# Exporting models in the TF1 Hub format

You can read more about this format in [TF1 Hub format](tf1_hub_module.md)

## Compatibility note

The TF1 Hub format is geared towards TensorFlow 1. It is only partially
supported by TF Hub in TensorFlow 2. Please do consider publishing in the new
[TF2 SavedModel](tf2_saved_model.md) format instead by following the
[Exporting a model](exporting_tf2_saved_model) guide.

The TF1 Hub format is similar to the SavedModel format of TensorFlow 1 on a
syntactic level (same file names and protocol messages) but semantically
different to allow for module reuse, composition and re-training (e.g.,
different storage of resource initializers, different tagging conventions for
metagraphs). The easiest way to tell them apart on disk is the presence or
absence of the `tfhub_module.pb` file.

## General approach

To define a new module, a publisher calls `hub.create_module_spec()` with a
function `module_fn`. This function constructs a graph representing the module's
internal structure, using `tf.placeholder()` for inputs to be supplied by the
caller. Then it defines signatures by calling `hub.add_signature(name, inputs,
outputs)` one or more times.

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

The result of `hub.create_module_spec()` can be used, instead of a path, to
instantiate a module object within a particular TensorFlow graph. In such case,
there is no checkpoint, and the module instance will use the variable
initializers instead.

Any module instance can be serialized to disk via its `export(path, session)`
method. Exporting a module serializes its definition together with the current
state of its variables in `session` into the passed path. This can be used when
exporting a module for the first time, as well as when exporting a fine tuned
module.

For compatibility with TensorFlow Estimators, `hub.LatestModuleExporter` exports
modules from the latest checkpoint, just like `tf.estimator.LatestExporter`
exports the entire model from the latest checkpoint.

Module publishers should implement a
[common signature](common_signatures/index.md) when possible, so that consumers
can easily exchange modules and find the best one for their problem.

## Real example

Take a look at our
[text embedding module exporter](https://github.com/tensorflow/hub/blob/master/examples/text_embeddings/export.py)
for a real-world example of how to create a module from a common text embedding
format.

## Advice for Publishers

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
