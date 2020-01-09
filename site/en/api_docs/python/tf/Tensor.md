page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.Tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/Tensor">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L288-L851">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Tensor`

Represents one of the outputs of an `Operation`.



### Aliases:

* Class <a href="/api_docs/python/tf/Tensor"><code>tf.compat.v1.Tensor</code></a>
* Class <a href="/api_docs/python/tf/Tensor"><code>tf.compat.v2.Tensor</code></a>


<!-- Placeholder for "Used in" -->

A `Tensor` is a symbolic handle to one of the outputs of an
`Operation`. It does not hold the values of that operation's output,
but instead provides a means of computing those values in a
TensorFlow <a href="../tf/Session"><code>tf.compat.v1.Session</code></a>.

This class has two primary purposes:

1. A `Tensor` can be passed as an input to another `Operation`.
   This builds a dataflow connection between operations, which
   enables TensorFlow to execute an entire `Graph` that represents a
   large, multi-step computation.

2. After the graph has been launched in a session, the value of the
   `Tensor` can be computed by passing it to
   <a href="../tf/Session#run"><code>tf.Session.run</code></a>.
   `t.eval()` is a shortcut for calling
   `tf.compat.v1.get_default_session().run(t)`.

In the following example, `c`, `d`, and `e` are symbolic `Tensor`
objects, whereas `result` is a numpy array that stores a concrete
value:

```python
# Build a dataflow graph.
c = tf.constant([[1.0, 2.0], [3.0, 4.0]])
d = tf.constant([[1.0, 1.0], [0.0, 1.0]])
e = tf.matmul(c, d)

# Construct a `Session` to execute the graph.
sess = tf.compat.v1.Session()

# Execute the graph and store the value that `e` represents in `result`.
result = sess.run(e)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L370-L395">View source</a>

``` python
__init__(
    op,
    value_index,
    dtype
)
```

Creates a new `Tensor`.


#### Args:


* <b>`op`</b>: An `Operation`. `Operation` that computes this tensor.
* <b>`value_index`</b>: An `int`. Index of the operation's endpoint that produces
  this tensor.
* <b>`dtype`</b>: A `DType`. Type of elements stored in this tensor.


#### Raises:


* <b>`TypeError`</b>: If the op is not an `Operation`.



## Properties

<h3 id="device"><code>device</code></h3>

The name of the device on which this tensor will be produced, or None.


<h3 id="dtype"><code>dtype</code></h3>

The `DType` of elements in this tensor.


<h3 id="graph"><code>graph</code></h3>

The `Graph` that contains this tensor.


<h3 id="name"><code>name</code></h3>

The string name of this tensor.


<h3 id="op"><code>op</code></h3>

The `Operation` that produces this tensor as an output.


<h3 id="shape"><code>shape</code></h3>

Returns the `TensorShape` that represents the shape of this tensor.

The shape is computed using shape inference functions that are
registered in the Op for each `Operation`.  See
<a href="../tf/TensorShape"><code>tf.TensorShape</code></a>
for more details of what a shape represents.

The inferred shape of a tensor is used to provide shape
information without having to launch the graph in a session. This
can be used for debugging, and providing early error messages. For
example:

```python
c = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

print(c.shape)
==> TensorShape([Dimension(2), Dimension(3)])

d = tf.constant([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, 1.0]])

print(d.shape)
==> TensorShape([Dimension(4), Dimension(2)])

# Raises a ValueError, because `c` and `d` do not have compatible
# inner dimensions.
e = tf.matmul(c, d)

f = tf.matmul(c, d, transpose_a=True, transpose_b=True)

print(f.shape)
==> TensorShape([Dimension(3), Dimension(4)])
```

In some cases, the inferred shape may have unknown dimensions. If
the caller has additional information about the values of these
dimensions, <a href="../tf/Tensor#set_shape"><code>Tensor.set_shape()</code></a> can be used to augment the
inferred shape.

#### Returns:

A `TensorShape` representing the shape of this tensor.


<h3 id="value_index"><code>value_index</code></h3>

The index of this tensor in the outputs of its `Operation`.




## Methods

