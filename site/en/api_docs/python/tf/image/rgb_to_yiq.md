description: Converts one or more images from RGB to YIQ.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.rgb_to_yiq" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.rgb_to_yiq

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L3189-L3215">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts one or more images from RGB to YIQ.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.rgb_to_yiq`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.rgb_to_yiq(
    images
)
</code></pre>



<!-- Placeholder for "Used in" -->

Outputs a tensor of the same shape as the `images` tensor, containing the YIQ
value of the pixels.
The output is only well defined if the value in images are in [0,1].

#### Usage Example:



```
>>> x = tf.constant([[[1.0, 2.0, 3.0]]])
>>> tf.image.rgb_to_yiq(x)
<tf.Tensor: shape=(1, 1, 3), dtype=float32,
numpy=array([[[ 1.815     , -0.91724455,  0.09962624]]], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
2-D or higher rank. Image data to convert. Last dimension must be
size 3.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
tensor with the same shape as `images`.
</td>
</tr>
</table>

