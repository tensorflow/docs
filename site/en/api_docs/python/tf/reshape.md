description: Reshapes a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.reshape" />
<meta itemprop="path" content="Stable" />
</div>

# tf.reshape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L59-L197">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reshapes a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.manip.reshape`, `tf.compat.v1.reshape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.reshape(
    tensor, shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given `tensor`, this operation returns a new <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> that has the same
values as `tensor` in the same order, except with a new shape given by
`shape`.

```
>>> t1 = [[1, 2, 3],
...       [4, 5, 6]]
>>> print(tf.shape(t1).numpy())
[2 3]
>>> t2 = tf.reshape(t1, [6])
>>> t2
<tf.Tensor: shape=(6,), dtype=int32,
  numpy=array([1, 2, 3, 4, 5, 6], dtype=int32)>
>>> tf.reshape(t2, [3, 2])
<tf.Tensor: shape=(3, 2), dtype=int32, numpy=
  array([[1, 2],
         [3, 4],
         [5, 6]], dtype=int32)>
```

The <a href="../tf/reshape.md"><code>tf.reshape</code></a> does not change the order of or the total number of elements
in the tensor, and so it can reuse the underlying data buffer. This makes it
a fast operation independent of how big of a tensor it is operating on.

```
>>> tf.reshape([1, 2, 3], [2, 2])
Traceback (most recent call last):
...
InvalidArgumentError: Input to reshape is a tensor with 3 values, but the
requested shape has 4
```

To instead reorder the data to rearrange the dimensions of a tensor, see
<a href="../tf/transpose.md"><code>tf.transpose</code></a>.

```
>>> t = [[1, 2, 3],
...      [4, 5, 6]]
>>> tf.reshape(t, [3, 2]).numpy()
array([[1, 2],
       [3, 4],
       [5, 6]], dtype=int32)
>>> tf.transpose(t, perm=[1, 0]).numpy()
array([[1, 4],
       [2, 5],
       [3, 6]], dtype=int32)
```

If one component of `shape` is the special value -1, the size of that
dimension is computed so that the total size remains constant.  In particular,
a `shape` of `[-1]` flattens into 1-D.  At most one component of `shape` can
be -1.

```
>>> t = [[1, 2, 3],
...      [4, 5, 6]]
>>> tf.reshape(t, [-1])
<tf.Tensor: shape=(6,), dtype=int32,
  numpy=array([1, 2, 3, 4, 5, 6], dtype=int32)>
>>> tf.reshape(t, [3, -1])
<tf.Tensor: shape=(3, 2), dtype=int32, numpy=
  array([[1, 2],
         [3, 4],
         [5, 6]], dtype=int32)>
>>> tf.reshape(t, [-1, 2])
<tf.Tensor: shape=(3, 2), dtype=int32, numpy=
  array([[1, 2],
         [3, 4],
         [5, 6]], dtype=int32)>
```

`tf.reshape(t, [])` reshapes a tensor `t` with one element to a scalar.

```
>>> tf.reshape([7], []).numpy()
7
```

#### More examples:



```
>>> t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(tf.shape(t).numpy())
[9]
>>> tf.reshape(t, [3, 3])
<tf.Tensor: shape=(3, 3), dtype=int32, numpy=
  array([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]], dtype=int32)>
```

```
>>> t = [[[1, 1], [2, 2]],
...      [[3, 3], [4, 4]]]
>>> print(tf.shape(t).numpy())
[2 2 2]
>>> tf.reshape(t, [2, 4])
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
  array([[1, 1, 2, 2],
         [3, 3, 4, 4]], dtype=int32)>
```

```
>>> t = [[[1, 1, 1],
...       [2, 2, 2]],
...      [[3, 3, 3],
...       [4, 4, 4]],
...      [[5, 5, 5],
...       [6, 6, 6]]]
>>> print(tf.shape(t).numpy())
[3 2 3]
>>> # Pass '[-1]' to flatten 't'.
>>> tf.reshape(t, [-1])
<tf.Tensor: shape=(18,), dtype=int32,
  numpy=array([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
  dtype=int32)>
>>> # -- Using -1 to infer the shape --
>>> # Here -1 is inferred to be 9:
>>> tf.reshape(t, [2, -1])
<tf.Tensor: shape=(2, 9), dtype=int32, numpy=
  array([[1, 1, 1, 2, 2, 2, 3, 3, 3],
         [4, 4, 4, 5, 5, 5, 6, 6, 6]], dtype=int32)>
>>> # -1 is inferred to be 2:
>>> tf.reshape(t, [-1, 9])
<tf.Tensor: shape=(2, 9), dtype=int32, numpy=
  array([[1, 1, 1, 2, 2, 2, 3, 3, 3],
         [4, 4, 4, 5, 5, 5, 6, 6, 6]], dtype=int32)>
>>> # -1 is inferred to be 3:
>>> tf.reshape(t, [ 2, -1, 3])
<tf.Tensor: shape=(2, 3, 3), dtype=int32, numpy=
  array([[[1, 1, 1],
          [2, 2, 2],
          [3, 3, 3]],
         [[4, 4, 4],
          [5, 5, 5],
          [6, 6, 6]]], dtype=int32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Defines the shape of the output tensor.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional string. A name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `tensor`.
</td>
</tr>

</table>