<h3 id="__abs__"><code>__abs__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L245-L278">View source</a>

``` python
__abs__(
    x,
    name=None
)
```

Computes the absolute value of a tensor.

Given a tensor of integer or floating-point values, this operation returns a
tensor of the same type, where each element contains the absolute value of the
corresponding element in the input.

Given a tensor `x` of complex numbers, this operation returns a tensor of type
`float32` or `float64` that is the absolute value of each element in `x`. All
elements in `x` must be complex numbers of the form \\(a + bj\\). The
absolute value is computed as \\( \sqrt{a^2 + b^2}\\).  For example:

```python
x = tf.constant([[-2.25 + 4.75j], [-3.25 + 5.75j]])
tf.abs(x)  # [5.25594902, 6.60492229]
```

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` of type `float16`, `float32`, `float64`,
  `int32`, `int64`, `complex64` or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` the same size, type, and sparsity as `x` with
  absolute values.
Note, for `complex64` or `complex128` input, the returned `Tensor` will be
  of type `float32` or `float64`, respectively.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.abs(x.values, ...), x.dense_shape)`


<h3 id="__add__"><code>__add__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__add__(
    x,
    y
)
```

Dispatches to add for strings and add_v2 for all other types.


<h3 id="__and__"><code>__and__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__and__(
    x,
    y
)
```

Returns the truth value of x AND y element-wise.

*NOTE*: <a href="../tf/math/logical_and"><code>math.logical_and</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`y`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__bool__"><code>__bool__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L747-L765">View source</a>

``` python
__bool__()
```

Dummy method to prevent a tensor from being used as a Python `bool`.

This overload raises a `TypeError` when the user inadvertently
treats a `Tensor` as a boolean (most commonly in an `if` or `while`
statement), in code that was not converted by AutoGraph. For example:

```python
if tf.constant(True):  # Will raise.
  # ...

if tf.constant(5) < tf.constant(7):  # Will raise.
  # ...
```

#### Raises:

`TypeError`.


<h3 id="__div__"><code>__div__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__div__(
    x,
    y
)
```

Divide two values using Python 2 semantics.

Used for Tensor.__div__.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` returns the quotient of x and y.


<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L1328-L1339">View source</a>

``` python
__eq__(other)
```

Compares two tensors element-wise for equality.


<h3 id="__floordiv__"><code>__floordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__floordiv__(
    x,
    y
)
```

Divides `x / y` elementwise, rounding toward the most negative integer.

The same as <a href="../tf/div"><code>tf.compat.v1.div(x,y)</code></a> for integers, but uses
`tf.floor(tf.compat.v1.div(x,y))` for
floating point arguments so that the result is always an integer (though
possibly an integer represented as floating point).  This op is generated by
`x // y` floor division in Python 3 and in Python 2.7 with
`from __future__ import division`.

`x` and `y` must have the same type, and the result will have the same type
as well.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` rounded down.



#### Raises:


* <b>`TypeError`</b>: If the inputs are complex.

<h3 id="__ge__"><code>__ge__</code></h3>

Defined in generated file: `python/ops/gen_math_ops.py`

``` python
__ge__(
    x,
    y,
    name=None
)
```

Returns the truth value of (x >= y) element-wise.

*NOTE*: <a href="../tf/math/greater_equal"><code>math.greater_equal</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L658-L802">View source</a>

``` python
__getitem__(
    tensor,
    slice_spec,
    var=None
)
```

Overload for Tensor.__getitem__.

This operation extracts the specified region from the tensor.
The notation is similar to NumPy with the restriction that
currently only support basic indexing. That means that
using a non-scalar tensor as input is not currently allowed.

#### Some useful examples:



```python
# Strip leading and trailing 2 elements
foo = tf.constant([1,2,3,4,5,6])
print(foo[2:-2].eval())  # => [3,4]

# Skip every other row and reverse the order of the columns
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[::2,::-1].eval())  # => [[3,2,1], [9,8,7]]

# Use scalar tensors as indices on both dimensions
print(foo[tf.constant(0), tf.constant(2)].eval())  # => 3

