
# Export a SavedModel

This page describes the details of exporting (saving) a model from a TensorFlow
program to the
[SavedModel format of TensorFlow 2](https://www.tensorflow.org/guide/saved_model).
This format is the recommended way to share pre-trained models and model pieces
on TensorFlow Hub. It replaces the older [TF1 Hub format](tf1_hub_module.md) and
comes with a new set of APIs. You can find more information on exporting the TF1
Hub format models in [TF1 Hub format export](exporting_hub_format.md). You can
find details on how to compress the SavedModel for sharing it on TensorFlow Hub
[here](writing_documentation.md#model-specific_asset_content).

Some model-building toolkits already provide tools to do this (e.g., see below
for [TensorFlow Model Garden](#tensorflow-model-garden)).

## Overview

SavedModel is TensorFlow's standard serialization format for trained models or
model pieces. It stores the model's trained weights together with the exact
TensorFlow operations to perform its computation. It can be used independently
from the code that created it. In particular, it can be reused across different
high-level model-building APIs like Keras, because TensorFlow operations are
their common basic language.

## Saving from Keras

Starting with TensorFlow 2, `tf.keras.Model.save()` and
`tf.keras.models.save_model()` default to the SavedModel format (not HDF5). The
resulting SavedModels that can be used with `hub.load()`, `hub.KerasLayer` and
similar adapters for other high-level APIs as they become available.

To share a complete Keras Model, just save it with `include_optimizer=False`.

To share a piece of a Keras Model, make the piece a Model in itself and then
save that. You can either lay out the code like that from the start....

```python
piece_to_share = tf.keras.Model(...)
full_model = tf.keras.Sequential([piece_to_share, ...])
full_model.fit(...)
piece_to_share.save(...)
```

...or cut out the piece to share after the fact (if it aligns with the layering
of your full model):

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
restoring the checkpoint) and the the latter approach for ResNet (see
[legacy/image_classification/tfhub_export.py](https://github.com/tensorflow/models/blob/master/official/legacy/image_classification/resnet/tfhub_export.py)).

## Saving from low-level TensorFlow

This requires good familiarity with TensorFlow's
[SavedModel Guide](https://www.tensorflow.org/guide/saved_model).

If you want to provide more than just a serving signature, you should implement
the [Reusable SavedModel interface](reusable_saved_models.md). Conceptually,
this looks like

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

## Advice for SavedModel creators

When creating a SavedModel for sharing on TensorFlow Hub, think ahead if and how
its consumers should fine-tune it, and provide guidance in the documentation.

Saving from a Keras Model should make all the mechanics of fine-tuning work
(saving weight regularization losses, declaring trainable variables, tracing
`__call__` for both `training=True` and `training=False`, etc.)

Choose a model interface that plays well with gradient flow, e.g., output logits
instead of softmax probabilities or top-k predictions.

If the model use dropout, batch normalization, or similar training techniques
that involve hyperparameters, set them to values that make sense across many
expected target problems and batch sizes. (As of this writing, saving from Keras
does not make it easy to let consumers adjust them.)

Weight regularizers on individual layers are saved (with their regularization
strength coefficients), but weight regularization from within the optimizer
(like `tf.keras.optimizers.Ftrl.l1_regularization_strength=...)`) is lost.
Advise consumers of your SavedModel accordingly.

<a name="tensorflow-model-garden"></a>

## TensorFlow Model Garden

The
[TensorFlow Model Garden](https://github.com/tensorflow/models/tree/master/research/official)
repo contains a lot of examples of creating reusable TF2 Saved Models to be
uploaded on [tfhub.dev](https://tfhub.dev/).

## Community Requests

The TensorFlow Hub team generates only a small fraction of the assets that are
available on tfhub.dev. We rely primarily on researchers at Google and DeepMind,
corporate and academic research institutions, and ML enthusiasts to produce
models. As a result, we can't guarantee that we can fulfill community requests
for specific assets, and we can't provide time estimates for new asset
availability.

The
[Community Model Requests milestone](https://github.com/tensorflow/hub/milestone/1)
below contains requests from the community for specific assets -- if you or
someone you know is interested in producing the asset and sharing it on
tfhub.dev, we welcome the submission!
