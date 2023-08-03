
# Common SavedModel APIs for Image Tasks

This page describes how [TF2 SavedModels](../tf2_saved_model.md) for
image-related tasks should implement the
[Reusable SavedModel API](../reusable_saved_models.md). (This replaces the
[Common Signatures for Images](../common_signatures/images.md) for the
now-deprecated [TF1 Hub format](../tf1_hub_module).)

<a name="feature-vector"></a>

## Image Feature Vector

### Usage summary

An **image feature vector** is a dense 1-D tensor that represents a whole image,
typically for use by a simple feed-forward classifier in the consumer model. (In
terms of classic CNNs, this is the bottleneck value after the spatial extent has
been pooled or flattened away, but before classification is done; for that, see
[image classification](#classification) below.)

A Reusable SavedModel for image feature extraction has a `__call__` method on
the root object that maps a batch of images to a batch of feature vectors. It
can be used like so:

```python
obj = hub.load("path/to/model")  # That's tf.saved_model.load() after download.
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = obj(images)   # A batch with shape [batch_size, num_features].
```

In Keras, the equivalent is

```python
features = hub.KerasLayer("path/to/model")(images)
```

The input follows the general convention for [input of images](#input). The
model documentation specifies the permissible range for `height` and `width` of
the input.

The output is a single tensor of dtype `float32` and shape `[batch_size,
num_features]`. The `batch_size` is the same as in the input. `num_features` is
a module-specific constant independent of input size.

### API details

The [Reusable SavedModel API](../reusable_saved_models.md) also provides a list
of `obj.variables` (e.g., for initialization when not loading eagerly).

A model that supports fine-tuning provides a list of `obj.trainable_variables`.
It may require you to pass `training=True` to execute in training mode (e.g.,
for dropout). Some models allow optional arguments to override hyperparameters
(e.g., dropout rate; to be described in model documentation). The model may also
provide a list of `obj.regularization_losses`. For details, see the
[Reusable SavedModel API](../reusable_saved_models.md).

In Keras, this is taken care of by `hub.KerasLayer`: initialize it with
`trainable=True` to enable fine-tuning, and (in the rare case that hparam
overrides apply) with `arguments=dict(some_hparam=some_value, ...))`.

### Notes

Applying dropout to the output features (or not) should be left to the model
consumer. The SavedModel itself should not perform dropout on the actual outputs
(even if it uses dropout internally in other places).

### Examples

Reusable SavedModels for image feature vectors are used in

*   the Colab tutorial
    [Retraining an Image Classifier](https://colab.research.google.com/github/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/tf2_image_retraining.ipynb),

<a name="classification"></a>

## Image Classification

### Usage summary

**Image classification** maps the pixels of an image to linear scores (logits)
for membership in the classes of a taxonomy _selected by the module publisher_.
This allows model consumers to to draw conclusions from the particular
classification learned by the publisher module. (For image classification with
a new set of classes, it is common to reuse an
[Image Feature Vector](#feature-vector) model with a new classifier instead.)

A Reusable SavedModel for image classification has a `__call__` method on the
root object that maps a batch of images to a batch of logits. It can be used
like so:

```python
obj = hub.load("path/to/model")  # That's tf.saved_model.load() after download.
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = obj(images)   # A batch with shape [batch_size, num_classes].
```

In Keras, the equivalent is

```python
logits = hub.KerasLayer("path/to/model")(images)
```

The input follows the general convention for [input of images](#input). The
model documentation specifies the permissible range for `height` and `width` of
the input.

The output `logits` is a single tensor of dtype `float32` and shape
`[batch_size, num_classes]`. The `batch_size` is the same as in the input.
`num_classes` is the number of classes in the classification, which is a
model-specific constant.

The value `logits[i, c]` is a score predicting the membership of example `i` in
the class with index `c`.

It depends on the underlying classification whether these scores are meant to be
used with softmax (for mutually exclusive classes), sigmoid (for orthogonal
classes), or something else. The module documentation should describe this, and
refer to a definition of the class indices.

### API details

The [Reusable SavedModel API](../reusable_saved_models.md) also provides a list
of `obj.variables` (e.g., for initialization when not loading eagerly).

A model that supports fine-tuning provides a list of `obj.trainable_variables`.
It may require you to pass `training=True` to execute in training mode (e.g.,
for dropout). Some models allow optional arguments to override hyperparameters
(e.g., dropout rate; to be described in model documentation). The model may also
provide a list of `obj.regularization_losses`. For details, see the
[Reusable SavedModel API](../reusable_saved_models.md).

In Keras, this is taken care of by `hub.KerasLayer`: initialize it with
`trainable=True` to enable fine-tuning, and (in the rare case that hparam
overrides apply) with `arguments=dict(some_hparam=some_value, ...))`.

<a name="input"></a>

## Image input

This is common to all types of image models.

A model that takes a batch of images as input accepts them as a dense 4-D tensor
of dtype `float32` and shape `[batch_size, height, width, 3]` whose elements are
RGB color values of pixels normalized to the range [0, 1]. This is what you get
from `tf.image.decode_*()` followed by `tf.image.convert_image_dtype(...,
tf.float32)`.

The model accepts any `batch_size`. The model documentation specifies the
permissible range for `height` and `width`. The last dimension is fixed to 3 RGB
channels.

It is recommended that models use the `channels_last` (or `NHWC`) layout of
Tensors throughout, and leave it to TensorFlow's graph optimizer to rewrite to
`channels_first` (or `NCHW`) if needed.