# Insert another dimension
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[tf.newaxis, :, :].eval()) # => [[[1,2,3], [4,5,6], [7,8,9]]]
print(foo[:, tf.newaxis, :].eval()) # => [[[1,2,3]], [[4,5,6]], [[7,8,9]]]
print(foo[:, :, tf.newaxis].eval()) # => [[[1],[2],[3]], [[4],[5],[6]],
[[7],[8],[9]]]

# Ellipses (3 equivalent operations)
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[tf.newaxis, :, :].eval())  # => [[[1,2,3], [4,5,6], [7,8,9]]]
print(foo[tf.newaxis, ...].eval())  # => [[[1,2,3], [4,5,6], [7,8,9]]]
print(foo[tf.newaxis].eval())  # => [[[1,2,3], [4,5,6], [7,8,9]]]

# Masks
foo = tf.constant([[1,2,3], [4,5,6], [7,8,9]])
print(foo[foo > 2].eval())  # => [3, 4, 5, 6, 7, 8, 9]
```

#### Notes:

- `tf.newaxis` is `None` as in NumPy.
- An implicit ellipsis is placed at the end of the `slice_spec`
- NumPy advanced indexing is currently not supported.



#### Args:


* <b>`tensor`</b>: An ops.Tensor object.
* <b>`slice_spec`</b>: The arguments to Tensor.__getitem__.
* <b>`var`</b>: In the case of variable slice assignment, the Variable object to slice
  (i.e. tensor is the read-only view of this variable).


#### Returns:

The appropriate slice of "tensor", based on "slice_spec".



#### Raises:


* <b>`ValueError`</b>: If a slice range is negative size.
* <b>`TypeError`</b>: If the slice indices aren't int, slice, ellipsis,
  tf.newaxis or scalar int32/int64 tensors.

<h3 id="__gt__"><code>__gt__</code></h3>

Defined in generated file: `python/ops/gen_math_ops.py`

``` python
__gt__(
    x,
    y,
    name=None
)
```

Returns the truth value of (x > y) element-wise.

*NOTE*: <a href="../tf/math/greater"><code>math.greater</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__invert__"><code>__invert__</code></h3>

Defined in generated file: `python/ops/gen_math_ops.py`

``` python
__invert__(
    x,
    name=None
)
```

Returns the truth value of NOT x element-wise.


#### Args:


* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L545-L558">View source</a>

``` python
__iter__()
```




<h3 id="__le__"><code>__le__</code></h3>

Defined in generated file: `python/ops/gen_math_ops.py`

``` python
__le__(
    x,
    y,
    name=None
)
```

Returns the truth value of (x <= y) element-wise.

*NOTE*: <a href="../tf/math/less_equal"><code>math.less_equal</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L738-L741">View source</a>

``` python
__len__()
```




<h3 id="__lt__"><code>__lt__</code></h3>

Defined in generated file: `python/ops/gen_math_ops.py`

``` python
__lt__(
    x,
    y,
    name=None
)
```

Returns the truth value of (x < y) element-wise.

*NOTE*: <a href="../tf/math/less"><code>math.less</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__matmul__"><code>__matmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__matmul__(
    x,
    y
)
```

Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

The inputs must, following any transpositions, be tensors of rank >= 2
where the inner 2 dimensions specify valid matrix multiplication arguments,
and any further outer dimensions match.

Both matrices must be of the same type. The supported types are:
`float16`, `float32`, `float64`, `int32`, `complex64`, `complex128`.

Either matrix can be transposed or adjointed (conjugated and transposed) on
the fly by setting one of the corresponding flag to `True`. These are `False`
by default.

If one or both of the matrices contain a lot of zeros, a more efficient
multiplication algorithm can be used by setting the corresponding
`a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default.
This optimization is only available for plain matrices (rank-2 tensors) with
datatypes `bfloat16` or `float32`.

#### For example:



```python
# 2-D tensor `a`
# [[1, 2, 3],
#  [4, 5, 6]]
a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# 2-D tensor `b`
# [[ 7,  8],
#  [ 9, 10],
#  [11, 12]]
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])

