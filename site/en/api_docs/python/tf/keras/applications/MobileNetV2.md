description: Instantiates the MobileNetV2 architecture.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.applications.MobileNetV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.applications.MobileNetV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/applications/mobilenet_v2.py#L95-L414">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates the MobileNetV2 architecture.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.applications.mobilenet_v2.MobileNetV2`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.applications.MobileNetV2`, `tf.compat.v1.keras.applications.mobilenet_v2.MobileNetV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.applications.MobileNetV2(
    input_shape=None, alpha=1.0, include_top=(True), weights='imagenet',
    input_tensor=None, pooling=None, classes=1000, classifier_activation='softmax',
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Reference:


- [MobileNetV2: Inverted Residuals and Linear Bottlenecks](
    https://arxiv.org/abs/1801.04381) (CVPR 2018)

Optionally loads weights pre-trained on ImageNet.

Caution: Be sure to properly pre-process your inputs to the application.
Please see <a href="../../../tf/keras/applications/mobilenet_v2/preprocess_input.md"><code>applications.mobilenet_v2.preprocess_input</code></a> for an example.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`input_shape`
</td>
<td>
Optional shape tuple, to be specified if you would
like to use a model with an input image resolution that is not
(224, 224, 3).
It should have exactly 3 inputs channels (224, 224, 3).
You can also omit this option if you would like
to infer input_shape from an input_tensor.
If you choose to include both input_tensor and input_shape then
input_shape will be used if they match, if the shapes
do not match then we will throw an error.
E.g. `(160, 160, 3)` would be one valid value.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
Float between 0 and 1. controls the width of the network.
This is known as the width multiplier in the MobileNetV2 paper,
but the name is kept for consistency with `applications.MobileNetV1`
model in Keras.
- If `alpha` < 1.0, proportionally decreases the number
of filters in each layer.
- If `alpha` > 1.0, proportionally increases the number
of filters in each layer.
- If `alpha` = 1, default number of filters from the paper
are used at each layer.
</td>
</tr><tr>
<td>
`include_top`
</td>
<td>
Boolean, whether to include the fully-connected
layer at the top of the network. Defaults to `True`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
String, one of `None` (random initialization),
'imagenet' (pre-training on ImageNet),
or the path to the weights file to be loaded.
</td>
</tr><tr>
<td>
`input_tensor`
</td>
<td>
Optional Keras tensor (i.e. output of
<a href="../../../tf/keras/Input.md"><code>layers.Input()</code></a>)
to use as image input for the model.
</td>
</tr><tr>
<td>
`pooling`
</td>
<td>
String, optional pooling mode for feature extraction
when `include_top` is `False`.
- `None` means that the output of the model
will be the 4D tensor output of the
last convolutional block.
- `avg` means that global average pooling
will be applied to the output of the
last convolutional block, and thus
the output of the model will be a
2D tensor.
- `max` means that global max pooling will
be applied.
</td>
</tr><tr>
<td>
`classes`
</td>
<td>
Integer, optional number of classes to classify images
into, only to be specified if `include_top` is True, and
if no `weights` argument is specified.
</td>
</tr><tr>
<td>
`classifier_activation`
</td>
<td>
A `str` or callable. The activation function to use
on the "top" layer. Ignored unless `include_top=True`. Set
`classifier_activation=None` to return the logits of the "top" layer.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
For backwards compatibility only.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/keras/Model.md"><code>keras.Model</code></a> instance.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
in case of invalid argument for `weights`,
or invalid input shape or invalid alpha, rows when
weights='imagenet'
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `classifier_activation` is not `softmax` or `None` when
using a pretrained top layer.
</td>
</tr>
</table>

