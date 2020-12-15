description: Equivalent of numpy.ndarray backed by TensorFlow tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.numpy.ndarray" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__abs__"/>
<meta itemprop="property" content="__add__"/>
<meta itemprop="property" content="__bool__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__floordiv__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__invert__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="__matmul__"/>
<meta itemprop="property" content="__mod__"/>
<meta itemprop="property" content="__mul__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__neg__"/>
<meta itemprop="property" content="__nonzero__"/>
<meta itemprop="property" content="__pos__"/>
<meta itemprop="property" content="__pow__"/>
<meta itemprop="property" content="__radd__"/>
<meta itemprop="property" content="__rfloordiv__"/>
<meta itemprop="property" content="__rmatmul__"/>
<meta itemprop="property" content="__rmod__"/>
<meta itemprop="property" content="__rmul__"/>
<meta itemprop="property" content="__rpow__"/>
<meta itemprop="property" content="__rsub__"/>
<meta itemprop="property" content="__rtruediv__"/>
<meta itemprop="property" content="__sub__"/>
<meta itemprop="property" content="__truediv__"/>
<meta itemprop="property" content="astype"/>
<meta itemprop="property" content="clip"/>
<meta itemprop="property" content="from_tensor"/>
<meta itemprop="property" content="ravel"/>
<meta itemprop="property" content="reshape"/>
<meta itemprop="property" content="tolist"/>
<meta itemprop="property" content="transpose"/>
</div>

# tf.experimental.numpy.ndarray

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L99-L336">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Equivalent of numpy.ndarray backed by TensorFlow tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.numpy.ndarray(
    shape, dtype=float, buffer=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This does not support all features of NumPy ndarrays e.g. strides and
memory order since, unlike NumPy, the backing storage is not a raw memory
buffer.


or if there are any differences in behavior.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
The shape of the array. Must be a scalar, an iterable of integers
or a `TensorShape` object.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Optional. The dtype of the array. Must be a python type, a numpy
type or a tensorflow `DType` object.
</td>
</tr><tr>
<td>
`buffer`
</td>
<td>
Optional. The backing buffer of the array. Must have shape
`shape`. Must be a `ndarray`, `np.ndarray` or a `Tensor`.
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
If `buffer` is specified and its shape does not match
`shape`.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`T`
</td>
<td>

</td>
</tr><tr>
<td>
`data`
</td>
<td>
Tensor object containing the array data.

This has a few key differences from the Python buffer object used in
NumPy arrays.
1. Tensors are immutable. So operations requiring in-place edit, e.g.
__setitem__, are performed by replacing the underlying buffer with a new
one.
2. Tensors do not provide access to their raw buffer.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>

</td>
</tr><tr>
<td>
`ndim`
</td>
<td>

</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Returns a tuple or tf.Tensor of array dimensions.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
Returns the number of elements in the array.
</td>
</tr>
</table>



## Methods

<h3 id="astype"><code>astype</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L245-L249">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>astype(
    dtype
)
</code></pre>




<h3 id="clip"><code>clip</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L205-L217">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>clip(
    a, a_min, a_max
)
</code></pre>

TensorFlow variant of NumPy's `clip`.

Unsupported arguments: `out`, `kwargs`.

See the NumPy documentation for [`numpy.clip`](https://numpy.org/doc/1.16/reference/generated/numpy.clip.html).

<h3 id="from_tensor"><code>from_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L164-L172">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_tensor(
    tensor
)
</code></pre>




<h3 id="ravel"><code>ravel</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_array_ops.py#L697-L703">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>ravel(
    a
)
</code></pre>

TensorFlow variant of NumPy's `ravel`.

Unsupported arguments: `order`.

See the NumPy documentation for [`numpy.ravel`](https://numpy.org/doc/1.16/reference/generated/numpy.ravel.html).

<h3 id="reshape"><code>reshape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_array_ops.py#L791-L799">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reshape(
    a, *newshape, **kwargs
)
</code></pre>