# `a` * `b`
# [[ 58,  64],
#  [139, 154]]
c = tf.matmul(a, b)


# 3-D tensor `a`
# [[[ 1,  2,  3],
#   [ 4,  5,  6]],
#  [[ 7,  8,  9],
#   [10, 11, 12]]]
a = tf.constant(np.arange(1, 13, dtype=np.int32),
                shape=[2, 2, 3])

# 3-D tensor `b`
# [[[13, 14],
#   [15, 16],
#   [17, 18]],
#  [[19, 20],
#   [21, 22],
#   [23, 24]]]
b = tf.constant(np.arange(13, 25, dtype=np.int32),
                shape=[2, 3, 2])

# `a` * `b`
# [[[ 94, 100],
#   [229, 244]],
#  [[508, 532],
#   [697, 730]]]
c = tf.matmul(a, b)

# Since python >= 3.5 the @ operator is supported (see PEP 465).
# In TensorFlow, it simply calls the `tf.matmul()` function, so the
# following lines are equivalent:
d = a @ b @ [[10.], [11.]]
d = tf.matmul(tf.matmul(a, b), [[10.], [11.]])
```

#### Args:


* <b>`a`</b>: `Tensor` of type `float16`, `float32`, `float64`, `int32`, `complex64`,
  `complex128` and rank > 1.
* <b>`b`</b>: `Tensor` with same type and rank as `a`.
* <b>`transpose_a`</b>: If `True`, `a` is transposed before multiplication.
* <b>`transpose_b`</b>: If `True`, `b` is transposed before multiplication.
* <b>`adjoint_a`</b>: If `True`, `a` is conjugated and transposed before
  multiplication.
* <b>`adjoint_b`</b>: If `True`, `b` is conjugated and transposed before
  multiplication.
* <b>`a_is_sparse`</b>: If `True`, `a` is treated as a sparse matrix.
* <b>`b_is_sparse`</b>: If `True`, `b` is treated as a sparse matrix.
* <b>`name`</b>: Name for the operation (optional).


#### Returns:

A `Tensor` of the same type as `a` and `b` where each inner-most matrix is
the product of the corresponding matrices in `a` and `b`, e.g. if all
transpose or adjoint attributes are `False`:

`output`[..., i, j] = sum_k (`a`[..., i, k] * `b`[..., k, j]),
for all indices i, j.


* <b>`Note`</b>: This is matrix product, not element-wise product.



#### Raises:


* <b>`ValueError`</b>: If transpose_a and adjoint_a, or transpose_b and adjoint_b
  are both set to True.

<h3 id="__mod__"><code>__mod__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__mod__(
    x,
    y
)
```

Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

true, this follows Python semantics in that the result here is consistent
with a flooring divide. E.g. `floor(x / y) * y + mod(x, y) = x`.

*NOTE*: <a href="../tf/math/floormod"><code>math.floormod</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__mul__"><code>__mul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__mul__(
    x,
    y
)
```

Dispatches cwise mul for "Dense*Dense" and "Dense*Sparse".


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L1342-L1351">View source</a>

``` python
__ne__(other)
```

Compares two tensors element-wise for equality.


<h3 id="__neg__"><code>__neg__</code></h3>

Defined in generated file: `python/ops/gen_math_ops.py`

``` python
__neg__(
    x,
    name=None
)
```

Computes numerical negative value element-wise.

I.e., \\(y = -x\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.negative(x.values, ...), x.dense_shape)`


<h3 id="__nonzero__"><code>__nonzero__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L767-L775">View source</a>

``` python
__nonzero__()
```

Dummy method to prevent a tensor from being used as a Python `bool`.

This is the Python 2.x counterpart to `__bool__()` above.

#### Raises:

`TypeError`.


<h3 id="__or__"><code>__or__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__or__(
    x,
    y
)
```

Returns the truth value of x OR y element-wise.

*NOTE*: <a href="../tf/math/logical_or"><code>math.logical_or</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`y`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__pow__"><code>__pow__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__pow__(
    x,
    y
)
```

Computes the power of one value to another.

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for
corresponding elements in `x` and `y`. For example:

