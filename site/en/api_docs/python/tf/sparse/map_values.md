description: Applies op to the .values tensor of one or more SparseTensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.map_values" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.map_values

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L2776-L2840">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies `op` to the `.values` tensor of one or more `SparseTensor`s.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.map_values(
    op, *args, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Replaces any `SparseTensor` in `args` or `kwargs` with its `values`
tensor (which contains the non-default values for the SparseTensor),
and then calls `op`.  Returns a `SparseTensor` that is constructed
from the input `SparseTensor`s' `indices`, `dense_shape`, and the
value returned by the `op`.

If the input arguments contain multiple `SparseTensor`s, then they must have
equal `indices` and dense shapes.

#### Examples:



```
>>> s = tf.sparse.from_dense([[1, 2, 0],
...                           [0, 4, 0],
...                           [1, 0, 0]])
>>> tf.sparse.to_dense(tf.sparse.map_values(tf.ones_like, s)).numpy()
array([[1, 1, 0],
       [0, 1, 0],
       [1, 0, 0]], dtype=int32)
```

```
>>> tf.sparse.to_dense(tf.sparse.map_values(tf.multiply, s, s)).numpy()
array([[ 1,  4,  0],
       [ 0, 16,  0],
       [ 1,  0,  0]], dtype=int32)
```

```
>>> tf.sparse.to_dense(tf.sparse.map_values(tf.add, s, 5)).numpy()
array([[6, 7, 0],
       [0, 9, 0],
       [6, 0, 0]], dtype=int32)
```

Note: even though `tf.add(0, 5) != 0`, implicit zeros
will remain unchanged. However, if the sparse tensor contains any explict
zeros, these will be affected by the mapping!

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`op`
</td>
<td>
The operation that should be applied to the SparseTensor `values`. `op`
is typically an element-wise operation (such as math_ops.add), but any
operation that preserves the shape can be used.
</td>
</tr><tr>
<td>
`*args`
</td>
<td>
Arguments for `op`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments for `op`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` whose `indices` and `dense_shape` matches the `indices`
and `dense_shape` of all input `SparseTensor`s.
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
If args contains no `SparseTensor`, or if the `indices`
or `dense_shape`s of the input `SparseTensor`s are not equal.
</td>
</tr>
</table>

