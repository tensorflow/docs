description: # tf.experimental.numpy: NumPy API on TensorFlow.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.numpy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="e"/>
<meta itemprop="property" content="inf"/>
<meta itemprop="property" content="newaxis"/>
<meta itemprop="property" content="pi"/>
</div>

# Module: tf.experimental.numpy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



# tf.experimental.numpy: NumPy API on TensorFlow.


This module provides a subset of NumPy API, built on top of TensorFlow
operations. APIs are based on and have been tested with NumPy 1.16 version.

The set of supported APIs may be expanded over time. Also future releases may
change the baseline version of NumPy API being supported. A list of some
systematic differences with NumPy are listed later in the "Differences with
NumPy" section.

## Getting Started

Please also see [TensorFlow NumPy Guide](
https://www.tensorflow.org/guide/tf_numpy).

In the code snippets below, we will assume that <a href="../../tf/experimental/numpy.md"><code>tf.experimental.numpy</code></a> is
imported as `tnp` and NumPy is imported as `np`

```python
print(tnp.ones([2,1]) + tnp.ones([1, 2]))
```

## Types

The module provides an `ndarray` class which wraps an immutable <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>.
Additional functions are provided which accept array-like objects. Here
array-like objects includes `ndarrays` as defined by this module, as well as
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>, in addition to types accepted by NumPy.

A subset of NumPy dtypes are supported. Type promotion follows NumPy
semantics.

```python
print(tnp.ones([1, 2], dtype=tnp.int16) + tnp.ones([2, 1], dtype=tnp.uint8))
```

## Array Interface

The `ndarray` class implements the `__array__` interface. This should allow
these objects to be passed into contexts that expect a NumPy or array-like
object (e.g. matplotlib).

```python
np.sum(tnp.ones([1, 2]) + np.ones([2, 1]))
```


## TF Interoperability

The TF-NumPy API calls can be interleaved with TensorFlow calls
without incurring Tensor data copies. This is true even if the `ndarray` or
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> is placed on a non-CPU device.

In general, the expected behavior should be on par with that of code involving
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> and running stateless TensorFlow functions on them.

```python
tnp.sum(tnp.ones([1, 2]) + tf.ones([2, 1]))
```

Note that the `__array_priority__` is currently chosen to be lower than
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>. Hence the `+` operator above returns a `tf.Tensor`.

Additional examples of interopability include:

*  using `with tf.GradientTape()` scope to compute gradients through the
  TF-NumPy API calls.
*  using `tf.distribution.Strategy` scope for distributed execution
*  using <a href="../../tf/vectorized_map.md"><code>tf.vectorized_map()</code></a> for speeding up code using auto-vectorization



## Device Support

Given that `ndarray` and functions wrap TensorFlow constructs, the code will
have GPU and TPU support on par with TensorFlow. Device placement can be
controlled by using `with tf.device` scopes. Note that these devices could
be local or remote.

```python
with tf.device("GPU:0"):
  x = tnp.ones([1, 2])
print(tf.convert_to_tensor(x).device)
```

## Graph and Eager Modes

Eager mode execution should typically match NumPy semantics of executing
op-by-op. However the same code can be executed in graph mode, by putting it
inside a <a href="../../tf/function.md"><code>tf.function</code></a>. The function body can contain NumPy code, and the inputs
can be `ndarray` as well.

```python
@tf.function
def f(x, y):
  return tnp.sum(x + y)

f(tnp.ones([1, 2]), tf.ones([2, 1]))
```
Python control flow based on `ndarray` values will be translated by
[autograph](https://www.tensorflow.org/code/tensorflow/python/autograph/g3doc/reference/index.md)
into <a href="../../tf/cond.md"><code>tf.cond</code></a> and <a href="../../tf/while_loop.md"><code>tf.while_loop</code></a> constructs. The code can be XLA compiled
for further optimizations.

However, note that graph mode execution can change behavior of certain
operations since symbolic execution may not have information that is computed
during runtime. Some differences are:

*   Shapes can be incomplete or unknown in graph mode. This means that
    `ndarray.shape`, `ndarray.size` and `ndarray.ndim` can return `ndarray`
    objects instead of returning integer (or tuple of integer) values.
*   `__len__`, `__iter__` and `__index__` properties of `ndarray`
    may similarly not be supported in graph mode. Code using these
    may need to change to explicit shape operations or control flow
    constructs.
*   Also note the [autograph limitations](
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/limitations.md).


## Mutation and Variables

`ndarrays` currently wrap immutable <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>. Hence mutation
operations like slice assigns are not supported. This may change in the future.
Note however that one can directly construct a <a href="../../tf/Variable.md"><code>tf.Variable</code></a> and use that with
the TF-NumPy APIs.

```python
tf_var = tf.Variable(2.0)
tf_var.assign_add(tnp.square(tf_var))
```

## Differences with NumPy

Here is a non-exhaustive list of differences:

*   Not all dtypes are currently supported. e.g. `np.float96`, `np.float128`.
    `np.object`, `np.str`, `np.recarray` types are not supported.
*   `ndarray` storage is in C order only. Fortran order, views, `stride_tricks`
    are not supported.
*   Only a subset of functions and modules are supported. This set will be
    expanded over time. For supported functions, some arguments or argument
    values may not be supported. This differences are generally provide in the
    function comments. Full `ufunc` support is also not provided.
*   Buffer mutation is currently not supported. `ndarrays` wrap immutable
    tensors. This means that output buffer arguments (e..g `out` in ufuncs) are
    not supported
*   NumPy C API is not supported. NumPy's Cython and Swig integration are not
    supported.

## Modules

[`random`](../../tf/experimental/numpy/random.md) module: Public API for tf.experimental.numpy.random namespace.

## Classes

[`class bool_`](../../tf/experimental/numpy/bool_.md): Boolean type (True or False), stored as a byte.

[`class complex128`](../../tf/experimental/numpy/complex128.md): Complex number type composed of two double-precision floating-point

[`class complex64`](../../tf/experimental/numpy/complex64.md): Complex number type composed of two single-precision floating-point

[`class complex_`](../../tf/experimental/numpy/complex128.md): Complex number type composed of two double-precision floating-point

[`class float16`](../../tf/experimental/numpy/float16.md): Half-precision floating-point number type.

[`class float32`](../../tf/experimental/numpy/float32.md): Single-precision floating-point number type, compatible with C ``float``.

[`class float64`](../../tf/experimental/numpy/float64.md): Double-precision floating-point number type, compatible with Python `float`

[`class float_`](../../tf/experimental/numpy/float64.md): Double-precision floating-point number type, compatible with Python `float`

[`class iinfo`](../../tf/experimental/numpy/iinfo.md): iinfo(type)

[`class inexact`](../../tf/experimental/numpy/inexact.md): Abstract base class of all numeric scalar types with a (potentially)

[`class int16`](../../tf/experimental/numpy/int16.md): Signed integer type, compatible with C ``short``.

[`class int32`](../../tf/experimental/numpy/int32.md): Signed integer type, compatible with C ``int``.

[`class int64`](../../tf/experimental/numpy/int64.md): Signed integer type, compatible with Python `int` anc C ``long``.

[`class int8`](../../tf/experimental/numpy/int8.md): Signed integer type, compatible with C ``char``.

[`class int_`](../../tf/experimental/numpy/int64.md): Signed integer type, compatible with Python `int` anc C ``long``.

[`class ndarray`](../../tf/experimental/numpy/ndarray.md): Equivalent of numpy.ndarray backed by TensorFlow tensors.

[`class object_`](../../tf/experimental/numpy/object_.md): Any Python object.

[`class string_`](../../tf/experimental/numpy/string_.md): bytes(iterable_of_ints) -> bytes

[`class uint16`](../../tf/experimental/numpy/uint16.md): Unsigned integer type, compatible with C ``unsigned short``.

[`class uint32`](../../tf/experimental/numpy/uint32.md): Unsigned integer type, compatible with C ``unsigned int``.

[`class uint64`](../../tf/experimental/numpy/uint64.md): Unsigned integer type, compatible with C ``unsigned long``.

[`class uint8`](../../tf/experimental/numpy/uint8.md): Unsigned integer type, compatible with C ``unsigned char``.

[`class unicode_`](../../tf/experimental/numpy/unicode_.md): str(object='') -> str

## Functions

[`abs(...)`](../../tf/experimental/numpy/abs.md): TensorFlow variant of NumPy's `abs`.

[`absolute(...)`](../../tf/experimental/numpy/absolute.md): TensorFlow variant of NumPy's `absolute`.

[`add(...)`](../../tf/experimental/numpy/add.md): TensorFlow variant of NumPy's `add`.

[`all(...)`](../../tf/experimental/numpy/all.md): TensorFlow variant of NumPy's `all`.

[`allclose(...)`](../../tf/experimental/numpy/allclose.md): TensorFlow variant of NumPy's `allclose`.

[`amax(...)`](../../tf/experimental/numpy/amax.md): TensorFlow variant of NumPy's `amax`.

[`amin(...)`](../../tf/experimental/numpy/amin.md): TensorFlow variant of NumPy's `amin`.

[`angle(...)`](../../tf/experimental/numpy/angle.md): TensorFlow variant of NumPy's `angle`.

[`any(...)`](../../tf/experimental/numpy/any.md): TensorFlow variant of NumPy's `any`.

[`append(...)`](../../tf/experimental/numpy/append.md): TensorFlow variant of NumPy's `append`.

[`arange(...)`](../../tf/experimental/numpy/arange.md): TensorFlow variant of NumPy's `arange`.

[`arccos(...)`](../../tf/experimental/numpy/arccos.md): TensorFlow variant of NumPy's `arccos`.

[`arccosh(...)`](../../tf/experimental/numpy/arccosh.md): TensorFlow variant of NumPy's `arccosh`.

[`arcsin(...)`](../../tf/experimental/numpy/arcsin.md): TensorFlow variant of NumPy's `arcsin`.

[`arcsinh(...)`](../../tf/experimental/numpy/arcsinh.md): TensorFlow variant of NumPy's `arcsinh`.

[`arctan(...)`](../../tf/experimental/numpy/arctan.md): TensorFlow variant of NumPy's `arctan`.

[`arctan2(...)`](../../tf/experimental/numpy/arctan2.md): TensorFlow variant of NumPy's `arctan2`.

[`arctanh(...)`](../../tf/experimental/numpy/arctanh.md): TensorFlow variant of NumPy's `arctanh`.

[`argmax(...)`](../../tf/experimental/numpy/argmax.md): TensorFlow variant of NumPy's `argmax`.

[`argmin(...)`](../../tf/experimental/numpy/argmin.md): TensorFlow variant of NumPy's `argmin`.

[`argsort(...)`](../../tf/experimental/numpy/argsort.md): TensorFlow variant of NumPy's `argsort`.

[`around(...)`](../../tf/experimental/numpy/around.md): TensorFlow variant of NumPy's `around`.

[`array(...)`](../../tf/experimental/numpy/array.md): TensorFlow variant of NumPy's `array`.

[`array_equal(...)`](../../tf/experimental/numpy/array_equal.md): TensorFlow variant of NumPy's `array_equal`.

[`asanyarray(...)`](../../tf/experimental/numpy/asanyarray.md): TensorFlow variant of NumPy's `asanyarray`.

[`asarray(...)`](../../tf/experimental/numpy/asarray.md): TensorFlow variant of NumPy's `asarray`.

[`ascontiguousarray(...)`](../../tf/experimental/numpy/ascontiguousarray.md): TensorFlow variant of NumPy's `ascontiguousarray`.

[`atleast_1d(...)`](../../tf/experimental/numpy/atleast_1d.md): TensorFlow variant of NumPy's `atleast_1d`.

[`atleast_2d(...)`](../../tf/experimental/numpy/atleast_2d.md): TensorFlow variant of NumPy's `atleast_2d`.

[`atleast_3d(...)`](../../tf/experimental/numpy/atleast_3d.md): TensorFlow variant of NumPy's `atleast_3d`.

[`average(...)`](../../tf/experimental/numpy/average.md): TensorFlow variant of NumPy's `average`.

[`bitwise_and(...)`](../../tf/experimental/numpy/bitwise_and.md): TensorFlow variant of NumPy's `bitwise_and`.

[`bitwise_not(...)`](../../tf/experimental/numpy/bitwise_not.md): TensorFlow variant of NumPy's `bitwise_not`.

[`bitwise_or(...)`](../../tf/experimental/numpy/bitwise_or.md): TensorFlow variant of NumPy's `bitwise_or`.

[`bitwise_xor(...)`](../../tf/experimental/numpy/bitwise_xor.md): TensorFlow variant of NumPy's `bitwise_xor`.

[`broadcast_arrays(...)`](../../tf/experimental/numpy/broadcast_arrays.md): TensorFlow variant of NumPy's `broadcast_arrays`.

[`broadcast_to(...)`](../../tf/experimental/numpy/broadcast_to.md): TensorFlow variant of NumPy's `broadcast_to`.

[`cbrt(...)`](../../tf/experimental/numpy/cbrt.md): TensorFlow variant of NumPy's `cbrt`.

[`ceil(...)`](../../tf/experimental/numpy/ceil.md): TensorFlow variant of NumPy's `ceil`.

[`clip(...)`](../../tf/experimental/numpy/clip.md): TensorFlow variant of NumPy's `clip`.

[`compress(...)`](../../tf/experimental/numpy/compress.md): TensorFlow variant of NumPy's `compress`.

[`concatenate(...)`](../../tf/experimental/numpy/concatenate.md): TensorFlow variant of NumPy's `concatenate`.

[`conj(...)`](../../tf/experimental/numpy/conj.md): TensorFlow variant of NumPy's `conj`.

[`conjugate(...)`](../../tf/experimental/numpy/conjugate.md): TensorFlow variant of NumPy's `conjugate`.

[`copy(...)`](../../tf/experimental/numpy/copy.md): TensorFlow variant of NumPy's `copy`.

[`cos(...)`](../../tf/experimental/numpy/cos.md): TensorFlow variant of NumPy's `cos`.

[`cosh(...)`](../../tf/experimental/numpy/cosh.md): TensorFlow variant of NumPy's `cosh`.

[`count_nonzero(...)`](../../tf/experimental/numpy/count_nonzero.md): TensorFlow variant of NumPy's `count_nonzero`.

[`cross(...)`](../../tf/experimental/numpy/cross.md): TensorFlow variant of NumPy's `cross`.

[`cumprod(...)`](../../tf/experimental/numpy/cumprod.md): TensorFlow variant of NumPy's `cumprod`.

[`cumsum(...)`](../../tf/experimental/numpy/cumsum.md): TensorFlow variant of NumPy's `cumsum`.

[`deg2rad(...)`](../../tf/experimental/numpy/deg2rad.md): TensorFlow variant of NumPy's `deg2rad`.

[`diag(...)`](../../tf/experimental/numpy/diag.md): TensorFlow variant of NumPy's `diag`.

[`diag_indices(...)`](../../tf/experimental/numpy/diag_indices.md): TensorFlow variant of NumPy's `diag_indices`.

[`diagflat(...)`](../../tf/experimental/numpy/diagflat.md): TensorFlow variant of NumPy's `diagflat`.

[`diagonal(...)`](../../tf/experimental/numpy/diagonal.md): TensorFlow variant of NumPy's `diagonal`.

[`diff(...)`](../../tf/experimental/numpy/diff.md): TensorFlow variant of NumPy's `diff`.

[`divide(...)`](../../tf/experimental/numpy/divide.md): TensorFlow variant of NumPy's `divide`.

[`divmod(...)`](../../tf/experimental/numpy/divmod.md): TensorFlow variant of NumPy's `divmod`.

[`dot(...)`](../../tf/experimental/numpy/dot.md): TensorFlow variant of NumPy's `dot`.

[`dsplit(...)`](../../tf/experimental/numpy/dsplit.md): TensorFlow variant of NumPy's `dsplit`.

[`dstack(...)`](../../tf/experimental/numpy/dstack.md): TensorFlow variant of NumPy's `dstack`.

[`einsum(...)`](../../tf/experimental/numpy/einsum.md): TensorFlow variant of NumPy's `einsum`.

[`empty(...)`](../../tf/experimental/numpy/empty.md): TensorFlow variant of NumPy's `empty`.

[`empty_like(...)`](../../tf/experimental/numpy/empty_like.md): TensorFlow variant of NumPy's `empty_like`.

[`equal(...)`](../../tf/experimental/numpy/equal.md): TensorFlow variant of NumPy's `equal`.

[`exp(...)`](../../tf/experimental/numpy/exp.md): TensorFlow variant of NumPy's `exp`.

[`exp2(...)`](../../tf/experimental/numpy/exp2.md): TensorFlow variant of NumPy's `exp2`.

[`expand_dims(...)`](../../tf/experimental/numpy/expand_dims.md): TensorFlow variant of NumPy's `expand_dims`.

[`expm1(...)`](../../tf/experimental/numpy/expm1.md): TensorFlow variant of NumPy's `expm1`.

[`eye(...)`](../../tf/experimental/numpy/eye.md): TensorFlow variant of NumPy's `eye`.

[`fabs(...)`](../../tf/experimental/numpy/fabs.md): TensorFlow variant of NumPy's `fabs`.

[`finfo(...)`](../../tf/experimental/numpy/finfo.md): TensorFlow variant of NumPy's `finfo`.

[`fix(...)`](../../tf/experimental/numpy/fix.md): TensorFlow variant of NumPy's `fix`.

[`flip(...)`](../../tf/experimental/numpy/flip.md): TensorFlow variant of NumPy's `flip`.

[`fliplr(...)`](../../tf/experimental/numpy/fliplr.md): TensorFlow variant of NumPy's `fliplr`.

[`flipud(...)`](../../tf/experimental/numpy/flipud.md): TensorFlow variant of NumPy's `flipud`.

[`float_power(...)`](../../tf/experimental/numpy/float_power.md): TensorFlow variant of NumPy's `float_power`.

[`floor(...)`](../../tf/experimental/numpy/floor.md): TensorFlow variant of NumPy's `floor`.

[`floor_divide(...)`](../../tf/experimental/numpy/floor_divide.md): TensorFlow variant of NumPy's `floor_divide`.

[`full(...)`](../../tf/experimental/numpy/full.md): TensorFlow variant of NumPy's `full`.

[`full_like(...)`](../../tf/experimental/numpy/full_like.md): TensorFlow variant of NumPy's `full_like`.

[`gcd(...)`](../../tf/experimental/numpy/gcd.md): TensorFlow variant of NumPy's `gcd`.

[`geomspace(...)`](../../tf/experimental/numpy/geomspace.md): TensorFlow variant of NumPy's `geomspace`.

[`greater(...)`](../../tf/experimental/numpy/greater.md): TensorFlow variant of NumPy's `greater`.

[`greater_equal(...)`](../../tf/experimental/numpy/greater_equal.md): TensorFlow variant of NumPy's `greater_equal`.

[`heaviside(...)`](../../tf/experimental/numpy/heaviside.md): TensorFlow variant of NumPy's `heaviside`.

[`hsplit(...)`](../../tf/experimental/numpy/hsplit.md): TensorFlow variant of NumPy's `hsplit`.

[`hstack(...)`](../../tf/experimental/numpy/hstack.md): TensorFlow variant of NumPy's `hstack`.

[`hypot(...)`](../../tf/experimental/numpy/hypot.md): TensorFlow variant of NumPy's `hypot`.

[`identity(...)`](../../tf/experimental/numpy/identity.md): TensorFlow variant of NumPy's `identity`.

[`imag(...)`](../../tf/experimental/numpy/imag.md): TensorFlow variant of NumPy's `imag`.

[`inner(...)`](../../tf/experimental/numpy/inner.md): TensorFlow variant of NumPy's `inner`.

[`isclose(...)`](../../tf/experimental/numpy/isclose.md): TensorFlow variant of NumPy's `isclose`.

[`iscomplex(...)`](../../tf/experimental/numpy/iscomplex.md): TensorFlow variant of NumPy's `iscomplex`.

[`iscomplexobj(...)`](../../tf/experimental/numpy/iscomplexobj.md): TensorFlow variant of NumPy's `iscomplexobj`.

[`isfinite(...)`](../../tf/experimental/numpy/isfinite.md): TensorFlow variant of NumPy's `isfinite`.

[`isinf(...)`](../../tf/experimental/numpy/isinf.md): TensorFlow variant of NumPy's `isinf`.

[`isnan(...)`](../../tf/experimental/numpy/isnan.md): TensorFlow variant of NumPy's `isnan`.

[`isneginf(...)`](../../tf/experimental/numpy/isneginf.md): TensorFlow variant of NumPy's `isneginf`.

[`isposinf(...)`](../../tf/experimental/numpy/isposinf.md): TensorFlow variant of NumPy's `isposinf`.

[`isreal(...)`](../../tf/experimental/numpy/isreal.md): TensorFlow variant of NumPy's `isreal`.

[`isrealobj(...)`](../../tf/experimental/numpy/isrealobj.md): TensorFlow variant of NumPy's `isrealobj`.

[`isscalar(...)`](../../tf/experimental/numpy/isscalar.md): TensorFlow variant of NumPy's `isscalar`.

[`issubdtype(...)`](../../tf/experimental/numpy/issubdtype.md): Returns True if first argument is a typecode lower/equal in type hierarchy.

[`ix_(...)`](../../tf/experimental/numpy/ix_.md): TensorFlow variant of NumPy's `ix_`.

[`kron(...)`](../../tf/experimental/numpy/kron.md): TensorFlow variant of NumPy's `kron`.

[`lcm(...)`](../../tf/experimental/numpy/lcm.md): TensorFlow variant of NumPy's `lcm`.

[`less(...)`](../../tf/experimental/numpy/less.md): TensorFlow variant of NumPy's `less`.

[`less_equal(...)`](../../tf/experimental/numpy/less_equal.md): TensorFlow variant of NumPy's `less_equal`.

[`linspace(...)`](../../tf/experimental/numpy/linspace.md): TensorFlow variant of NumPy's `linspace`.

[`log(...)`](../../tf/experimental/numpy/log.md): TensorFlow variant of NumPy's `log`.

[`log10(...)`](../../tf/experimental/numpy/log10.md): TensorFlow variant of NumPy's `log10`.

[`log1p(...)`](../../tf/experimental/numpy/log1p.md): TensorFlow variant of NumPy's `log1p`.

[`log2(...)`](../../tf/experimental/numpy/log2.md): TensorFlow variant of NumPy's `log2`.

[`logaddexp(...)`](../../tf/experimental/numpy/logaddexp.md): TensorFlow variant of NumPy's `logaddexp`.

[`logaddexp2(...)`](../../tf/experimental/numpy/logaddexp2.md): TensorFlow variant of NumPy's `logaddexp2`.

[`logical_and(...)`](../../tf/experimental/numpy/logical_and.md): TensorFlow variant of NumPy's `logical_and`.

[`logical_not(...)`](../../tf/experimental/numpy/logical_not.md): TensorFlow variant of NumPy's `logical_not`.

[`logical_or(...)`](../../tf/experimental/numpy/logical_or.md): TensorFlow variant of NumPy's `logical_or`.

[`logical_xor(...)`](../../tf/experimental/numpy/logical_xor.md): TensorFlow variant of NumPy's `logical_xor`.

[`logspace(...)`](../../tf/experimental/numpy/logspace.md): TensorFlow variant of NumPy's `logspace`.

[`matmul(...)`](../../tf/experimental/numpy/matmul.md): TensorFlow variant of NumPy's `matmul`.

[`max(...)`](../../tf/experimental/numpy/max.md): TensorFlow variant of NumPy's `max`.

[`maximum(...)`](../../tf/experimental/numpy/maximum.md): TensorFlow variant of NumPy's `maximum`.

[`mean(...)`](../../tf/experimental/numpy/mean.md): TensorFlow variant of NumPy's `mean`.

[`meshgrid(...)`](../../tf/experimental/numpy/meshgrid.md): TensorFlow variant of NumPy's `meshgrid`.

[`min(...)`](../../tf/experimental/numpy/min.md): TensorFlow variant of NumPy's `min`.

[`minimum(...)`](../../tf/experimental/numpy/minimum.md): TensorFlow variant of NumPy's `minimum`.

[`mod(...)`](../../tf/experimental/numpy/mod.md): TensorFlow variant of NumPy's `mod`.

[`moveaxis(...)`](../../tf/experimental/numpy/moveaxis.md): TensorFlow variant of NumPy's `moveaxis`.

[`multiply(...)`](../../tf/experimental/numpy/multiply.md): TensorFlow variant of NumPy's `multiply`.

[`nanmean(...)`](../../tf/experimental/numpy/nanmean.md): TensorFlow variant of NumPy's `nanmean`.

[`nanprod(...)`](../../tf/experimental/numpy/nanprod.md): TensorFlow variant of NumPy's `nanprod`.

[`nansum(...)`](../../tf/experimental/numpy/nansum.md): TensorFlow variant of NumPy's `nansum`.

[`ndim(...)`](../../tf/experimental/numpy/ndim.md): TensorFlow variant of NumPy's `ndim`.

[`negative(...)`](../../tf/experimental/numpy/negative.md): TensorFlow variant of NumPy's `negative`.

[`nextafter(...)`](../../tf/experimental/numpy/nextafter.md): TensorFlow variant of NumPy's `nextafter`.

[`nonzero(...)`](../../tf/experimental/numpy/nonzero.md): TensorFlow variant of NumPy's `nonzero`.

[`not_equal(...)`](../../tf/experimental/numpy/not_equal.md): TensorFlow variant of NumPy's `not_equal`.

[`ones(...)`](../../tf/experimental/numpy/ones.md): TensorFlow variant of NumPy's `ones`.

[`ones_like(...)`](../../tf/experimental/numpy/ones_like.md): TensorFlow variant of NumPy's `ones_like`.

[`outer(...)`](../../tf/experimental/numpy/outer.md): TensorFlow variant of NumPy's `outer`.

[`pad(...)`](../../tf/experimental/numpy/pad.md): TensorFlow variant of NumPy's `pad`.

[`polyval(...)`](../../tf/experimental/numpy/polyval.md): TensorFlow variant of NumPy's `polyval`.

[`positive(...)`](../../tf/experimental/numpy/positive.md): TensorFlow variant of NumPy's `positive`.

[`power(...)`](../../tf/experimental/numpy/power.md): TensorFlow variant of NumPy's `power`.

[`prod(...)`](../../tf/experimental/numpy/prod.md): TensorFlow variant of NumPy's `prod`.

[`promote_types(...)`](../../tf/experimental/numpy/promote_types.md): TensorFlow variant of NumPy's `promote_types`.

[`ptp(...)`](../../tf/experimental/numpy/ptp.md): TensorFlow variant of NumPy's `ptp`.

[`rad2deg(...)`](../../tf/experimental/numpy/rad2deg.md): TensorFlow variant of NumPy's `rad2deg`.

[`ravel(...)`](../../tf/experimental/numpy/ravel.md): TensorFlow variant of NumPy's `ravel`.

[`real(...)`](../../tf/experimental/numpy/real.md): TensorFlow variant of NumPy's `real`.

[`reciprocal(...)`](../../tf/experimental/numpy/reciprocal.md): TensorFlow variant of NumPy's `reciprocal`.

[`remainder(...)`](../../tf/experimental/numpy/remainder.md): TensorFlow variant of NumPy's `remainder`.

[`repeat(...)`](../../tf/experimental/numpy/repeat.md): TensorFlow variant of NumPy's `repeat`.

[`reshape(...)`](../../tf/experimental/numpy/reshape.md): TensorFlow variant of NumPy's `reshape`.

[`result_type(...)`](../../tf/experimental/numpy/result_type.md): TensorFlow variant of NumPy's `result_type`.

[`roll(...)`](../../tf/experimental/numpy/roll.md): TensorFlow variant of NumPy's `roll`.

[`rot90(...)`](../../tf/experimental/numpy/rot90.md): TensorFlow variant of NumPy's `rot90`.

[`round(...)`](../../tf/experimental/numpy/round.md): TensorFlow variant of NumPy's `round`.

[`select(...)`](../../tf/experimental/numpy/select.md): TensorFlow variant of NumPy's `select`.

[`shape(...)`](../../tf/experimental/numpy/shape.md): TensorFlow variant of NumPy's `shape`.

[`sign(...)`](../../tf/experimental/numpy/sign.md): TensorFlow variant of NumPy's `sign`.

[`signbit(...)`](../../tf/experimental/numpy/signbit.md): TensorFlow variant of NumPy's `signbit`.

[`sin(...)`](../../tf/experimental/numpy/sin.md): TensorFlow variant of NumPy's `sin`.

[`sinc(...)`](../../tf/experimental/numpy/sinc.md): TensorFlow variant of NumPy's `sinc`.

[`sinh(...)`](../../tf/experimental/numpy/sinh.md): TensorFlow variant of NumPy's `sinh`.

[`size(...)`](../../tf/experimental/numpy/size.md): TensorFlow variant of NumPy's `size`.

[`sort(...)`](../../tf/experimental/numpy/sort.md): TensorFlow variant of NumPy's `sort`.

[`split(...)`](../../tf/experimental/numpy/split.md): TensorFlow variant of NumPy's `split`.

[`sqrt(...)`](../../tf/experimental/numpy/sqrt.md): TensorFlow variant of NumPy's `sqrt`.

[`square(...)`](../../tf/experimental/numpy/square.md): TensorFlow variant of NumPy's `square`.

[`squeeze(...)`](../../tf/experimental/numpy/squeeze.md): TensorFlow variant of NumPy's `squeeze`.

[`stack(...)`](../../tf/experimental/numpy/stack.md): TensorFlow variant of NumPy's `stack`.

[`std(...)`](../../tf/experimental/numpy/std.md): TensorFlow variant of NumPy's `std`.

[`subtract(...)`](../../tf/experimental/numpy/subtract.md): TensorFlow variant of NumPy's `subtract`.

[`sum(...)`](../../tf/experimental/numpy/sum.md): TensorFlow variant of NumPy's `sum`.

[`swapaxes(...)`](../../tf/experimental/numpy/swapaxes.md): TensorFlow variant of NumPy's `swapaxes`.

[`take(...)`](../../tf/experimental/numpy/take.md): TensorFlow variant of NumPy's `take`.

[`take_along_axis(...)`](../../tf/experimental/numpy/take_along_axis.md): TensorFlow variant of NumPy's `take_along_axis`.

[`tan(...)`](../../tf/experimental/numpy/tan.md): TensorFlow variant of NumPy's `tan`.

[`tanh(...)`](../../tf/experimental/numpy/tanh.md): TensorFlow variant of NumPy's `tanh`.

[`tensordot(...)`](../../tf/experimental/numpy/tensordot.md): TensorFlow variant of NumPy's `tensordot`.

[`tile(...)`](../../tf/experimental/numpy/tile.md): TensorFlow variant of NumPy's `tile`.

[`trace(...)`](../../tf/experimental/numpy/trace.md): TensorFlow variant of NumPy's `trace`.

[`transpose(...)`](../../tf/experimental/numpy/transpose.md): TensorFlow variant of NumPy's `transpose`.

[`tri(...)`](../../tf/experimental/numpy/tri.md): TensorFlow variant of NumPy's `tri`.

[`tril(...)`](../../tf/experimental/numpy/tril.md): TensorFlow variant of NumPy's `tril`.

[`triu(...)`](../../tf/experimental/numpy/triu.md): TensorFlow variant of NumPy's `triu`.

[`true_divide(...)`](../../tf/experimental/numpy/true_divide.md): TensorFlow variant of NumPy's `true_divide`.

[`vander(...)`](../../tf/experimental/numpy/vander.md): TensorFlow variant of NumPy's `vander`.

[`var(...)`](../../tf/experimental/numpy/var.md): TensorFlow variant of NumPy's `var`.

[`vdot(...)`](../../tf/experimental/numpy/vdot.md): TensorFlow variant of NumPy's `vdot`.

[`vsplit(...)`](../../tf/experimental/numpy/vsplit.md): TensorFlow variant of NumPy's `vsplit`.

[`vstack(...)`](../../tf/experimental/numpy/vstack.md): TensorFlow variant of NumPy's `vstack`.

[`where(...)`](../../tf/experimental/numpy/where.md): TensorFlow variant of NumPy's `where`.

[`zeros(...)`](../../tf/experimental/numpy/zeros.md): TensorFlow variant of NumPy's `zeros`.

[`zeros_like(...)`](../../tf/experimental/numpy/zeros_like.md): TensorFlow variant of NumPy's `zeros_like`.

## Other Members

* `e = 2.718281828459045` <a id="e"></a>
* `inf = inf` <a id="inf"></a>
* `newaxis = None` <a id="newaxis"></a>
* `pi = 3.141592653589793` <a id="pi"></a>