```python
x = tf.constant([[2, 2], [3, 3]])
y = tf.constant([[8, 16], [2, 3]])
tf.pow(x, y)  # [[256, 65536], [9, 27]]
```

#### Args:


* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`y`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`.


<h3 id="__radd__"><code>__radd__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__radd__(
    y,
    x
)
```

Dispatches to add for strings and add_v2 for all other types.


<h3 id="__rand__"><code>__rand__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rand__(
    y,
    x
)
```

Returns the truth value of x AND y element-wise.

*NOTE*: <a href="../tf/math/logical_and"><code>math.logical_and</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`y`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__rdiv__"><code>__rdiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rdiv__(
    y,
    x
)
```

Divide two values using Python 2 semantics.

Used for Tensor.__div__.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` returns the quotient of x and y.


<h3 id="__rfloordiv__"><code>__rfloordiv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rfloordiv__(
    y,
    x
)
```

Divides `x / y` elementwise, rounding toward the most negative integer.

The same as <a href="../tf/div"><code>tf.compat.v1.div(x,y)</code></a> for integers, but uses
`tf.floor(tf.compat.v1.div(x,y))` for
floating point arguments so that the result is always an integer (though
possibly an integer represented as floating point).  This op is generated by
`x // y` floor division in Python 3 and in Python 2.7 with
`from __future__ import division`.

`x` and `y` must have the same type, and the result will have the same type
as well.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` rounded down.



#### Raises:


* <b>`TypeError`</b>: If the inputs are complex.

<h3 id="__rmatmul__"><code>__rmatmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rmatmul__(
    y,
    x
)
```

Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

The inputs must, following any transpositions, be tensors of rank >= 2
where the inner 2 dimensions specify valid matrix multiplication arguments,
and any further outer dimensions match.

Both matrices must be of the same type. The supported types are:
`float16`, `float32`, `float64`, `int32`, `complex64`, `complex128`.

Either matrix can be transposed or adjointed (conjugated and transposed) on
the fly by setting one of the corresponding flag to `True`. These are `False`
by default.

If one or both of the matrices contain a lot of zeros, a more efficient
multiplication algorithm can be used by setting the corresponding
`a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default.
This optimization is only available for plain matrices (rank-2 tensors) with
datatypes `bfloat16` or `float32`.

#### For example:



```python
# 2-D tensor `a`
# [[1, 2, 3],
#  [4, 5, 6]]
a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# 2-D tensor `b`
# [[ 7,  8],
#  [ 9, 10],
#  [11, 12]]
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])

# `a` * `b`
# [[ 58,  64],
#  [139, 154]]
c = tf.matmul(a, b)


# 3-D tensor `a`
# [[[ 1,  2,  3],
#   [ 4,  5,  6]],
#  [[ 7,  8,  9],
#   [10, 11, 12]]]
a = tf.constant(np.arange(1, 13, dtype=np.int32),
                shape=[2, 2, 3])

# 3-D tensor `b`
# [[[13, 14],
#   [15, 16],
#   [17, 18]],
#  [[19, 20],
#   [21, 22],
#   [23, 24]]]
b = tf.constant(np.arange(13, 25, dtype=np.int32),
                shape=[2, 3, 2])

# `a` * `b`
# [[[ 94, 100],
#   [229, 244]],
#  [[508, 532],
#   [697, 730]]]
c = tf.matmul(a, b)

