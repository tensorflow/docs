description: Return the elements where condition is True (multiplexing x and y).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.where" />
<meta itemprop="path" content="Stable" />
</div>

# tf.where

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L4488-L4600">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return the elements where `condition` is `True` (multiplexing `x` and `y`).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.where_v2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.where(
    condition, x=None, y=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operator has two modes: in one mode both `x` and `y` are provided, in
another mode neither are provided. `condition` is always expected to be a
<a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool`.

#### Retrieving indices of `True` elements

If `x` and `y` are not provided (both are None):

<a href="../tf/where.md"><code>tf.where</code></a> will return the indices of `condition` that are `True`, in
the form of a 2-D tensor with shape (n, d).
(Where n is the number of matching indices in `condition`,
and d is the number of dimensions in `condition`).

Indices are output in row-major order.

```
>>> tf.where([True, False, False, True])
<tf.Tensor: shape=(2, 1), dtype=int64, numpy=
array([[0],
       [3]])>
```

```
>>> tf.where([[True, False], [False, True]])
<tf.Tensor: shape=(2, 2), dtype=int64, numpy=
array([[0, 0],
       [1, 1]])>
```

```
>>> tf.where([[[True, False], [False, True], [True, True]]])
<tf.Tensor: shape=(4, 3), dtype=int64, numpy=
array([[0, 0, 0],
       [0, 1, 1],
       [0, 2, 0],
       [0, 2, 1]])>
```

#### Multiplexing between `x` and `y`

If `x` and `y` are provided (both have non-None values):

<a href="../tf/where.md"><code>tf.where</code></a> will choose an output shape from the shapes of `condition`, `x`,
and `y` that all three shapes are
[broadcastable](https://docs.scipy.org/doc/numpy/reference/ufuncs.html) to.

The `condition` tensor acts as a mask that chooses whether the corresponding
element / row in the output should be taken from `x`
(if the element in `condition` is True) or `y` (if it is false).

```
>>> tf.where([True, False, False, True], [1,2,3,4], [100,200,300,400])
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([  1, 200, 300,   4],
dtype=int32)>
>>> tf.where([True, False, False, True], [1,2,3,4], [100])
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([  1, 100, 100,   4],
dtype=int32)>
>>> tf.where([True, False, False, True], [1,2,3,4], 100)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([  1, 100, 100,   4],
dtype=int32)>
>>> tf.where([True, False, False, True], 1, 100)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([  1, 100, 100,   1],
dtype=int32)>
```

```
>>> tf.where(True, [1,2,3,4], 100)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([1, 2, 3, 4],
dtype=int32)>
>>> tf.where(False, [1,2,3,4], 100)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([100, 100, 100, 100],
dtype=int32)>
```

Note that if the gradient of either branch of the tf.where generates
a NaN, then the gradient of the entire tf.where will be NaN.
A workaround is to use an inner tf.where to ensure the function has
no asymptote, and to avoid computing a value whose gradient is NaN by
replacing dangerous inputs with safe inputs.

Instead of this,

```
>>> y = tf.constant(-1, dtype=tf.float32)
>>> tf.where(y > 0, tf.sqrt(y), y)
<tf.Tensor: shape=(), dtype=float32, numpy=-1.0>
```

Use this

```
>>> tf.where(y > 0, tf.sqrt(tf.where(y > 0, y, 1)), y)
<tf.Tensor: shape=(), dtype=float32, numpy=-1.0>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`condition`
</td>
<td>
A <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool`
</td>
</tr><tr>
<td>
`x`
</td>
<td>
If provided, a Tensor which is of the same type as `y`, and has a shape
broadcastable with `condition` and `y`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
If provided, a Tensor which is of the same type as `x`, and has a shape
broadcastable with `condition` and `x`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name of the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
If `x` and `y` are provided:
A `Tensor` with the same type as `x` and `y`, and shape that
is broadcast from `condition`, `x`, and `y`.
Otherwise, a `Tensor` with shape `(num_true, dim_size(condition))`.
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
When exactly one of `x` or `y` is non-None, or the shapes
are not all broadcastable.
</td>
</tr>
</table>

