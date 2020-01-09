page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.DType


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/dtypes.py#L31-L296">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `DType`

Represents the type of the elements in a `Tensor`.



### Aliases:

* Class `tf.DType`
* Class `tf.compat.v1.DType`
* Class `tf.compat.v1.dtypes.DType`
* Class `tf.compat.v2.DType`
* Class `tf.compat.v2.dtypes.DType`


<!-- Placeholder for "Used in" -->

The following `DType` objects are defined:

* <a href="../../tf#float16"><code>tf.float16</code></a>: 16-bit half-precision floating-point.
* <a href="../../tf#float32"><code>tf.float32</code></a>: 32-bit single-precision floating-point.
* <a href="../../tf#float64"><code>tf.float64</code></a>: 64-bit double-precision floating-point.
* <a href="../../tf#bfloat16"><code>tf.bfloat16</code></a>: 16-bit truncated floating-point.
* <a href="../../tf#complex64"><code>tf.complex64</code></a>: 64-bit single-precision complex.
* <a href="../../tf#complex128"><code>tf.complex128</code></a>: 128-bit double-precision complex.
* <a href="../../tf#int8"><code>tf.int8</code></a>: 8-bit signed integer.
* <a href="../../tf#uint8"><code>tf.uint8</code></a>: 8-bit unsigned integer.
* <a href="../../tf#uint16"><code>tf.uint16</code></a>: 16-bit unsigned integer.
* <a href="../../tf#uint32"><code>tf.uint32</code></a>: 32-bit unsigned integer.
* <a href="../../tf#uint64"><code>tf.uint64</code></a>: 64-bit unsigned integer.
* <a href="../../tf#int16"><code>tf.int16</code></a>: 16-bit signed integer.
* <a href="../../tf#int32"><code>tf.int32</code></a>: 32-bit signed integer.
* <a href="../../tf#int64"><code>tf.int64</code></a>: 64-bit signed integer.
* <a href="../../tf#bool"><code>tf.bool</code></a>: Boolean.
* <a href="../../tf#string"><code>tf.string</code></a>: String.
* <a href="../../tf#qint8"><code>tf.qint8</code></a>: Quantized 8-bit signed integer.
* <a href="../../tf#quint8"><code>tf.quint8</code></a>: Quantized 8-bit unsigned integer.
* <a href="../../tf#qint16"><code>tf.qint16</code></a>: Quantized 16-bit signed integer.
* <a href="../../tf#quint16"><code>tf.quint16</code></a>: Quantized 16-bit unsigned integer.
* <a href="../../tf#qint32"><code>tf.qint32</code></a>: Quantized 32-bit signed integer.
* <a href="../../tf#resource"><code>tf.resource</code></a>: Handle to a mutable resource.
* <a href="../../tf#variant"><code>tf.variant</code></a>: Values of arbitrary types.

The <a href="../../tf/dtypes/as_dtype"><code>tf.as_dtype()</code></a> function converts numpy types and string type
names to a `DType` object.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/dtypes.py#L64-L85">View source</a>

``` python
__init__(type_enum)
```

Creates a new `DataType`.

NOTE(mrry): In normal circumstances, you should not need to
construct a `DataType` object directly. Instead, use the
<a href="../../tf/dtypes/as_dtype"><code>tf.as_dtype()</code></a> function.

#### Args:


* <b>`type_enum`</b>: A `types_pb2.DataType` enum value.


#### Raises:


* <b>`TypeError`</b>: If `type_enum` is not a value `types_pb2.DataType`.



## Properties

<h3 id="as_datatype_enum"><code>as_datatype_enum</code></h3>

Returns a `types_pb2.DataType` enum value based on this `DType`.


<h3 id="as_numpy_dtype"><code>as_numpy_dtype</code></h3>

Returns a `numpy.dtype` based on this `DType`.


<h3 id="base_dtype"><code>base_dtype</code></h3>

Returns a non-reference `DType` based on this `DType`.


<h3 id="is_bool"><code>is_bool</code></h3>

Returns whether this is a boolean data type


<h3 id="is_complex"><code>is_complex</code></h3>

Returns whether this is a complex floating point type.


<h3 id="is_floating"><code>is_floating</code></h3>

Returns whether this is a (non-quantized, real) floating point type.


<h3 id="is_integer"><code>is_integer</code></h3>

Returns whether this is a (non-quantized) integer type.


<h3 id="is_numpy_compatible"><code>is_numpy_compatible</code></h3>




<h3 id="is_quantized"><code>is_quantized</code></h3>

Returns whether this is a quantized data type.


<h3 id="is_unsigned"><code>is_unsigned</code></h3>

Returns whether this type is unsigned.

Non-numeric, unordered, and quantized types are not considered unsigned, and
this function returns `False`.

#### Returns:

Whether a `DType` is unsigned.


<h3 id="limits"><code>limits</code></h3>

Return intensity limits, i.e.

(min, max) tuple, of the dtype.
Args:
  clip_negative : bool, optional If True, clip the negative range (i.e.
    return 0 for min intensity) even if the image dtype allows negative
    values. Returns
  min, max : tuple Lower and upper intensity limits.

<h3 id="max"><code>max</code></h3>

Returns the maximum representable value in this data type.


#### Raises:


* <b>`TypeError`</b>: if this is a non-numeric, unordered, or quantized type.

<h3 id="min"><code>min</code></h3>

Returns the minimum representable value in this data type.


#### Raises:


* <b>`TypeError`</b>: if this is a non-numeric, unordered, or quantized type.

<h3 id="name"><code>name</code></h3>

Returns the string name for this `DType`.


<h3 id="real_dtype"><code>real_dtype</code></h3>

Returns the dtype correspond to this dtype's real part.


<h3 id="size"><code>size</code></h3>






## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/dtypes.py#L260-L268">View source</a>

``` python
__eq__(other)
```

Returns True iff this DType refers to the same type as `other`.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/dtypes.py#L270-L272">View source</a>

``` python
__ne__(other)
```

Returns True iff self != other.


<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/dtypes.py#L240-L258">View source</a>

``` python
is_compatible_with(other)
```

Returns True if the `other` DType will be converted to this DType.

The conversion rules are as follows:

```python
DType(T)       .is_compatible_with(DType(T))        == True
```

#### Args:


* <b>`other`</b>: A `DType` (or object that may be converted to a `DType`).


#### Returns:

True if a Tensor of the `other` `DType` will be implicitly converted to
this `DType`.