# Since python >= 3.5 the @ operator is supported (see PEP 465).
# In TensorFlow, it simply calls the `tf.matmul()` function, so the
# following lines are equivalent:
d = a @ b @ [[10.], [11.]]
d = tf.matmul(tf.matmul(a, b), [[10.], [11.]])
```

#### Args:


* <b>`a`</b>: `Tensor` of type `float16`, `float32`, `float64`, `int32`, `complex64`,
  `complex128` and rank > 1.
* <b>`b`</b>: `Tensor` with same type and rank as `a`.
* <b>`transpose_a`</b>: If `True`, `a` is transposed before multiplication.
* <b>`transpose_b`</b>: If `True`, `b` is transposed before multiplication.
* <b>`adjoint_a`</b>: If `True`, `a` is conjugated and transposed before
  multiplication.
* <b>`adjoint_b`</b>: If `True`, `b` is conjugated and transposed before
  multiplication.
* <b>`a_is_sparse`</b>: If `True`, `a` is treated as a sparse matrix.
* <b>`b_is_sparse`</b>: If `True`, `b` is treated as a sparse matrix.
* <b>`name`</b>: Name for the operation (optional).


#### Returns:

A `Tensor` of the same type as `a` and `b` where each inner-most matrix is
the product of the corresponding matrices in `a` and `b`, e.g. if all
transpose or adjoint attributes are `False`:

`output`[..., i, j] = sum_k (`a`[..., i, k] * `b`[..., k, j]),
for all indices i, j.


* <b>`Note`</b>: This is matrix product, not element-wise product.



#### Raises:


* <b>`ValueError`</b>: If transpose_a and adjoint_a, or transpose_b and adjoint_b
  are both set to True.

<h3 id="__rmod__"><code>__rmod__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rmod__(
    y,
    x
)
```

Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

true, this follows Python semantics in that the result here is consistent
with a flooring divide. E.g. `floor(x / y) * y + mod(x, y) = x`.

*NOTE*: <a href="../tf/math/floormod"><code>math.floormod</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__rmul__"><code>__rmul__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rmul__(
    y,
    x
)
```

Dispatches cwise mul for "Dense*Dense" and "Dense*Sparse".


<h3 id="__ror__"><code>__ror__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__ror__(
    y,
    x
)
```

Returns the truth value of x OR y element-wise.

*NOTE*: <a href="../tf/math/logical_or"><code>math.logical_or</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`y`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


<h3 id="__rpow__"><code>__rpow__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rpow__(
    y,
    x
)
```

Computes the power of one value to another.

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for
corresponding elements in `x` and `y`. For example:

```python
x = tf.constant([[2, 2], [3, 3]])
y = tf.constant([[8, 16], [2, 3]])
tf.pow(x, y)  # [[256, 65536], [9, 27]]
```

#### Args:


* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`y`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`.


<h3 id="__rsub__"><code>__rsub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rsub__(
    y,
    x
)
```

Returns x - y element-wise.

*NOTE*: `Subtract` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__rtruediv__"><code>__rtruediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rtruediv__(
    y,
    x
)
```




<h3 id="__rxor__"><code>__rxor__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L922-L925">View source</a>

``` python
__rxor__(
    y,
    x
)
```

Logical XOR function.

x ^ y = (x | y) & ~(x & y)

Inputs are tensor and if the tensors contains more than one element, an
element-wise logical XOR is computed.

#### Usage:



```python
x = tf.constant([False, False, True, True], dtype = tf.bool)
y = tf.constant([False, True, False, True], dtype = tf.bool)
z = tf.logical_xor(x, y, name="LogicalXor")
#  here z = [False  True  True False]
```

#### Args:


* <b>`x`</b>: A `Tensor` type bool.
* <b>`y`</b>: A `Tensor` of type bool.


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.


<h3 id="__sub__"><code>__sub__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__sub__(
    x,
    y
)
```

Returns x - y element-wise.

*NOTE*: `Subtract` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__truediv__"><code>__truediv__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__truediv__(
    x,
    y
)
```




<h3 id="__xor__"><code>__xor__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L896-L912">View source</a>

``` python
__xor__(
    x,
    y
)
```

Logical XOR function.

x ^ y = (x | y) & ~(x & y)

Inputs are tensor and if the tensors contains more than one element, an
element-wise logical XOR is computed.

#### Usage:



```python
x = tf.constant([False, False, True, True], dtype = tf.bool)
y = tf.constant([False, True, False, True], dtype = tf.bool)
z = tf.logical_xor(x, y, name="LogicalXor")
#  here z = [False  True  True False]
```

#### Args:


* <b>`x`</b>: A `Tensor` type bool.
* <b>`y`</b>: A `Tensor` of type bool.


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.


<h3 id="consumers"><code>consumers</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L652-L664">View source</a>

``` python
consumers()
```

