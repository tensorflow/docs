
# Common Signatures for Images

This page describes common signatures that should be implemented by modules in
the [TF1 Hub format](../tf1_hub_module.md) for image-related tasks. (For the
[TF2 SavedModel format](../tf2_saved_model.md), see the analogous
[SavedModel API](../common_saved_model_apis/images.md).)

Some modules can be used for more than one task (e.g., image classification
modules tend to do some feature extraction on the way). Therefore, each module
provides (1) named signatures for all the tasks anticipated by the publisher,
and (2) a default signature `output = m(images)` for its designated primary
task.

<a name="feature-vector"></a>
## Image Feature Vector

### Usage summary

An **image feature vector** is a dense 1-D tensor that represents a whole image,
typically for classification by the consumer model. (Unlike the intermediate
activations of CNNs, it does not offer a spatial breakdown. Unlike [image
classification](#classification), it discards the classification learned
by the publisher model.)

A module for image feature extraction has a default signature that maps a batch
of images to a batch of feature vectors. It can be used like so:

```python
  module_spec = hub.load_module_spec("path/to/module")
  height, width = hub.get_expected_image_size(module_spec)
  images = ...  # A batch of images with shape [batch_size, height, width, 3].
  module = hub.Module(module_spec)
  features = module(images)   # A batch with shape [batch_size, num_features].
```

It also defines the corresponding named signature.

### Signature specification

The named signature for extracting image feature vectors is invoked as

```python
  outputs = module(dict(images=images), signature="image_feature_vector",
                   as_dict=True)
  features = outputs["default"]
```

The input follows the general convention for
[input of images](#input).

The outputs dictionary contains a `"default"` output of dtype `float32` and
shape `[batch_size, num_features]`. The `batch_size` is the same as in the
input, but not known at graph construction time. `num_features` is a known,
module-specific constant independent of input size.

These feature vectors are meant to be usable for classification with a simple
feed-forward classifier (like the pooled features from the topmost convolutional
layer in a typical CNN for image classification).

Applying dropout to the output features (or not) should be left to the module
consumer. The module itself should not perform dropout on the actual outputs
(even if it uses dropout internally in other places).

The outputs dictionary may provide further outputs, for example, the activations
of hidden layers inside the module. Their keys and values are module-dependent.
It is recommended to prefix architecture-dependent keys with an architecture
name (e.g., to avoid confusing the intermediate layer `"InceptionV3/Mixed_5c"`
with the topmost convolutional layer `"InceptionV2/Mixed_5c"`).

<a name="classification"></a>
## Image Classification

### Usage summary

**Image classification** maps the pixels of an image to linear scores (logits)
for membership in the classes of a taxonomy _selected by the module publisher_.
This allows consumers to draw conclusions from the particular classification
learned by the publisher module, and not just its underlying features (cf.
[Image Feature Vector](#feature-vector)).

A module for image feature extraction has a default signature that maps a batch
of images to a batch of logits. It can be used like so:

```python
  module_spec = hub.load_module_spec("path/to/module")
  height, width = hub.get_expected_image_size(module_spec)
  images = ...  # A batch of images with shape [batch_size, height, width, 3].
  module = hub.Module(module_spec)
  logits = module(images)   # A batch with shape [batch_size, num_classes].
```

It also defines the corresponding named signature.

### Signature specification

The named signature for extracting image feature vectors is invoked as

```python
  outputs = module(dict(images=images), signature="image_classification",
                   as_dict=True)
  logits = outputs["default"]
```

The input follows the general convention for
[input of images](#input).

The outputs dictionary contains a `"default"` output of dtype `float32` and
shape `[batch_size, num_classes]`. The `batch_size` is the same as in the input,
but not known at graph construction time. `num_classes` is the number of classes
in the classification, which is a known constant independent of input size.

Evaluating `outputs["default"][i, c]` yields a score predicting the membership
of example `i` in the class with index `c`.

It depends on the underlying classification whether these scores are meant to be
used with softmax (for mutually exclusive classes), sigmoid (for orthogonal
classes), or something else. The module documentation should describe this,
and refer to a definition of the class indices.

The outputs dictionary may provide further outputs, for example, the activations
of hidden layers inside the module. Their keys and values are module-dependent.
It is recommended to prefix architecture-dependent keys with an architecture
name (e.g., to avoid confusing the intermediate layer `"InceptionV3/Mixed_5c"`
with the topmost convolutional layer `"InceptionV2/Mixed_5c"`).

<a name="input"></a>
## Image input

This is common to all types of image modules and image signatures.

A signature that takes a batch of images as input accepts them as a dense 4-D
tensor of dtype `float32` and shape `[batch_size, height, width, 3]` whose
elements are RGB color values of pixels normalized to the range [0, 1]. This is
what you get from `tf.image.decode_*()` followed by
`tf.image.convert_image_dtype(..., tf.float32)`.

A module with exactly one (or one principal) input of images uses the name
`"images"` for this input.

The module accepts any `batch_size`, and correspondingly sets the first
dimension of TensorInfo.tensor_shape to "unknown". The last dimension is fixed
to the number `3` of RGB channels. The `height` and `width` dimensions are
fixed to the expected size of input images. (Future work may remove that
restriction for fully convolutional modules.)

Consumers of the module should not inspect the shape directly, but obtain
the size information by calling hub.get_expected_image_size()
on the module or module spec, and are expected to resize input images
accordingly (typically before/during batching).

For simplicity, TF-Hub modules use the `channels_last`
(or `NHWC`) layout of Tensors, and leave it to TensorFlow's graph optimizer
to rewrite to `channels_first` (or `NCHW`) if needed. It has been doing that
by default since TensorFlow version 1.7.
