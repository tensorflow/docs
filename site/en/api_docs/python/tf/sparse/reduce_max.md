description: Computes the max of elements across dimensions of a SparseTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.reduce_max" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.reduce_max

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sparse_ops.py#L1071-L1147">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the max of elements across dimensions of a SparseTensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.reduce_max(
    sp_input, axis=None, keepdims=None, output_is_sparse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This Op takes a SparseTensor and is the sparse counterpart to
<a href="../../tf/math/reduce_max.md"><code>tf.reduce_max()</code></a>.  In particular, this Op also returns a dense `Tensor`
if `output_is_sparse` is `False`, or a `SparseTensor` if `output_is_sparse`
is `True`.

Note: A gradient is not defined for this function, so it can't be used
in training models that need gradient descent.

Reduces `sp_input` along the dimensions given in `axis`.  Unless
`keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
`axis`. If `keepdims` is true, the reduced dimensions are retained
with length 1.

If `axis` has no entries, all dimensions are reduced, and a tensor
with a single element is returned.  Additionally, the axes can be negative,
similar to the indexing rules in Python.

The values not defined in `sp_input` don't participate in the reduce max,
as opposed to be implicitly assumed 0 -- hence it can return negative values
for sparse `axis`. But, in case there are no values in
`axis`, it will reduce to 0. See second example below.

#### For example:



```python
# 'x' represents [[1, ?, 2]
#                 [?, 3, ?]]
# where ? is implicitly-zero.
tf.sparse.reduce_max(x) ==> 3
tf.sparse.reduce_max(x, 0) ==> [1, 3, 2]
tf.sparse.reduce_max(x, 1) ==> [2, 3]  # Can also use -1 as the axis.
tf.sparse.reduce_max(x, 1, keepdims=True) ==> [[2], [3]]
tf.sparse.reduce_max(x, [0, 1]) ==> 3

# 'y' represents [[-7, ?]
#                 [ 4, 3]
#                 [ ?, ?]
tf.sparse.reduce_max(x, 1) ==> [-7, 4, 0]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
The SparseTensor to reduce. Should have numeric type.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The dimensions to reduce; list or scalar. If `None` (the
default), reduces all dimensions.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
If true, retain reduced dimensions with length 1.
</td>
</tr><tr>
<td>
`output_is_sparse`
</td>
<td>
If true, returns a `SparseTensor` instead of a dense
`Tensor` (the default).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The reduced Tensor or the reduced SparseTensor if `output_is_sparse` is
True.
</td>
</tr>

</table>

