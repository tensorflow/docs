description: Represents the type of the elements in a Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.dtypes.DType" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="is_compatible_with"/>
</div>

# tf.dtypes.DType

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/dtypes.py#L37-L216">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents the type of the elements in a `Tensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.DType`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.DType`, `tf.compat.v1.dtypes.DType`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.dtypes.DType()
</code></pre>



<!-- Placeholder for "Used in" -->

The following `DType` objects are defined:

* <a href="../../tf.md#float16"><code>tf.float16</code></a>: 16-bit half-precision floating-point.
* <a href="../../tf.md#float32"><code>tf.float32</code></a>: 32-bit single-precision floating-point.
* <a href="../../tf.md#float64"><code>tf.float64</code></a>: 64-bit double-precision floating-point.
* <a href="../../tf.md#bfloat16"><code>tf.bfloat16</code></a>: 16-bit truncated floating-point.
* <a href="../../tf.md#complex64"><code>tf.complex64</code></a>: 64-bit single-precision complex.
* <a href="../../tf.md#complex128"><code>tf.complex128</code></a>: 128-bit double-precision complex.
* <a href="../../tf.md#int8"><code>tf.int8</code></a>: 8-bit signed integer.
* <a href="../../tf.md#uint8"><code>tf.uint8</code></a>: 8-bit unsigned integer.
* <a href="../../tf.md#uint16"><code>tf.uint16</code></a>: 16-bit unsigned integer.
* <a href="../../tf.md#uint32"><code>tf.uint32</code></a>: 32-bit unsigned integer.
* <a href="../../tf.md#uint64"><code>tf.uint64</code></a>: 64-bit unsigned integer.
* <a href="../../tf.md#int16"><code>tf.int16</code></a>: 16-bit signed integer.
* <a href="../../tf.md#int32"><code>tf.int32</code></a>: 32-bit signed integer.
* <a href="../../tf.md#int64"><code>tf.int64</code></a>: 64-bit signed integer.
* <a href="../../tf.md#bool"><code>tf.bool</code></a>: Boolean.
* <a href="../../tf.md#string"><code>tf.string</code></a>: String.
* <a href="../../tf.md#qint8"><code>tf.qint8</code></a>: Quantized 8-bit signed integer.
* <a href="../../tf.md#quint8"><code>tf.quint8</code></a>: Quantized 8-bit unsigned integer.
* <a href="../../tf.md#qint16"><code>tf.qint16</code></a>: Quantized 16-bit signed integer.
* <a href="../../tf.md#quint16"><code>tf.quint16</code></a>: Quantized 16-bit unsigned integer.
* <a href="../../tf.md#qint32"><code>tf.qint32</code></a>: Quantized 32-bit signed integer.
* <a href="../../tf.md#resource"><code>tf.resource</code></a>: Handle to a mutable resource.
* <a href="../../tf.md#variant"><code>tf.variant</code></a>: Values of arbitrary types.

The <a href="../../tf/dtypes/as_dtype.md"><code>tf.as_dtype()</code></a> function converts numpy types and string type
names to a `DType` object.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`as_datatype_enum`
</td>
<td>
Returns a `types_pb2.DataType` enum value based on this data type.
</td>
</tr><tr>
<td>
`as_numpy_dtype`
</td>
<td>
Returns a Python `type` object based on this `DType`.
</td>
</tr><tr>
<td>
`base_dtype`
</td>
<td>
Returns a non-reference `DType` based on this `DType`.
</td>
</tr><tr>
<td>
`is_bool`
</td>
<td>
Returns whether this is a boolean data type.
</td>
</tr><tr>
<td>
`is_complex`
</td>
<td>
Returns whether this is a complex floating point type.
</td>
</tr><tr>
<td>
`is_floating`
</td>
<td>
Returns whether this is a (non-quantized, real) floating point type.
</td>
</tr><tr>
<td>
`is_integer`
</td>
<td>
Returns whether this is a (non-quantized) integer type.
</td>
</tr><tr>
<td>
`is_numpy_compatible`
</td>
<td>
Returns whether this data type has a compatible NumPy data type.
</td>
</tr><tr>
<td>
`is_quantized`
</td>
<td>
Returns whether this is a quantized data type.
</td>
</tr><tr>
<td>
`is_unsigned`
</td>
<td>
Returns whether this type is unsigned.

Non-numeric, unordered, and quantized types are not considered unsigned, and
this function returns `False`.
</td>
</tr><tr>
<td>
`limits`
</td>
<td>
Return intensity limits, i.e.

(min, max) tuple, of the dtype.
Args:
clip_negative : bool, optional If True, clip the negative range (i.e.
return 0 for min intensity) even if the image dtype allows negative
values. Returns
min, max : tuple Lower and upper intensity limits.
</td>
</tr><tr>
<td>
`max`
</td>
<td>
Returns the maximum representable value in this data type.
</td>
</tr><tr>
<td>
`min`
</td>
<td>
Returns the minimum representable value in this data type.
</td>
</tr><tr>
<td>
`name`
</td>
<td>

</td>
</tr><tr>
<td>
`real_dtype`
</td>
<td>
Returns the `DType` corresponding to this `DType`'s real part.
</td>
</tr><tr>
<td>
`size`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/dtypes.py#L172-L190">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_compatible_with(
    other
)
</code></pre>

Returns True if the `other` DType will be converted to this DType.

The conversion rules are as follows:

```python
DType(T)       .is_compatible_with(DType(T))        == True
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`other`
</td>
<td>
A `DType` (or object that may be converted to a `DType`).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
True if a Tensor of the `other` `DType` will be implicitly converted to
this `DType`.
</td>
</tr>

</table>



<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/dtypes.py#L192-L203">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Returns True iff this DType refers to the same type as `other`.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/dtypes.py#L205-L207">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Returns True iff self != other.