<h3 id="tolist"><code>tolist</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L329-L330">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tolist()
</code></pre>




<h3 id="transpose"><code>transpose</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_array_ops.py#L814-L819">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>transpose(
    a, axes=None
)
</code></pre>

TensorFlow variant of NumPy's `transpose`.

See the NumPy documentation for [`numpy.transpose`](https://numpy.org/doc/1.16/reference/generated/numpy.transpose.html).

<h3 id="__abs__"><code>__abs__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L623-L625">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__abs__(
    x
)
</code></pre>

TensorFlow variant of NumPy's `absolute`.

Unsupported arguments: `out`, `where`, `casting`, `order`, `dtype`, `subok`, `signature`, `extobj`.

See the NumPy documentation for [`numpy.absolute`](https://numpy.org/doc/1.16/reference/generated/numpy.absolute.html).

<h3 id="__add__"><code>__add__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__add__(
    a, b
)
</code></pre>




<h3 id="__bool__"><code>__bool__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L266-L267">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__bool__()
</code></pre>




<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    a, b
)
</code></pre>




<h3 id="__floordiv__"><code>__floordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__floordiv__(
    a, b
)
</code></pre>




<h3 id="__ge__"><code>__ge__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ge__(
    a, b
)
</code></pre>




<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_array_ops.py#L1839-L1852">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    slice_spec
)
</code></pre>

Implementation of ndarray.__getitem__.


<h3 id="__gt__"><code>__gt__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__gt__(
    a, b
)
</code></pre>




<h3 id="__invert__"><code>__invert__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L1063-L1066">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__invert__(
    x
)
</code></pre>

TensorFlow variant of NumPy's `logical_not`.

Unsupported arguments: `out`, `where`, `casting`, `order`, `dtype`, `subok`, `signature`, `extobj`.

See the NumPy documentation for [`numpy.logical_not`](https://numpy.org/doc/1.16/reference/generated/numpy.logical_not.html).

<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L272-L278">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>




<h3 id="__le__"><code>__le__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__le__(
    a, b
)
</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L236-L243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>




<h3 id="__lt__"><code>__lt__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__lt__(
    a, b
)
</code></pre>




<h3 id="__matmul__"><code>__matmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__matmul__(
    a, b
)
</code></pre>




<h3 id="__mod__"><code>__mod__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mod__(
    a, b
)
</code></pre>




<h3 id="__mul__"><code>__mul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mul__(
    a, b
)
</code></pre>




<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    a, b
)
</code></pre>




<h3 id="__neg__"><code>__neg__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L252-L253">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__neg__()
</code></pre>




<h3 id="__nonzero__"><code>__nonzero__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L269-L270">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__nonzero__()
</code></pre>




<h3 id="__pos__"><code>__pos__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_arrays.py#L255-L256">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__pos__()
</code></pre>




<h3 id="__pow__"><code>__pow__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__pow__(
    a, b
)
</code></pre>




<h3 id="__radd__"><code>__radd__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__radd__(
    a, b
)
</code></pre>




<h3 id="__rfloordiv__"><code>__rfloordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rfloordiv__(
    a, b
)
</code></pre>




<h3 id="__rmatmul__"><code>__rmatmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmatmul__(
    a, b
)
</code></pre>




<h3 id="__rmod__"><code>__rmod__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmod__(
    a, b
)
</code></pre>




<h3 id="__rmul__"><code>__rmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmul__(
    a, b
)
</code></pre>




<h3 id="__rpow__"><code>__rpow__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rpow__(
    a, b
)
</code></pre>




<h3 id="__rsub__"><code>__rsub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rsub__(
    a, b
)
</code></pre>




<h3 id="__rtruediv__"><code>__rtruediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rtruediv__(
    a, b
)
</code></pre>




<h3 id="__sub__"><code>__sub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__sub__(
    a, b
)
</code></pre>




<h3 id="__truediv__"><code>__truediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_math_ops.py#L949-L957">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__truediv__(
    a, b
)
</code></pre>






