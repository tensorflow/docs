

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.DType

## Class `DType`





Defined in [`tensorflow/python/framework/dtypes.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/framework/dtypes.py).

See the guide: [Building Graphs > Tensor types](../../../api_guides/python/framework#Tensor_types)

Represents the type of the elements in a `Tensor`.

The following `DType` objects are defined:

* <a href="../tf/float16"><code>tf.float16</code></a>: 16-bit half-precision floating-point.
* <a href="../tf/float32"><code>tf.float32</code></a>: 32-bit single-precision floating-point.
* <a href="../tf/double"><code>tf.float64</code></a>: 64-bit double-precision floating-point.
* <a href="../tf/bfloat16"><code>tf.bfloat16</code></a>: 16-bit truncated floating-point.
* <a href="../tf/complex64"><code>tf.complex64</code></a>: 64-bit single-precision complex.
* <a href="../tf/complex128"><code>tf.complex128</code></a>: 128-bit double-precision complex.
* <a href="../tf/int8"><code>tf.int8</code></a>: 8-bit signed integer.
* <a href="../tf/uint8"><code>tf.uint8</code></a>: 8-bit unsigned integer.
* <a href="../tf/uint16"><code>tf.uint16</code></a>: 16-bit unsigned integer.
* <a href="../tf/uint32"><code>tf.uint32</code></a>: 32-bit unsigned integer.
* <a href="../tf/uint64"><code>tf.uint64</code></a>: 64-bit unsigned integer.
* <a href="../tf/int16"><code>tf.int16</code></a>: 16-bit signed integer.
* <a href="../tf/int32"><code>tf.int32</code></a>: 32-bit signed integer.
* <a href="../tf/int64"><code>tf.int64</code></a>: 64-bit signed integer.
* <a href="../tf/bool"><code>tf.bool</code></a>: Boolean.
* <a href="../tf/string"><code>tf.string</code></a>: String.
* <a href="../tf/qint8"><code>tf.qint8</code></a>: Quantized 8-bit signed integer.
* <a href="../tf/quint8"><code>tf.quint8</code></a>: Quantized 8-bit unsigned integer.
* <a href="../tf/qint16"><code>tf.qint16</code></a>: Quantized 16-bit signed integer.
* <a href="../tf/quint16"><code>tf.quint16</code></a>: Quantized 16-bit unsigned integer.
* <a href="../tf/qint32"><code>tf.qint32</code></a>: Quantized 32-bit signed integer.
* <a href="../tf/resource"><code>tf.resource</code></a>: Handle to a mutable resource.
* <a href="../tf/variant"><code>tf.variant</code></a>: Values of arbitrary types.

In addition, variants of these types with the `_ref` suffix are
defined for reference-typed tensors.

The `tf.as_dtype()` function converts numpy types and string type
names to a `DType` object.

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

Return intensity limits, i.e. (min, max) tuple, of the dtype.
#### Args:

* <b>`clip_negative `</b>: bool, optional
      If True, clip the negative range (i.e. return 0 for min intensity)
      even if the image dtype allows negative values.
Returns
  min, max : tuple
    Lower and upper intensity limits.

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

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(type_enum)
```

Creates a new `DataType`.

NOTE(mrry): In normal circumstances, you should not need to
construct a `DataType` object directly. Instead, use the
`tf.as_dtype()` function.

#### Args:

* <b>`type_enum`</b>: A `types_pb2.DataType` enum value.


#### Raises:

* <b>`TypeError`</b>: If `type_enum` is not a value `types_pb2.DataType`.

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Returns True iff this DType refers to the same type as `other`.

<h3 id="__int__"><code>__int__</code></h3>

``` python
__int__()
```



<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```

Returns True iff self != other.

<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

``` python
is_compatible_with(other)
```

Returns True if the `other` DType will be converted to this DType.

The conversion rules are as follows:

```python
DType(T)       .is_compatible_with(DType(T))        == True
DType(T)       .is_compatible_with(DType(T).as_ref) == True
DType(T).as_ref.is_compatible_with(DType(T))        == False
DType(T).as_ref.is_compatible_with(DType(T).as_ref) == True
```

#### Args:

* <b>`other`</b>: A `DType` (or object that may be converted to a `DType`).


#### Returns:

True if a Tensor of the `other` `DType` will be implicitly converted to
this `DType`.



