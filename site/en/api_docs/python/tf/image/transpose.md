description: Transpose image(s) by swapping the height and width dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L660-L715">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Transpose image(s) by swapping the height and width dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.transpose`, `tf.compat.v1.image.transpose_image`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.transpose(
    image, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.transpose(x)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 1.,  2.,  3.],
        [ 7.,  8.,  9.]],
       [[ 4.,  5.,  6.],
        [10., 11., 12.]]], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
of shape `[height, width, channels]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
If `image` was 4-D, a 4-D float Tensor of shape
`[batch, width, height, channels]`
If `image` was 3-D, a 3-D float Tensor of shape
`[width, height, channels]`
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
if the shape of `image` not supported.
</td>
</tr>
</table>



#### Usage Example:



```
>>> image = [[[1, 2], [3, 4]],
...         [[5, 6], [7, 8]],
...         [[9, 10], [11, 12]]]
>>> image = tf.constant(image)
>>> tf.image.transpose(image)
<tf.Tensor: shape=(2, 3, 2), dtype=int32, numpy=
array([[[ 1,  2],
       [ 5,  6],
       [ 9, 10]],
      [[ 3,  4],
       [ 7,  8],
       [11, 12]]], dtype=int32)>
```