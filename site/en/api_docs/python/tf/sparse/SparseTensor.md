description: Represents a sparse tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.SparseTensor" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__div__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__mul__"/>
<meta itemprop="property" content="__truediv__"/>
<meta itemprop="property" content="consumers"/>
<meta itemprop="property" content="eval"/>
<meta itemprop="property" content="from_value"/>
<meta itemprop="property" content="get_shape"/>
</div>

# tf.sparse.SparseTensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/sparse_tensor.py#L47-L260">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a sparse tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.SparseTensor`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.SparseTensor`, `tf.compat.v1.sparse.SparseTensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.SparseTensor(
    indices, values, dense_shape
)
</code></pre>



<!-- Placeholder for "Used in" -->

TensorFlow represents a sparse tensor as three separate dense tensors:
`indices`, `values`, and `dense_shape`.  In Python, the three tensors are
collected into a `SparseTensor` class for ease of use.  If you have separate
`indices`, `values`, and `dense_shape` tensors, wrap them in a `SparseTensor`
object before passing to the ops below.

Concretely, the sparse tensor `SparseTensor(indices, values, dense_shape)`
comprises the following components, where `N` and `ndims` are the number
of values and number of dimensions in the `SparseTensor`, respectively:

* `indices`: A 2-D int64 tensor of shape `[N, ndims]`, which specifies the
  indices of the elements in the sparse tensor that contain nonzero values
  (elements are zero-indexed). For example, `indices=[[1,3], [2,4]]` specifies
  that the elements with indexes of [1,3] and [2,4] have nonzero values.

* `values`: A 1-D tensor of any type and shape `[N]`, which supplies the
  values for each element in `indices`. For example, given `indices=[[1,3],
  [2,4]]`, the parameter `values=[18, 3.6]` specifies that element [1,3] of
  the sparse tensor has a value of 18, and element [2,4] of the tensor has a
  value of 3.6.

* `dense_shape`: A 1-D int64 tensor of shape `[ndims]`, which specifies the
  dense_shape of the sparse tensor. Takes a list indicating the number of
  elements in each dimension. For example, `dense_shape=[3,6]` specifies a
  two-dimensional 3x6 tensor, `dense_shape=[2,3,4]` specifies a
  three-dimensional 2x3x4 tensor, and `dense_shape=[9]` specifies a
  one-dimensional tensor with 9 elements.

The corresponding dense tensor satisfies:

```python
dense.shape = dense_shape
dense[tuple(indices[i])] = values[i]
```

By convention, `indices` should be sorted in row-major order (or equivalently
lexicographic order on the tuples `indices[i]`). This is not enforced when
`SparseTensor` objects are constructed, but most ops assume correct ordering.
If the ordering of sparse tensor `st` is wrong, a fixed version can be
obtained by calling <a href="../../tf/sparse/reorder.md"><code>tf.sparse.reorder(st)</code></a>.

Example: The sparse tensor

```python
SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
```

represents the dense tensor

```python
[[1, 0, 0, 0]
 [0, 0, 2, 0]
 [0, 0, 0, 0]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`
</td>
<td>
A 2-D int64 tensor of shape `[N, ndims]`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A 1-D tensor of any type and shape `[N]`.
</td>
</tr><tr>
<td>
`dense_shape`
</td>
<td>
A 1-D int64 tensor of shape `[ndims]`.
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
When building an eager SparseTensor if `dense_shape` is
unknown or contains unknown elements (None or -1).
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dense_shape`
</td>
<td>
A 1-D Tensor of int64 representing the shape of the dense tensor.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The `DType` of elements in this tensor.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
The `Graph` that contains the index, value, and dense_shape tensors.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
The indices of non-zero values in the represented dense tensor.
</td>
</tr><tr>
<td>
`op`
</td>
<td>
The `Operation` that produces `values` as an output.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Get the `TensorShape` representing the shape of the dense tensor.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
The non-zero values in the represented dense tensor.
</td>
</tr>
</table>



## Methods

<h3 id="consumers"><code>consumers</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/sparse_tensor.py#L259-L260">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>consumers()
</code></pre>




<h3 id="eval"><code>eval</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/sparse_tensor.py#L214-L237">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>eval(
    feed_dict=None, session=None
)
</code></pre>

Evaluates this sparse tensor in a `Session`.

Calling this method will execute all preceding operations that
produce the inputs needed for the operation that produces this
tensor.

*N.B.* Before invoking <a href="../../tf/sparse/SparseTensor.md#eval"><code>SparseTensor.eval()</code></a>, its graph must have been
launched in a session, and either a default session must be
available, or `session` must be specified explicitly.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`feed_dict`
</td>
<td>
A dictionary that maps `Tensor` objects to feed values. See
`tf.Session.run` for a description of the valid feed values.
</td>
</tr><tr>
<td>
`session`
</td>
<td>
(Optional.) The `Session` to be used to evaluate this sparse
tensor. If none, the default session will be used.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensorValue` object.
</td>
</tr>

</table>



<h3 id="from_value"><code>from_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/sparse_tensor.py#L106-L114">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_value(
    sparse_tensor_value
)
</code></pre>




<h3 id="get_shape"><code>get_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/sparse_tensor.py#L154-L160">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_shape()
</code></pre>

Get the `TensorShape` representing the shape of the dense tensor.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `TensorShape` object.
</td>
</tr>

</table>



<h3 id="__div__"><code>__div__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L1145-L1151">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__div__(
    sp_x, y
)
</code></pre>

Component-wise divides a SparseTensor by a dense Tensor.

*Limitation*: this Op only broadcasts the dense side to the sparse side, but not
the other direction.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sp_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  `N x R` matrix with the indices of non-empty values in a
SparseTensor, possibly not in canonical ordering.
</td>
</tr><tr>
<td>
`sp_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
1-D.  `N` non-empty values corresponding to `sp_indices`.
</td>
</tr><tr>
<td>
`sp_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  Shape of the input SparseTensor.
</td>
</tr><tr>
<td>
`dense`
</td>
<td>
A `Tensor`. Must have the same type as `sp_values`.
`R`-D.  The dense Tensor operand.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `sp_values`.
</td>
</tr>

</table>



<h3 id="__mul__"><code>__mul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L1145-L1151">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mul__(
    sp_x, y
)
</code></pre>

Component-wise multiplies a SparseTensor by a dense Tensor.

The output locations corresponding to the implicitly zero elements in the sparse
tensor will be zero (i.e., will not take up storage space), regardless of the
contents of the dense tensor (even if it's +/-INF and that INF*0 == NaN).

*Limitation*: this Op only broadcasts the dense side to the sparse side, but not
the other direction.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sp_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  `N x R` matrix with the indices of non-empty values in a
SparseTensor, possibly not in canonical ordering.
</td>
</tr><tr>
<td>
`sp_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
1-D.  `N` non-empty values corresponding to `sp_indices`.
</td>
</tr><tr>
<td>
`sp_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  Shape of the input SparseTensor.
</td>
</tr><tr>
<td>
`dense`
</td>
<td>
A `Tensor`. Must have the same type as `sp_values`.
`R`-D.  The dense Tensor operand.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `sp_values`.
</td>
</tr>

</table>



<h3 id="__truediv__"><code>__truediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L1145-L1151">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__truediv__(
    sp_x, y
)
</code></pre>

Internal helper function for 'sp_t / dense_t'.




