description: Instantiates a Mobile NASNet model in ImageNet mode.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.applications.NASNetMobile" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.applications.NASNetMobile

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/applications/nasnet.py#L322-L396">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates a Mobile NASNet model in ImageNet mode.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.applications.nasnet.NASNetMobile`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.applications.NASNetMobile`, `tf.compat.v1.keras.applications.nasnet.NASNetMobile`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.applications.NASNetMobile(
    input_shape=None, include_top=(True), weights='imagenet', input_tensor=None,
    pooling=None, classes=1000
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Reference:


- [Learning Transferable Architectures for Scalable Image Recognition](
    https://arxiv.org/abs/1707.07012) (CVPR 2018)

Optionally loads weights pre-trained on ImageNet.
Note that the data format convention used by the model is
the one specified in your Keras config at `~/.keras/keras.json`.

Note: each Keras Application expects a specific kind of input preprocessing.
For NASNet, call <a href="../../../tf/keras/applications/nasnet/preprocess_input.md"><code>tf.keras.applications.nasnet.preprocess_input</code></a> on your
inputs before passing them to the model.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`input_shape`
</td>
<td>
Optional shape tuple, only to be specified
if `include_top` is False (otherwise the input shape
has to be `(224, 224, 3)` for NASNetMobile
It should have exactly 3 inputs channels,
and width and height should be no smaller than 32.
E.g. `(224, 224, 3)` would be one valid value.
</td>
</tr><tr>
<td>
`include_top`
</td>
<td>
Whether to include the fully-connected
layer at the top of the network.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
`None` (random initialization) or
`imagenet` (ImageNet weights)
For loading `imagenet` weights, `input_shape` should be (224, 224, 3)
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
Optional pooling mode for feature extraction
when `include_top` is `False`.
- `None` means that the output of the model
will be the 4D tensor output of the
last convolutional layer.
- `avg` means that global average pooling
will be applied to the output of the
last convolutional layer, and thus
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
Optional number of classes to classify images
into, only to be specified if `include_top` is True, and
if no `weights` argument is specified.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras model instance.
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
In case of invalid argument for `weights`,
or invalid input shape.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If attempting to run this model with a
backend that does not support separable convolutions.
</td>
</tr>
</table>

