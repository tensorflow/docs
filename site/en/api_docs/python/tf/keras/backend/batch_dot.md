description: Batchwise dot product.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.batch_dot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.batch_dot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L1835-L2021">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batchwise dot product.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.batch_dot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.batch_dot(
    x, y, axes=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`batch_dot` is used to compute dot product of `x` and `y` when
`x` and `y` are data in batch, i.e. in a shape of
`(batch_size, :)`.
`batch_dot` results in a tensor or variable with less dimensions
than the input. If the number of dimensions is reduced to 1,
we use `expand_dims` to make sure that ndim is at least 2.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Keras tensor or variable with `ndim >= 2`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Keras tensor or variable with `ndim >= 2`.
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
Tuple or list of integers with target dimensions, or single integer.
The sizes of `x.shape[axes[0]]` and `y.shape[axes[1]]` should be equal.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor with shape equal to the concatenation of `x`'s shape
(less the dimension that was summed over) and `y`'s shape
(less the batch dimension and the dimension that was summed over).
If the final rank is 1, we reshape it to `(batch_size, 1)`.
</td>
</tr>

</table>



#### Examples:



```
>>> x_batch = tf.keras.backend.ones(shape=(32, 20, 1))
>>> y_batch = tf.keras.backend.ones(shape=(32, 30, 20))
>>> xy_batch_dot = tf.keras.backend.batch_dot(x_batch, y_batch, axes=(1, 2))
>>> tf.keras.backend.int_shape(xy_batch_dot)
(32, 1, 30)
```

#### Shape inference:

Let `x`'s shape be `(100, 20)` and `y`'s shape be `(100, 30, 20)`.
If `axes` is (1, 2), to find the output shape of resultant tensor,
    loop through each dimension in `x`'s shape and `y`'s shape:
* `x.shape[0]` : 100 : append to output shape
* `x.shape[1]` : 20 : do not append to output shape,
    dimension 1 of `x` has been summed over. (`dot_axes[0]` = 1)
* `y.shape[0]` : 100 : do not append to output shape,
    always ignore first dimension of `y`
* `y.shape[1]` : 30 : append to output shape
* `y.shape[2]` : 20 : do not append to output shape,
    dimension 2 of `y` has been summed over. (`dot_axes[1]` = 2)
`output_shape` = `(100, 30)`
