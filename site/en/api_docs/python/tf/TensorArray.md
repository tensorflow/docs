description: Class wrapping dynamic-sized, per-time-step, write-once Tensor arrays.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.TensorArray" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="concat"/>
<meta itemprop="property" content="gather"/>
<meta itemprop="property" content="grad"/>
<meta itemprop="property" content="identity"/>
<meta itemprop="property" content="read"/>
<meta itemprop="property" content="scatter"/>
<meta itemprop="property" content="size"/>
<meta itemprop="property" content="split"/>
<meta itemprop="property" content="stack"/>
<meta itemprop="property" content="unstack"/>
<meta itemprop="property" content="write"/>
</div>

# tf.TensorArray

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L947-L1271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Class wrapping dynamic-sized, per-time-step, write-once Tensor arrays.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.TensorArray`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.TensorArray(
    dtype, size=None, dynamic_size=None, clear_after_read=None,
    tensor_array_name=None, handle=None, flow=None, infer_shape=(True),
    element_shape=None, colocate_with_first_write_call=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class is meant to be used with dynamic iteration primitives such as
`while_loop` and `map_fn`.  It supports gradient back-propagation via special
"flow" control flow dependencies.

Example 1: Plain reading and writing.

```
>>> ta = tf.TensorArray(tf.float32, size=0, dynamic_size=True, clear_after_read=False)
>>> ta = ta.write(0, 10)
>>> ta = ta.write(1, 20)
>>> ta = ta.write(2, 30)
>>>
>>> ta.read(0)
<tf.Tensor: shape=(), dtype=float32, numpy=10.0>
>>> ta.read(1)
<tf.Tensor: shape=(), dtype=float32, numpy=20.0>
>>> ta.read(2)
<tf.Tensor: shape=(), dtype=float32, numpy=30.0>
>>> ta.stack()
<tf.Tensor: shape=(3,), dtype=float32, numpy=array([10., 20., 30.],
dtype=float32)>
```

Example 2: Fibonacci sequence algorithm that writes in a loop then returns.

```
>>> @tf.function
... def fibonacci(n):
...   ta = tf.TensorArray(tf.float32, size=0, dynamic_size=True)
...   ta = ta.unstack([0., 1.])
...
...   for i in range(2, n):
...     ta = ta.write(i, ta.read(i - 1) + ta.read(i - 2))
...
...   return ta.stack()
>>>
>>> fibonacci(7)
<tf.Tensor: shape=(7,), dtype=float32,
numpy=array([0., 1., 1., 2., 3., 5., 8.], dtype=float32)>
```

Example 3: A simple loop interacting with a <a href="../tf/Variable.md"><code>tf.Variable</code></a>.


```
v = tf.Variable(1)
@tf.function
def f(x):
  ta = tf.TensorArray(tf.int32, size=0, dynamic_size=True)
  for i in tf.range(x):
    v.assign_add(i)
    ta = ta.write(i, v)
  return ta.stack()
f(5)
<tf.Tensor: shape=(5,), dtype=int32, numpy=array([ 1,  2,  4,  7, 11],
dtype=int32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
(required) data type of the TensorArray.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
(optional) int32 scalar `Tensor`: the size of the TensorArray.
Required if handle is not provided.
</td>
</tr><tr>
<td>
`dynamic_size`
</td>
<td>
(optional) Python bool: If true, writes to the TensorArray
can grow the TensorArray past its initial size.  Default: False.
</td>
</tr><tr>
<td>
`clear_after_read`
</td>
<td>
Boolean (optional, default: True).  If True, clear
TensorArray values after reading them.  This disables read-many
semantics, but allows early release of memory.
</td>
</tr><tr>
<td>
`tensor_array_name`
</td>
<td>
(optional) Python string: the name of the TensorArray.
This is used when creating the TensorArray handle.  If this value is
set, handle should be None.
</td>
</tr><tr>
<td>
`handle`
</td>
<td>
(optional) A `Tensor` handle to an existing TensorArray.  If this
is set, tensor_array_name should be None. Only supported in graph mode.
</td>
</tr><tr>
<td>
`flow`
</td>
<td>
(optional) A float `Tensor` scalar coming from an existing
<a href="../tf/TensorArray.md#flow"><code>TensorArray.flow</code></a>. Only supported in graph mode.
</td>
</tr><tr>
<td>
`infer_shape`
</td>
<td>
(optional, default: True) If True, shape inference
is enabled.  In this case, all elements must have the same shape.
</td>
</tr><tr>
<td>
`element_shape`
</td>
<td>
(optional, default: None) A `TensorShape` object specifying
the shape constraints of each of the elements of the TensorArray.
Need not be fully defined.
</td>
</tr><tr>
<td>
`colocate_with_first_write_call`
</td>
<td>
If `True`, the TensorArray will be
colocated on the same device as the Tensor used on its first write
(write operations include `write`, `unstack`, and `split`).  If `False`,
the TensorArray will be placed on the device determined by the
device context available during its initialization.
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
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if both handle and tensor_array_name are provided.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
if handle is provided but is not a Tensor.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
The data type of this TensorArray.
</td>
</tr><tr>
<td>
`dynamic_size`
</td>
<td>
Python bool; if `True` the TensorArray can grow dynamically.
</td>
</tr><tr>
<td>
`element_shape`
</td>
<td>
The <a href="../tf/TensorShape.md"><code>tf.TensorShape</code></a> of elements in this TensorArray.
</td>
</tr><tr>
<td>
`flow`
</td>
<td>
The flow `Tensor` forcing ops leading to this TensorArray state.
</td>
</tr><tr>
<td>
`handle`
</td>
<td>
The reference to the TensorArray.
</td>
</tr>
</table>



## Methods

<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1268-L1271">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close(
    name=None
)
</code></pre>