Returns a list of `Operation`s that consume this tensor.


#### Returns:

A list of `Operation`s.


<h3 id="eval"><code>eval</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L777-L798">View source</a>

``` python
eval(
    feed_dict=None,
    session=None
)
```

Evaluates this tensor in a `Session`.

Calling this method will execute all preceding operations that
produce the inputs needed for the operation that produces this
tensor.

*N.B.* Before invoking <a href="../tf/Tensor#eval"><code>Tensor.eval()</code></a>, its graph must have been
launched in a session, and either a default session must be
available, or `session` must be specified explicitly.

#### Args:


* <b>`feed_dict`</b>: A dictionary that maps `Tensor` objects to feed values. See
  <a href="../tf/Session#run"><code>tf.Session.run</code></a> for a description of the valid feed values.
* <b>`session`</b>: (Optional.) The `Session` to be used to evaluate this tensor. If
  none, the default session will be used.


#### Returns:

A numpy array corresponding to the value of this tensor.


<h3 id="experimental_ref"><code>experimental_ref</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L800-L851">View source</a>

``` python
experimental_ref()
```

Returns a hashable reference object to this Tensor.

Warning: Experimental API that could be changed or removed.

The primary usecase for this API is to put tensors in a set/dictionary.
We can't put tensors in a set/dictionary as `tensor.__hash__()` is no longer
available starting Tensorflow 2.0.

```python
import tensorflow as tf

x = tf.constant(5)
y = tf.constant(10)
z = tf.constant(10)

# The followings will raise an exception starting 2.0
# TypeError: Tensor is unhashable if Tensor equality is enabled.
tensor_set = {x, y, z}
tensor_dict = {x: 'five', y: 'ten', z: 'ten'}
```

Instead, we can use `tensor.experimental_ref()`.

```python
tensor_set = {x.experimental_ref(),
              y.experimental_ref(),
              z.experimental_ref()}

print(x.experimental_ref() in tensor_set)
==> True

tensor_dict = {x.experimental_ref(): 'five',
               y.experimental_ref(): 'ten',
               z.experimental_ref(): 'ten'}

print(tensor_dict[y.experimental_ref()])
==> ten
```

Also, the reference object provides `.deref()` function that returns the
original Tensor.

```python
x = tf.constant(5)
print(x.experimental_ref().deref())
==> tf.Tensor(5, shape=(), dtype=int32)
```

<h3 id="get_shape"><code>get_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L580-L582">View source</a>

``` python
get_shape()
```

Alias of Tensor.shape.


<h3 id="set_shape"><code>set_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L584-L645">View source</a>

``` python
set_shape(shape)
```

Updates the shape of this tensor.

This method can be called multiple times, and will merge the given
`shape` with the current shape of this tensor. It can be used to
provide additional information about the shape of this tensor that
cannot be inferred from the graph alone. For example, this can be used
to provide additional information about the shapes of images:

```python
_, image_data = tf.compat.v1.TFRecordReader(...).read(...)
image = tf.image.decode_png(image_data, channels=3)

# The height and width dimensions of `image` are data dependent, and
# cannot be computed without executing the op.
print(image.shape)
==> TensorShape([Dimension(None), Dimension(None), Dimension(3)])

# We know that each image in this dataset is 28 x 28 pixels.
image.set_shape([28, 28, 3])
print(image.shape)
==> TensorShape([Dimension(28), Dimension(28), Dimension(3)])
```

NOTE: This shape is not enforced at runtime. Setting incorrect shapes can
result in inconsistencies between the statically-known graph and the runtime
value of tensors. For runtime validation of the shape, use <a href="../tf/ensure_shape"><code>tf.ensure_shape</code></a>
instead.

#### Args:


* <b>`shape`</b>: A `TensorShape` representing the shape of this tensor, a
  `TensorShapeProto`, a list, a tuple, or None.


#### Raises:


* <b>`ValueError`</b>: If `shape` is not compatible with the current shape of
  this tensor.



## Class Members

* `OVERLOADABLE_OPERATORS` <a id="OVERLOADABLE_OPERATORS"></a>
