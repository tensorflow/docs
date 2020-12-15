description: Instantiates the Inception-ResNet v2 architecture.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.applications.InceptionResNetV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.applications.InceptionResNetV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/applications/inception_resnet_v2.py#L43-L248">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates the Inception-ResNet v2 architecture.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.applications.inception_resnet_v2.InceptionResNetV2`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.applications.InceptionResNetV2`, `tf.compat.v1.keras.applications.inception_resnet_v2.InceptionResNetV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.applications.InceptionResNetV2(
    include_top=(True), weights='imagenet', input_tensor=None, input_shape=None,
    pooling=None, classes=1000, classifier_activation='softmax', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Reference:


- [Inception-v4, Inception-ResNet and the Impact of
   Residual Connections on Learning](https://arxiv.org/abs/1602.07261)
  (AAAI 2017)

Optionally loads weights pre-trained on ImageNet.
Note that the data format convention used by the model is
the one specified in your Keras config at `~/.keras/keras.json`.

Caution: Be sure to properly pre-process your inputs to the application.
Please see <a href="../../../tf/keras/applications/inception_resnet_v2/preprocess_input.md"><code>applications.inception_resnet_v2.preprocess_input</code></a> for an example.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`include_top`
</td>
<td>
whether to include the fully-connected
layer at the top of the network.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
one of `None` (random initialization),
'imagenet' (pre-training on ImageNet),
or the path to the weights file to be loaded.
</td>
</tr><tr>
<td>
`input_tensor`
</td>
<td>
optional Keras tensor (i.e. output of <a href="../../../tf/keras/Input.md"><code>layers.Input()</code></a>)
to use as image input for the model.
</td>
</tr><tr>
<td>
`input_shape`
</td>
<td>
optional shape tuple, only to be specified
if `include_top` is `False` (otherwise the input shape
has to be `(299, 299, 3)` (with `'channels_last'` data format)
or `(3, 299, 299)` (with `'channels_first'` data format).
It should have exactly 3 inputs channels,
and width and height should be no smaller than 75.
E.g. `(150, 150, 3)` would be one valid value.
</td>
</tr><tr>
<td>
`pooling`
</td>
<td>
Optional pooling mode for feature extraction
when `include_top` is `False`.
- `None` means that the output of the model will be
the 4D tensor output of the last convolutional block.
- `'avg'` means that global average pooling
will be applied to the output of the
last convolutional block, and thus
the output of the model will be a 2D tensor.
- `'max'` means that global max pooling will be applied.
</td>
</tr><tr>
<td>
`classes`
</td>
<td>
optional number of classes to classify images
into, only to be specified if `include_top` is `True`, and
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
or invalid input shape.
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

