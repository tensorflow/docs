
# SavedModels from TF Hub in TensorFlow 2

The
[SavedModel format of TensorFlow 2](https://www.tensorflow.org/guide/saved_model)
is the recommended way to share pre-trained models and model pieces on
TensorFlow Hub. It replaces the older [TF1 Hub format](tf1_hub_module.md) and
comes with a new set of APIs.

This page explains how to reuse TF2 SavedModels in a TensorFlow 2 program with
the low-level `hub.load()` API and its `hub.KerasLayer` wrapper. (Typically,
`hub.KerasLayer` is combined with other `tf.keras.layers` to build a Keras model
or the `model_fn` of a TF2 Estimator.) These APIs can also load the legacy
models in TF1 Hub format, within limits, see the
[compatibility guide](model_compatibility.md).

Users of TensorFlow 1 can update to TF 1.15 and then use the same APIs.
Older versions of TF1 do not work.

## Using SavedModels from TF Hub

### Using a SavedModel in Keras

[Keras](https://www.tensorflow.org/guide/keras/) is TensorFlow's high-level API
for building deep learning models by composing Keras Layer objects.
The `tensorflow_hub` library provides the class `hub.KerasLayer` that gets
initialized with the URL (or filesystem path) of a SavedModel and then
provides the computation from the SavedModel, including its pre-trained
weights.

Here is an example of using a pre-trained text embedding:

```python
import tensorflow as tf
import tensorflow_hub as hub

hub_url = "https://tfhub.dev/google/nnlm-en-dim128/2"
embed = hub.KerasLayer(hub_url)
embeddings = embed(["A long sentence.", "single-word", "http://example.com"])
print(embeddings.shape, embeddings.dtype)
```

From this, a text classifier can be built in the usual Keras way:

```python
model = tf.keras.Sequential([
    embed,
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
```

The [Text classification
colab](https://colab.research.google.com/github/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/tf2_text_classification.ipynb)
is a complete example how to train and evaluate such a classifier.

The model weights in a `hub.KerasLayer` are set to non-trainable by default.
See the section on fine-tuning below for how to change that. Weights are
shared between all applications of the same layer object, as usual in Keras.


### Using a SavedModel in an Estimator

Users of TensorFlow's
[Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)
API for distributed training can use SavedModels from TF Hub by
writing their `model_fn` in terms of  `hub.KerasLayer` among other
`tf.keras.layers`.


### Behind the scenes: SavedModel downloading and caching

Using a SavedModel from TensorFlow Hub (or other HTTPS servers that implement
its [hosting](hosting.md) protocol) downloads and decompresses it to the local
filesystem if not already present. The environment variable `TFHUB_CACHE_DIR`
can be set to override the default temporary location for caching the downloaded
and uncompressed SavedModels. For details, see [Caching](caching.md).

### Using a SavedModel in low-level TensorFlow
#### Model Handles

SavedModels can be loaded from a specified `handle`, where the `handle` is a
filesystem path, valid TFhub.dev model URL (e.g. "https://tfhub.dev/...").
Kaggle Models URLs mirror TFhub.dev handles in accordance with our Terms and the
license associated with the model assets, e.g. "https://www.kaggle.com/...".
Handles from Kaggle Models are equivalent to their corresponding TFhub.dev
handle.

The function `hub.load(handle)` downloads and decompresses a SavedModel
(unless `handle` is already a filesystem path) and then returns the result
of loading it with TensorFlow's built-in function `tf.saved_model.load()`.
Therefore, `hub.load()` can handle any valid SavedModel (unlike its
predecessor `hub.Module` for TF1).

#### Advanced topic: what to expect from the SavedModel after loading

Depending on the contents of the SavedModel, the result of
`obj = hub.load(...)` can be invoked in various ways (as explained in
much greater detail in TensorFlow's [SavedModel
Guide](https://www.tensorflow.org/guide/saved_model):

  * The serving signatures of the SavedModel (if any) are represented as a
    dictionary of concrete functions and can be called like
    `tensors_out = obj.signatures["serving_default"](**tensors_in)`,
    with dictionaries of tensors keyed by the respective input and output
    names and subject to the signature's shape and dtype constraints.

  * The
    [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)-decorated
    methods of the saved object (if any) are restored as tf.function objects
    that can be called by all combinations of Tensor and non-Tensor arguments
    for which the tf.function had been
    [traced](https://www.tensorflow.org/tutorials/customization/performance#tracing)
    prior to saving. In particular, if there is an `obj.__call__` method
    with suitable traces, `obj` itself can be called like a Python function.
    A simple example could look like
    `output_tensor = obj(input_tensor, training=False)`.

This leaves enormous liberty in the interfaces that SavedModels can
implement. The [Reusable SavedModels interface](reusable_saved_models.md)
for `obj` establishes conventions such that client code, including adapters
like `hub.KerasLayer`, know how to use the SavedModel.

Some SavedModels may not follow that convention, especially whole models
not meant to be reused in larger models, and just provide serving signatures.

The trainable variables in a SavedModel are reloaded as trainable,
and `tf.GradientTape` will watch them by default. See the section on
fine-tuning below for some caveats, and consider avoiding this for starters.
Even if you want to fine-tune, you may want to see if `obj.trainable_variables`
advises to re-train only a subset of the originally trainable variables.


## Creating SavedModels for TF Hub

### Overview

SavedModel is TensorFlow's standard serialization format for trained models
or model pieces.
It stores the model's trained weights together with the exact TensorFlow
operations to perform its computation. It can be used independently from
the code that created it. In particular, it can be reused across different
high-level model-building APIs like Keras, because TensorFlow operations
are their common basic language.

### Saving from Keras

Starting with TensorFlow 2, `tf.keras.Model.save()` and
`tf.keras.models.save_model()` default to the SavedModel format (not HDF5).
The resulting SavedModels that can be used with `hub.load()`,
`hub.KerasLayer` and similar adapters for other high-level APIs
as they become available.

To share a complete Keras Model, just save it with `include_optimizer=False`.

To share a piece of a Keras Model, make the piece a Model in itself and then
save that. You can either lay out the code like that from the start....

```python
piece_to_share = tf.keras.Model(...)
full_model = tf.keras.Sequential([piece_to_share, ...])
full_model.fit(...)
piece_to_share.save(...)
```

...or cut out the piece to share after the fact (if it aligns with the
layering of your full model):

```python
full_model = tf.keras.Model(...)
sharing_input = full_model.get_layer(...).get_output_at(0)
sharing_output = full_model.get_layer(...).get_output_at(0)
piece_to_share = tf.keras.Model(sharing_input, sharing_output)
piece_to_share.save(..., include_optimizer=False)
```

[TensorFlow Models](https://github.com/tensorflow/models) on GitHub uses the
former approach for BERT (see
[nlp/tools/export_tfhub_lib.py](https://github.com/tensorflow/models/blob/master/official/nlp/tools/export_tfhub_lib.py),
note the split between `core_model` for export and the `pretrainer` for
restoring the checkpoint) and the latter approach for ResNet (see
[legacy/image_classification/tfhub_export.py](https://github.com/tensorflow/models/blob/master/official/legacy/image_classification/resnet/tfhub_export.py)).

### Saving from low-level TensorFlow

This requires good familiarity with TensorFlow's [SavedModel
Guide](https://www.tensorflow.org/guide/saved_model).

If you want to provide more than just a serving signature, you should
implement the [Reusable SavedModel interface](reusable_saved_models.md).
Conceptually, this looks like

```python
class MyMulModel(tf.train.Checkpoint):
  def __init__(self, v_init):
    super().__init__()
    self.v = tf.Variable(v_init)
    self.variables = [self.v]
    self.trainable_variables = [self.v]
    self.regularization_losses = [
        tf.function(input_signature=[])(lambda: 0.001 * self.v**2),
    ]

  @tf.function(input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
  def __call__(self, inputs):
    return tf.multiply(inputs, self.v)

tf.saved_model.save(MyMulModel(2.0), "/tmp/my_mul")

layer = hub.KerasLayer("/tmp/my_mul")
print(layer([10., 20.]))  # [20., 40.]
layer.trainable = True
print(layer.trainable_weights)  # [2.]
print(layer.losses)  # 0.004
```


## Fine-Tuning

Training the already-trained variables of an imported SavedModel together with
those of the model around it is called *fine-tuning* the SavedModel.
This can result in better quality, but often makes the training more
demanding (may take more time, depend more on the optimizer and its
hyperparameters, increase the risk of overfitting and require dataset
augmentation, esp. for CNNs). We advise SavedModel consumers to look into
fine-tuning only after having established a good training regime,
and only if the SavedModel publisher recommends it.

Fine-tuning changes the "continuous" model parameters that are trained.
It does not change hard-coded transformations, such as tokenizing text
input and mapping tokens to their corresponding entries in an embedding matrix.

### For SavedModel consumers

Creating a `hub.KerasLayer` like

```python
layer = hub.KerasLayer(..., trainable=True)
```

enables fine-tuning of the SavedModel loaded by the layer. It adds the
trainable weights and weight regularizers declared in the SavedModel
to the Keras model, and runs the SavedModel's computation in training
mode (think of dropout etc.).

The [image classification
colab](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/tf2_image_retraining.ipynb)
contains an end-to-end example with optional fine-tuning.

#### Re-exporting the fine-tuning result

Advanced users may want to save the results of fine-tuning back into
a SavedModel that can be used instead of the originally loaded one.
This can be done with code like

```python
loaded_obj = hub.load("https://tfhub.dev/...")
hub_layer = hub.KerasLayer(loaded_obj, trainable=True, ...)

model = keras.Sequential([..., hub_layer, ...])
model.compile(...)
model.fit(...)

export_module_dir = os.path.join(os.getcwd(), "finetuned_model_export")
tf.saved_model.save(loaded_obj, export_module_dir)
```

### For SavedModel creators

When creating a SavedModel for sharing on TensorFlow Hub,
think ahead if and how its consumers should fine-tune it,
and provide guidance in the documentation.

Saving from a Keras Model should make all the mechanics of fine-tuning work
(saving weight regularization losses, declaring trainable variables, tracing
`__call__` for both `training=True` and `training=False`, etc.)

Choose a model interface that plays well with gradient flow,
e.g., output logits instead of softmax probabilities or top-k predictions.

If the model use dropout, batch normalization, or similar training techniques
that involve hyperparameters, set them to values that make sense across many
expected target problems and batch sizes. (As of this writing, saving from
Keras does not make it easy to let consumers adjust them.)

Weight regularizers on individual layers are saved (with their regularization
strength coefficients), but weight regularization from within the optimizer
(like `tf.keras.optimizers.Ftrl.l1_regularization_strength=...)`)
is lost. Advise consumers of your SavedModel accordingly.