Close the current TensorArray.

Note: The output of this function should be used. If it is not, a warning will be logged or an error may be raised. To mark the output as used, call its .mark_used() method.

<h3 id="concat"><code>concat</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1192-L1204">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>concat(
    name=None
)
</code></pre>

Return the values in the TensorArray as a concatenated `Tensor`.

All of the values must have been written, their ranks must match, and
and their shapes must all match for all dimensions except the first.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
All the tensors in the TensorArray concatenated into one tensor.
</td>
</tr>

</table>



<h3 id="gather"><code>gather</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1175-L1190">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>gather(
    indices, name=None
)
</code></pre>

Return selected values in the TensorArray as a packed `Tensor`.

All of selected values must have been written and their shapes
must all match.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`indices`
</td>
<td>
A `1-D` `Tensor` taking values in `[0, max_value)`.  If
the `TensorArray` is not dynamic, `max_value=size()`.
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
The tensors in the `TensorArray` selected by `indices`, packed into one
tensor.
</td>
</tr>

</table>



<h3 id="grad"><code>grad</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1128-L1129">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>grad(
    source, flow=None, name=None
)
</code></pre>




<h3 id="identity"><code>identity</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1118-L1126">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>identity()
</code></pre>

Returns a TensorArray with the same content and properties.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A new TensorArray object with flow that ensures the control dependencies
from the contexts will become control dependencies for writes, reads, etc.
Use this object for all subsequent operations.
</td>
</tr>

</table>



<h3 id="read"><code>read</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1131-L1141">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>read(
    index, name=None
)
</code></pre>

Read the value at location `index` in the TensorArray.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`index`
</td>
<td>
0-D.  int32 tensor with the index to read from.
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
The tensor at index `index`.
</td>
</tr>

</table>



<h3 id="scatter"><code>scatter</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1226-L1243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>scatter(
    indices, value, name=None
)
</code></pre>

Scatter the values of a `Tensor` in specific indices of a `TensorArray`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`indices`
</td>
<td>
A `1-D` `Tensor` taking values in `[0, max_value)`.  If
the `TensorArray` is not dynamic, `max_value=size()`.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
(N+1)-D.  Tensor of type `dtype`.  The Tensor to unpack.
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
A new TensorArray object with flow that ensures the scatter occurs.
Use this object for all subsequent operations.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the shape inference fails.
</td>
</tr>
</table>


Note: The output of this function should be used. If it is not, a warning will be logged or an error may be raised. To mark the output as used, call its .mark_used() method.

<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1264-L1266">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>size(
    name=None
)
</code></pre>

Return the size of the TensorArray.


<h3 id="split"><code>split</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1245-L1262">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>split(
    value, lengths, name=None
)
</code></pre>

Split the values of a `Tensor` into the TensorArray.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
(N+1)-D.  Tensor of type `dtype`.  The Tensor to split.
</td>
</tr><tr>
<td>
`lengths`
</td>
<td>
1-D.  int32 vector with the lengths to use when splitting
`value` along its first dimension.
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
A new TensorArray object with flow that ensures the split occurs.
Use this object for all subsequent operations.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the shape inference fails.
</td>
</tr>
</table>


Note: The output of this function should be used. If it is not, a warning will be logged or an error may be raised. To mark the output as used, call its .mark_used() method.

<h3 id="stack"><code>stack</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1161-L1173">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stack(
    name=None
)
</code></pre>

Return the values in the TensorArray as a stacked `Tensor`.

All of the values must have been written and their shapes must all match.
If input shapes have rank-`R`, then output shape will have rank-`(R+1)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
All the tensors in the TensorArray stacked into one tensor.
</td>
</tr>

</table>



<h3 id="unstack"><code>unstack</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1206-L1224">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>unstack(
    value, name=None
)
</code></pre>

Unstack the values of a `Tensor` in the TensorArray.

If input value shapes have rank-`R`, then the output TensorArray will
contain elements whose shapes are rank-`(R-1)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
(N+1)-D.  Tensor of type `dtype`.  The Tensor to unstack.
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
A new TensorArray object with flow that ensures the unstack occurs.
Use this object for all subsequent operations.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the shape inference fails.
</td>
</tr>
</table>


Note: The output of this function should be used. If it is not, a warning will be logged or an error may be raised. To mark the output as used, call its .mark_used() method.

<h3 id="write"><code>write</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/tensor_array_ops.py#L1143-L1159">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>write(
    index, value, name=None
)
</code></pre>

Write `value` into index `index` of the TensorArray.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`index`
</td>
<td>
0-D.  int32 scalar with the index to write to.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
N-D.  Tensor of type `dtype`.  The Tensor to write to this index.
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
A new TensorArray object with flow that ensures the write occurs.
Use this object for all subsequent operations.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if there are more writers than specified.
</td>
</tr>
</table>


Note: The output of this function should be used. If it is not, a warning will be logged or an error may be raised. To mark the output as used, call its .mark_used() method.



