description: Image resizing layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.Resizing" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.experimental.preprocessing.Resizing

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/image_preprocessing.py#L57-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Image resizing layer.

Inherits From: [`Layer`](../../../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.Resizing`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.Resizing(
    height, width, interpolation='bilinear', name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Resize the batched image input to target height and width. The input should
be a 4-D tensor in the format of NHWC.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`height`
</td>
<td>
Integer, the height of the output shape.
</td>
</tr><tr>
<td>
`width`
</td>
<td>
Integer, the width of the output shape.
</td>
</tr><tr>
<td>
`interpolation`
</td>
<td>
String, the interpolation method. Defaults to `bilinear`.
Supports `bilinear`, `nearest`, `bicubic`, `area`, `lanczos3`, `lanczos5`,
`gaussian`, `mitchellcubic`
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string, the name of the layer.
</td>
</tr>
</table>



