description: Instantiates the EfficientNetB4 architecture.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.applications.EfficientNetB4" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.applications.EfficientNetB4

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/applications/efficientnet.py#L621-L644">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates the EfficientNetB4 architecture.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.applications.efficientnet.EfficientNetB4`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.applications.EfficientNetB4`, `tf.compat.v1.keras.applications.efficientnet.EfficientNetB4`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.applications.EfficientNetB4(
    include_top=(True), weights='imagenet', input_tensor=None, input_shape=None,
    pooling=None, classes=1000, classifier_activation='softmax', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Reference:


- [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](
    https://arxiv.org/abs/1905.11946) (ICML 2019)

Optionally loads weights pre-trained on ImageNet.
Note that the data format convention used by the model is
the one specified in your Keras config at `~/.keras/keras.json`.
If you have never configured it, it defaults to `"channels_last"`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`include_top`
</td>
<td>
Whether to include the fully-connected
layer at the top of the network. Defaults to True.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
One of `None` (random initialization),
'imagenet' (pre-training on ImageNet),
or the path to the weights file to be loaded. Defaults to 'imagenet'.
</td>
</tr><tr>
<td>
`input_tensor`
</td>
<td>
Optional Keras tensor
(i.e. output of <a href="../../../tf/keras/Input.md"><code>layers.Input()</code></a>)
to use as image input for the model.
</td>
</tr><tr>
<td>
`input_shape`
</td>
<td>
Optional shape tuple, only to be specified
if `include_top` is False.
It should have exactly 3 inputs channels.
</td>
</tr><tr>
<td>
`pooling`
</td>
<td>
Optional pooling mode for feature extraction
when `include_top` is `False`. Defaults to None.
- `None` means that the output of the model will be
the 4D tensor output of the
last convolutional layer.
- `avg` means that global average pooling
will be applied to the output of the
last convolutional layer, and thus
the output of the model will be a 2D tensor.
- `max` means that global max pooling will
be applied.
</td>
</tr><tr>
<td>
`classes`
</td>
<td>
Optional number of classes to classify images
into, only to be specified if `include_top` is True, and
if no `weights` argument is specified. Defaults to 1000 (number of
ImageNet classes).
</td>
</tr><tr>
<td>
`classifier_activation`
</td>
<td>
A `str` or callable. The activation function to use
on the "top" layer. Ignored unless `include_top=True`. Set
`classifier_activation=None` to return the logits of the "top" layer.
Defaults to 'softmax'.
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

