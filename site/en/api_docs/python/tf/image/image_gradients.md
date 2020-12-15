description: Returns image gradients (dy, dx) for each color channel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.image_gradients" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.image_gradients

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L4308-L4379">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns image gradients (dy, dx) for each color channel.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.image_gradients`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.image_gradients(
    image
)
</code></pre>



<!-- Placeholder for "Used in" -->

Both output tensors have the same shape as the input: [batch_size, h, w,
d]. The gradient values are organized so that [I(x+1, y) - I(x, y)] is in
location (x, y). That means that dy will always have zeros in the last row,
and dx will always have zeros in the last column.

#### Usage Example:

```python
BATCH_SIZE = 1
IMAGE_HEIGHT = 5
IMAGE_WIDTH = 5
CHANNELS = 1
image = tf.reshape(tf.range(IMAGE_HEIGHT * IMAGE_WIDTH * CHANNELS,
  delta=1, dtype=tf.float32),
  shape=(BATCH_SIZE, IMAGE_HEIGHT, IMAGE_WIDTH, CHANNELS))
dx, dy = tf.image.image_gradients(image)
print(image[0, :,:,0])
tf.Tensor(
  [[ 0.  1.  2.  3.  4.]
  [ 5.  6.  7.  8.  9.]
  [10. 11. 12. 13. 14.]
  [15. 16. 17. 18. 19.]
  [20. 21. 22. 23. 24.]], shape=(5, 5), dtype=float32)
print(dx[0, :,:,0])
tf.Tensor(
  [[5. 5. 5. 5. 5.]
  [5. 5. 5. 5. 5.]
  [5. 5. 5. 5. 5.]
  [5. 5. 5. 5. 5.]
  [0. 0. 0. 0. 0.]], shape=(5, 5), dtype=float32)
print(dy[0, :,:,0])
tf.Tensor(
  [[1. 1. 1. 1. 0.]
  [1. 1. 1. 1. 0.]
  [1. 1. 1. 1. 0.]
  [1. 1. 1. 1. 0.]
  [1. 1. 1. 1. 0.]], shape=(5, 5), dtype=float32)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
Tensor with shape [batch_size, h, w, d].
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Pair of tensors (dy, dx) holding the vertical and horizontal image
gradients (1-step finite difference).
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
If `image` is not a 4D tensor.
</td>
</tr>
</table>

