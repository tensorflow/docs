page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.RaggedTensor

## Class `RaggedTensor`

Represents a ragged tensor.



### Aliases:

* Class `tf.RaggedTensor`
* Class `tf.compat.v1.RaggedTensor`
* Class `tf.compat.v2.RaggedTensor`



Defined in [`python/ops/ragged/ragged_tensor.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ragged/ragged_tensor.py).

<!-- Placeholder for "Used in" -->

A `RaggedTensor` is a tensor with one or more *ragged dimensions*, which are
dimensions whose slices may have different lengths.  For example, the inner
(column) dimension of `rt=[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is ragged,
since the column slices (`rt[0, :]`, ..., `rt[4, :]`) have different lengths.
Dimensions whose slices all have the same length are called *uniform
dimensions*.  The outermost dimension of a `RaggedTensor` is always uniform,
since it consists of a single slice (and so there is no possibility for
differing slice lengths).

The total number of dimensions in a `RaggedTensor` is called its *rank*,
and the number of ragged dimensions in a `RaggedTensor` is called its
*ragged-rank*.  A `RaggedTensor`'s ragged-rank is fixed at graph creation
time: it can't depend on the runtime values of `Tensor`s, and can't vary
dynamically for different session runs.

### Potentially Ragged Tensors

Many ops support both `Tensor`s and `RaggedTensor`s.  The term "potentially
ragged tensor" may be used to refer to a tensor that might be either a
`Tensor` or a `RaggedTensor`.  The ragged-rank of a `Tensor` is zero.

### Documenting RaggedTensor Shapes

When documenting the shape of a RaggedTensor, ragged dimensions can be
indicated by enclosing them in parentheses.  For example, the shape of
a 3-D `RaggedTensor` that stores the fixed-size word embedding for each
word in a sentence, for each sentence in a batch, could be written as
`[num_sentences, (num_words), embedding_size]`.  The parentheses around
`(num_words)` indicate that dimension is ragged, and that the length
of each element list in that dimension may vary for each item.

### Component Tensors

Internally, a `RaggedTensor` consists of a concatenated list of values that
are partitioned into variable-length rows.  In particular, each `RaggedTensor`
consists of:

  * A `values` tensor, which concatenates the variable-length rows into a
    flattened list.  For example, the `values` tensor for
    `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is `[3, 1, 4, 1, 5, 9, 2, 6]`.

  * A `row_splits` vector, which indicates how those flattened values are
    divided into rows.  In particular, the values for row `rt[i]` are stored
    in the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.

#### Example:



```python
>>> print(tf.RaggedTensor.from_row_splits(
...     values=[3, 1, 4, 1, 5, 9, 2, 6],
...     row_splits=[0, 4, 4, 7, 8, 8]))
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>
```

### Alternative Row-Partitioning Schemes

In addition to `row_splits`, ragged tensors provide support for four other
row-partitioning schemes:

  * `row_lengths`: a vector with shape `[nrows]`, which specifies the length
    of each row.

  * `value_rowids` and `nrows`: `value_rowids` is a vector with shape
    `[nvals]`, corresponding one-to-one with `values`, which specifies
    each value's row index.  In particular, the row `rt[row]` consists of the
    values `rt.values[j]` where `value_rowids[j]==row`.  `nrows` is an
    integer scalar that specifies the number of rows in the
    `RaggedTensor`. (`nrows` is used to indicate trailing empty rows.)

  * `row_starts`: a vector with shape `[nrows]`, which specifies the start
    offset of each row.  Equivalent to `row_splits[:-1]`.

  * `row_limits`: a vector with shape `[nrows]`, which specifies the stop
    offset of each row.  Equivalent to `row_splits[1:]`.

Example: The following ragged tensors are equivalent, and all represent the
nested list `[[3, 1, 4, 1], [], [5, 9, 2], [6], []]`.

```python
>>> values = [3, 1, 4, 1, 5, 9, 2, 6]
>>> rt1 = RaggedTensor.from_row_splits(values, row_splits=[0, 4, 4, 7, 8, 8])
>>> rt2 = RaggedTensor.from_row_lengths(values, row_lengths=[4, 0, 3, 1, 0])
>>> rt3 = RaggedTensor.from_value_rowids(
...     values, value_rowids=[0, 0, 0, 0, 2, 2, 2, 3], nrows=5)
>>> rt4 = RaggedTensor.from_row_starts(values, row_starts=[0, 4, 4, 7, 8])
>>> rt5 = RaggedTensor.from_row_limits(values, row_limits=[4, 4, 7, 8, 8])
```

### Multiple Ragged Dimensions

`RaggedTensor`s with multiple ragged dimensions can be defined by using
a nested `RaggedTensor` for the `values` tensor.  Each nested `RaggedTensor`
adds a single ragged dimension.

```python
>>> inner_rt = RaggedTensor.from_row_splits(  # =rt1 from above
...     values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8, 8])
>>> outer_rt = RaggedTensor.from_row_splits(
...     values=inner_rt, row_splits=[0, 3, 3, 5])
>>> print outer_rt.to_list()
[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]
>>> print outer_rt.ragged_rank
2
```

The factory function <a href="../tf/RaggedTensor#from_nested_row_splits"><code>RaggedTensor.from_nested_row_splits</code></a> may be used to
construct a `RaggedTensor` with multiple ragged dimensions directly, by
providing a list of `row_splits` tensors:

```python
>>> RaggedTensor.from_nested_row_splits(
...     flat_values=[3, 1, 4, 1, 5, 9, 2, 6],
...     nested_row_splits=([0, 3, 3, 5], [0, 4, 4, 7, 8, 8])).to_list()
[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]
```

### Uniform Inner Dimensions

`RaggedTensor`s with uniform inner dimensions can be defined
by using a multidimensional `Tensor` for `values`.

```python
>>> rt = RaggedTensor.from_row_splits(values=tf.ones([5, 3]),
..                                    row_splits=[0, 2, 5])
>>> print rt.to_list()
[[[1, 1, 1], [1, 1, 1]],
 [[1, 1, 1], [1, 1, 1], [1, 1, 1]]]
 >>> print rt.shape
 (2, ?, 3)
```

### RaggedTensor Shape Restrictions

The shape of a RaggedTensor is currently restricted to have the following
form:

  * A single uniform dimension
  * Followed by one or more ragged dimensions
  * Followed by zero or more uniform dimensions.

This restriction follows from the fact that each nested `RaggedTensor`
replaces the uniform outermost dimension of its `values` with a uniform
dimension followed by a ragged dimension.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    values,
    row_splits,
    cached_row_lengths=None,
    cached_value_rowids=None,
    cached_nrows=None,
    internal=False
)
```

Creates a `RaggedTensor` with a specified partitioning for `values`.

This constructor is private -- please use one of the following ops to
build `RaggedTensor`s:

  * <a href="../tf/RaggedTensor#from_row_lengths"><code>tf.RaggedTensor.from_row_lengths</code></a>
  * <a href="../tf/RaggedTensor#from_value_rowids"><code>tf.RaggedTensor.from_value_rowids</code></a>
  * <a href="../tf/RaggedTensor#from_row_splits"><code>tf.RaggedTensor.from_row_splits</code></a>
  * <a href="../tf/RaggedTensor#from_row_starts"><code>tf.RaggedTensor.from_row_starts</code></a>
  * <a href="../tf/RaggedTensor#from_row_limits"><code>tf.RaggedTensor.from_row_limits</code></a>
  * <a href="../tf/RaggedTensor#from_nested_row_splits"><code>tf.RaggedTensor.from_nested_row_splits</code></a>
  * <a href="../tf/RaggedTensor#from_nested_row_lengths"><code>tf.RaggedTensor.from_nested_row_lengths</code></a>
  * <a href="../tf/RaggedTensor#from_nested_value_rowids"><code>tf.RaggedTensor.from_nested_value_rowids</code></a>

#### Args:


* <b>`values`</b>: A potentially ragged tensor of any dtype and shape `[nvals, ...]`.
* <b>`row_splits`</b>: A 1-D integer tensor with shape `[nrows+1]`.
* <b>`cached_row_lengths`</b>: A 1-D integer tensor with shape `[nrows]`
* <b>`cached_value_rowids`</b>: A 1-D integer tensor with shape `[nvals]`.
* <b>`cached_nrows`</b>: A 1-D integer scalar tensor.
* <b>`internal`</b>: True if the constructor is being called by one of the factory
  methods.  If false, an exception will be raised.


#### Raises:


* <b>`TypeError`</b>: If a row partitioning tensor has an inappropriate dtype.
* <b>`TypeError`</b>: If exactly one row partitioning argument was not specified.
* <b>`ValueError`</b>: If a row partitioning tensor has an inappropriate shape.
* <b>`ValueError`</b>: If multiple partitioning arguments are specified.
* <b>`ValueError`</b>: If nrows is specified but value_rowids is not None.



## Properties

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of values in this tensor.


<h3 id="flat_values"><code>flat_values</code></h3>

The innermost `values` tensor for this ragged tensor.

Concretely, if `rt.values` is a `Tensor`, then `rt.flat_values` is
`rt.values`; otherwise, `rt.flat_values` is `rt.values.flat_values`.

Conceptually, `flat_values` is the tensor formed by flattening the
outermost dimension and all of the ragged dimensions into a single
dimension.

`rt.flat_values.shape = [nvals] + rt.shape[rt.ragged_rank + 1:]`
(where `nvals` is the number of items in the flattened dimensions).

#### Returns:

A `Tensor`.


#### Example:

>     >>> rt = ragged.constant([[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]])
>     >>> print rt.flat_values()
>     tf.Tensor([3, 1, 4, 1, 5, 9, 2, 6])

<h3 id="nested_row_splits"><code>nested_row_splits</code></h3>

A tuple containing the row_splits for all ragged dimensions.

`rt.nested_row_splits` is a tuple containing the `row_splits` tensors for
all ragged dimensions in `rt`, ordered from outermost to innermost.  In
particular, `rt.nested_row_splits = (rt.row_splits,) + value_splits` where:

    * `value_splits = ()` if `rt.values` is a `Tensor`.
    * `value_splits = rt.values.nested_row_splits` otherwise.

#### Returns:

A `tuple` of 1-D integer `Tensor`s.


#### Example:

>     >>> rt = ragged.constant([[[[3, 1, 4, 1], [], [5, 9, 2]], [], [[6], []]]])
>     >>> for i, splits in enumerate(rt.nested_row_splits()):
>     ...   print('Splits for dimension %d: %s' % (i+1, splits))
>     Splits for dimension 1: [0, 1]
>     Splits for dimension 2: [0, 3, 3, 5]
>     Splits for dimension 3: [0, 4, 4, 7, 8, 8]

<h3 id="ragged_rank"><code>ragged_rank</code></h3>

The number of ragged dimensions in this ragged tensor.


#### Returns:

A Python `int` indicating the number of ragged dimensions in this ragged
tensor.  The outermost dimension is not considered ragged.


<h3 id="row_splits"><code>row_splits</code></h3>

The row-split indices for this ragged tensor's `values`.

`rt.row_splits` specifies where the values for each row begin and end in
`rt.values`.  In particular, the values for row `rt[i]` are stored in
the slice `rt.values[rt.row_splits[i]:rt.row_splits[i+1]]`.

#### Returns:

A 1-D integer `Tensor` with shape `[self.nrows+1]`.
The returned tensor is non-empty, and is sorted in ascending order.
`self.row_splits[0]` is zero, and `self.row_splits[-1]` is equal to
`self.values.shape[0]`.


#### Example:

>     >>> rt = ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>     >>> print rt.row_splits  # indices of row splits in rt.values
>     tf.Tensor([0, 4, 4, 7, 8, 8])

<h3 id="shape"><code>shape</code></h3>

The statically known shape of this ragged tensor.


#### Returns:

A `TensorShape` containing the statically known shape of this ragged
tensor.  Ragged dimensions have a size of `None`.



#### Examples:


```python
>>> ragged.constant([[0], [1, 2]]).shape
TensorShape([Dimension(2), Dimension(None)])

>>> ragged.constant([[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1).shape
TensorShape([Dimension(2), Dimension(None), Dimension(2)
```


<h3 id="values"><code>values</code></h3>

The concatenated rows for this ragged tensor.

`rt.values` is a potentially ragged tensor formed by flattening the two
outermost dimensions of `rt` into a single dimension.

`rt.values.shape = [nvals] + rt.shape[2:]` (where `nvals` is the
number of items in the outer two dimensions of `rt`).

`rt.ragged_rank = self.ragged_rank - 1`

#### Returns:

A potentially ragged tensor.


#### Example:

>     >>> rt = ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>     >>> print rt.values
>     tf.Tensor([3, 1, 4, 1, 5, 9, 2, 6])



## Methods

<h3 id="__abs__"><code>__abs__</code></h3>

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

``` python
__add__(
    x,
    y,
    name=None
)
```

Returns x + y element-wise.

*NOTE*: <a href="../tf/math/add"><code>math.add</code></a> supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__and__"><code>__and__</code></h3>

``` python
__and__(
    x,
    y,
    name=None
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

``` python
__bool__(_)
```

Dummy method to prevent a RaggedTensor from being used as a Python bool.


<h3 id="__div__"><code>__div__</code></h3>

``` python
__div__(
    x,
    y,
    name=None
)
```

Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Deprecated in favor of operator or tf.math.divide.

NOTE: Prefer using the Tensor division operator or tf.divide which obey Python
3 division operator semantics.

This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
and `y` are both integers then the result will be an integer. This is in
contrast to Python 3, where division with `/` is always a float while division
with `//` is always an integer.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` returns the quotient of x and y.


<h3 id="__floordiv__"><code>__floordiv__</code></h3>

``` python
__floordiv__(
    x,
    y,
    name=None
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

``` python
__getitem__(key)
```

Returns the specified piece of this RaggedTensor.

Supports multidimensional indexing and slicing, with one restriction:
indexing into a ragged inner dimension is not allowed.  This case is
problematic because the indicated value may exist in some rows but not
others.  In such cases, it's not obvious whether we should (1) report an
IndexError; (2) use a default value; or (3) skip that value and return a
tensor with fewer rows than we started with.  Following the guiding
principles of Python ("In the face of ambiguity, refuse the temptation to
guess"), we simply disallow this operation.

Any dimensions added by `array_ops.newaxis` will be ragged if the following
dimension is ragged.

#### Args:


* <b>`self`</b>: The RaggedTensor to slice.
* <b>`key`</b>: Indicates which piece of the RaggedTensor to return, using standard
  Python semantics (e.g., negative values index from the end).  `key`
  may have any of the following types:

  * `int` constant
  * Scalar integer `Tensor`
  * `slice` containing integer constants and/or scalar integer
    `Tensor`s
  * `Ellipsis`
  * `tf.newaxis`
  * `tuple` containing any of the above (for multidimentional indexing)


#### Returns:

A `Tensor` or `RaggedTensor` object.  Values that include at least one
ragged dimension are returned as `RaggedTensor`.  Values that include no
ragged dimensions are returned as `Tensor`.  See above for examples of
expressions that return `Tensor`s vs `RaggedTensor`s.



#### Raises:


* <b>`ValueError`</b>: If `key` is out of bounds.
* <b>`ValueError`</b>: If `key` is not supported.
* <b>`TypeError`</b>: If the indices in `key` have an unsupported type.


#### Examples:


```python
>>> # A 2-D ragged tensor with 1 ragged dimension.
>>> rt = ragged.constant([['a', 'b', 'c'], ['d', 'e'], ['f'], ['g']])
>>> rt[0].eval().tolist()       # First row (1-D `Tensor`)
['a', 'b', 'c']
>>> rt[:3].eval().tolist()      # First three rows (2-D RaggedTensor)
[['a', 'b', 'c'], ['d', 'e'], '[f'], [g']]
>>> rt[3, 0].eval().tolist()    # 1st element of 4th row (scalar)
'g'

>>> # A 3-D ragged tensor with 2 ragged dimensions.
>>> rt = ragged.constant([[[1, 2, 3], [4]],
...                    [[5], [], [6]],
...                    [[7]],
...                    [[8, 9], [10]]])
>>> rt[1].eval().tolist()       # Second row (2-D RaggedTensor)
[[5], [], [6]]
>>> rt[3, 0].eval().tolist()    # First element of fourth row (1-D Tensor)
[8, 9]
>>> rt[:, 1:3].eval().tolist()  # Items 1-3 of each row (3-D RaggedTensor)
[[[4]], [[], [6]], [], [[10]]]
>>> rt[:, -1:].eval().tolist()  # Last item of each row (3-D RaggedTensor)
[[[4]], [[6]], [[7]], [[10]]]
```


<h3 id="__gt__"><code>__gt__</code></h3>

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


<h3 id="__le__"><code>__le__</code></h3>

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


<h3 id="__lt__"><code>__lt__</code></h3>

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


<h3 id="__mod__"><code>__mod__</code></h3>

``` python
__mod__(
    x,
    y,
    name=None
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

``` python
__mul__(
    x,
    y,
    name=None
)
```

Returns x * y element-wise.

*NOTE*: `<a href="../tf/math/multiply"><code>tf.multiply</code></a>` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__neg__"><code>__neg__</code></h3>

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

``` python
__nonzero__(_)
```

Dummy method to prevent a RaggedTensor from being used as a Python bool.


<h3 id="__or__"><code>__or__</code></h3>

``` python
__or__(
    x,
    y,
    name=None
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

``` python
__pow__(
    x,
    y,
    name=None
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

``` python
__radd__(
    x,
    y,
    name=None
)
```

Returns x + y element-wise.

*NOTE*: <a href="../tf/math/add"><code>math.add</code></a> supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__rand__"><code>__rand__</code></h3>

``` python
__rand__(
    x,
    y,
    name=None
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

``` python
__rdiv__(
    x,
    y,
    name=None
)
```

Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Deprecated in favor of operator or tf.math.divide.

NOTE: Prefer using the Tensor division operator or tf.divide which obey Python
3 division operator semantics.

This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
and `y` are both integers then the result will be an integer. This is in
contrast to Python 3, where division with `/` is always a float while division
with `//` is always an integer.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` returns the quotient of x and y.


<h3 id="__rfloordiv__"><code>__rfloordiv__</code></h3>

``` python
__rfloordiv__(
    x,
    y,
    name=None
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

<h3 id="__rmod__"><code>__rmod__</code></h3>

``` python
__rmod__(
    x,
    y,
    name=None
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

``` python
__rmul__(
    x,
    y,
    name=None
)
```

Returns x * y element-wise.

*NOTE*: `<a href="../tf/math/multiply"><code>tf.multiply</code></a>` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.


<h3 id="__ror__"><code>__ror__</code></h3>

``` python
__ror__(
    x,
    y,
    name=None
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

``` python
__rpow__(
    x,
    y,
    name=None
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

``` python
__rsub__(
    x,
    y,
    name=None
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

``` python
__rtruediv__(
    x,
    y,
    name=None
)
```

Divides x / y elementwise (using Python 3 division operator semantics).

NOTE: Prefer using the Tensor operator or tf.divide which obey Python
division operator semantics.

This function forces Python 3 division operator semantics where all integer
arguments are cast to floating types first.   This op is generated by normal
`x / y` division in Python 3 and in Python 2.7 with
`from __future__ import division`.  If you want integer division that rounds
down, use `x // y` or `tf.math.floordiv`.

`x` and `y` must have the same numeric type.  If the inputs are floating
point, the output will have the same type.  If the inputs are integral, the
inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32`
and `int64` (matching the behavior of Numpy).

#### Args:


* <b>`x`</b>: `Tensor` numerator of numeric type.
* <b>`y`</b>: `Tensor` denominator of numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` evaluated in floating point.



#### Raises:


* <b>`TypeError`</b>: If `x` and `y` have different dtypes.

<h3 id="__rxor__"><code>__rxor__</code></h3>

``` python
__rxor__(
    x,
    y,
    name='LogicalXor'
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

``` python
__sub__(
    x,
    y,
    name=None
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

``` python
__truediv__(
    x,
    y,
    name=None
)
```

Divides x / y elementwise (using Python 3 division operator semantics).

NOTE: Prefer using the Tensor operator or tf.divide which obey Python
division operator semantics.

This function forces Python 3 division operator semantics where all integer
arguments are cast to floating types first.   This op is generated by normal
`x / y` division in Python 3 and in Python 2.7 with
`from __future__ import division`.  If you want integer division that rounds
down, use `x // y` or `tf.math.floordiv`.

`x` and `y` must have the same numeric type.  If the inputs are floating
point, the output will have the same type.  If the inputs are integral, the
inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32`
and `int64` (matching the behavior of Numpy).

#### Args:


* <b>`x`</b>: `Tensor` numerator of numeric type.
* <b>`y`</b>: `Tensor` denominator of numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` evaluated in floating point.



#### Raises:


* <b>`TypeError`</b>: If `x` and `y` have different dtypes.

<h3 id="__xor__"><code>__xor__</code></h3>

``` python
__xor__(
    x,
    y,
    name='LogicalXor'
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


<h3 id="bounding_shape"><code>bounding_shape</code></h3>

``` python
bounding_shape(
    axis=None,
    name=None,
    out_type=None
)
```

Returns the tight bounding box shape for this `RaggedTensor`.


#### Args:


* <b>`axis`</b>: An integer scalar or vector indicating which axes to return the
  bounding box for.  If not specified, then the full bounding box is
  returned.
* <b>`name`</b>: A name prefix for the returned tensor (optional).
* <b>`out_type`</b>: `dtype` for the returned tensor.  Defaults to
  `self.row_splits.dtype`.


#### Returns:

An integer `Tensor` (`dtype=self.row_splits.dtype`).  If `axis` is not
specified, then `output` is a vector with
`output.shape=[self.shape.ndims]`.  If `axis` is a scalar, then the
`output` is a scalar.  If `axis` is a vector, then `output` is a vector,
where `output[i]` is the bounding size for dimension `axis[i]`.


#### Example:

>     >>> rt = ragged.constant([[1, 2, 3, 4], [5], [], [6, 7, 8, 9], [10]])
>     >>> rt.bounding_shape()
>     [5, 4]

<h3 id="consumers"><code>consumers</code></h3>

``` python
consumers()
```




<h3 id="from_nested_row_lengths"><code>from_nested_row_lengths</code></h3>

``` python
@classmethod
from_nested_row_lengths(
    cls,
    flat_values,
    nested_row_lengths,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` from a nested list of `row_lengths` tensors.


#### Equivalent to:



```python
result = flat_values
for row_lengths in reversed(nested_row_lengths):
  result = from_row_lengths(result, row_lengths)
```

#### Args:


* <b>`flat_values`</b>: A potentially ragged tensor.
* <b>`nested_row_lengths`</b>: A list of 1-D integer tensors.  The `i`th tensor is
  used as the `row_lengths` for the `i`th ragged dimension.
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form
  a valid `RaggedTensor`.


#### Returns:

A `RaggedTensor` (or `flat_values` if `nested_row_lengths` is empty).


<h3 id="from_nested_row_splits"><code>from_nested_row_splits</code></h3>

``` python
@classmethod
from_nested_row_splits(
    cls,
    flat_values,
    nested_row_splits,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` from a nested list of `row_splits` tensors.


#### Equivalent to:



```python
result = flat_values
for row_splits in reversed(nested_row_splits):
  result = from_row_splits(result, row_splits)
```

#### Args:


* <b>`flat_values`</b>: A potentially ragged tensor.
* <b>`nested_row_splits`</b>: A list of 1-D integer tensors.  The `i`th tensor is
  used as the `row_splits` for the `i`th ragged dimension.
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form a
  valid `RaggedTensor`.


#### Returns:

A `RaggedTensor` (or `flat_values` if `nested_row_splits` is empty).


<h3 id="from_nested_value_rowids"><code>from_nested_value_rowids</code></h3>

``` python
@classmethod
from_nested_value_rowids(
    cls,
    flat_values,
    nested_value_rowids,
    nested_nrows=None,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` from a nested list of `value_rowids` tensors.


#### Equivalent to:



```python
result = flat_values
for (rowids, nrows) in reversed(zip(nested_value_rowids, nested_nrows)):
  result = from_value_rowids(result, rowids, nrows)
```

#### Args:


* <b>`flat_values`</b>: A potentially ragged tensor.
* <b>`nested_value_rowids`</b>: A list of 1-D integer tensors.  The `i`th tensor is
  used as the `value_rowids` for the `i`th ragged dimension.
* <b>`nested_nrows`</b>: A list of integer scalars.  The `i`th scalar is used as the
  `nrows` for the `i`th ragged dimension.
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form
  a valid `RaggedTensor`.


#### Returns:

A `RaggedTensor` (or `flat_values` if `nested_value_rowids` is empty).



#### Raises:


* <b>`ValueError`</b>: If `len(nested_values_rowids) != len(nested_nrows)`.

<h3 id="from_row_lengths"><code>from_row_lengths</code></h3>

``` python
@classmethod
from_row_lengths(
    cls,
    values,
    row_lengths,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` with rows partitioned by `row_lengths`.

The returned `RaggedTensor` corresponds with the python list defined by:

```python
result = [[values.pop(0) for i in range(length)]
          for length in row_lengths]
```

#### Args:


* <b>`values`</b>: A potentially ragged tensor with shape `[nvals, ...]`.
* <b>`row_lengths`</b>: A 1-D integer tensor with shape `[nrows]`.  Must be
  nonnegative.  `sum(row_lengths)` must be `nvals`.
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form
  a valid `RaggedTensor`.


#### Returns:

A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.


#### Example:

>     >>> print(tf.RaggedTensor.from_row_lengths(
>     ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
>     ...     row_lengths=[4, 0, 3, 1, 0]))
>     <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []])>

<h3 id="from_row_limits"><code>from_row_limits</code></h3>

``` python
@classmethod
from_row_limits(
    cls,
    values,
    row_limits,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` with rows partitioned by `row_limits`.

Equivalent to: `from_row_splits(values, concat([0, row_limits]))`.

#### Args:


* <b>`values`</b>: A potentially ragged tensor with shape `[nvals, ...]`.
* <b>`row_limits`</b>: A 1-D integer tensor with shape `[nrows]`.  Must be sorted in
  ascending order.  If `nrows>0`, then `row_limits[-1]` must be `nvals`.
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form
  a valid `RaggedTensor`.


#### Returns:

A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.


#### Example:

>     >>> print(tf.RaggedTensor.from_row_limits(
>     ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
>     ...     row_limits=[4, 4, 7, 8, 8]))
>     <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

<h3 id="from_row_splits"><code>from_row_splits</code></h3>

``` python
@classmethod
from_row_splits(
    cls,
    values,
    row_splits,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` with rows partitioned by `row_splits`.

The returned `RaggedTensor` corresponds with the python list defined by:

```python
result = [values[row_splits[i]:row_splits[i + 1]]
          for i in range(len(row_splits) - 1)]
```

#### Args:


* <b>`values`</b>: A potentially ragged tensor with shape `[nvals, ...]`.
* <b>`row_splits`</b>: A 1-D integer tensor with shape `[nrows+1]`.  Must not be
  empty, and must be sorted in ascending order.  `row_splits[0]` must be
  zero and `row_splits[-1]` must be `nvals`.
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form
  a valid `RaggedTensor`.


#### Returns:

A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.



#### Raises:


* <b>`ValueError`</b>: If `row_splits` is an empty list.

#### Example:

>     >>> print(tf.RaggedTensor.from_row_splits(
>     ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
>     ...     row_splits=[0, 4, 4, 7, 8, 8]))
>     <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

<h3 id="from_row_starts"><code>from_row_starts</code></h3>

``` python
@classmethod
from_row_starts(
    cls,
    values,
    row_starts,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` with rows partitioned by `row_starts`.

Equivalent to: `from_row_splits(values, concat([row_starts, nvals]))`.

#### Args:


* <b>`values`</b>: A potentially ragged tensor with shape `[nvals, ...]`.
* <b>`row_starts`</b>: A 1-D integer tensor with shape `[nrows]`.  Must be
  nonnegative and sorted in ascending order.  If `nrows>0`, then
  `row_starts[0]` must be zero.
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form
  a valid `RaggedTensor`.


#### Returns:

A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.


#### Example:

>     >>> print(tf.RaggedTensor.from_row_starts(
>     ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
>     ...     row_starts=[0, 4, 4, 7, 8]))
>     <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

<h3 id="from_sparse"><code>from_sparse</code></h3>

``` python
@classmethod
from_sparse(
    cls,
    st_input,
    name=None,
    row_splits_dtype=tf.dtypes.int64
)
```

Converts a 2D <a href="../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a> to a `RaggedTensor`.

Each row of the `output` `RaggedTensor` will contain the explicit values
from the same row in `st_input`.  `st_input` must be ragged-right.  If not
it is not ragged-right, then an error will be generated.

#### Example:



```python
>>> st = SparseTensor(indices=[[0, 1], [0, 2], [0, 3], [1, 0], [3, 0]],
...                   values=[1, 2, 3, 4, 5],
...                   dense_shape=[4, 3])
>>> rt.RaggedTensor.from_sparse(st).eval().tolist()
[[1, 2, 3], [4], [], [5]]
```

Currently, only two-dimensional `SparseTensors` are supported.

#### Args:


* <b>`st_input`</b>: The sparse tensor to convert.  Must have rank 2.
* <b>`name`</b>: A name prefix for the returned tensors (optional).
* <b>`row_splits_dtype`</b>: `dtype` for the returned `RaggedTensor`'s `row_splits`
  tensor.  One of <a href="../tf#int32"><code>tf.int32</code></a> or <a href="../tf#int64"><code>tf.int64</code></a>.


#### Returns:

A `RaggedTensor` with the same values as `st_input`.
`output.ragged_rank = rank(st_input) - 1`.
`output.shape = [st_input.dense_shape[0], None]`.


#### Raises:


* <b>`ValueError`</b>: If the number of dimensions in `st_input` is not known
  statically, or is not two.

<h3 id="from_tensor"><code>from_tensor</code></h3>

``` python
@classmethod
from_tensor(
    cls,
    tensor,
    lengths=None,
    padding=None,
    ragged_rank=1,
    name=None,
    row_splits_dtype=tf.dtypes.int64
)
```

Converts a <a href="../tf/Tensor"><code>tf.Tensor</code></a> into a `RaggedTensor`.

The set of absent/default values may be specified using a vector of lengths
or a padding value (but not both).  If `lengths` is specified, then the
output tensor will satisfy `output[row] = tensor[row][:lengths[row]]`. If
'lengths' is a list of lists or tuple of lists, those lists will be used
as nested row lengths. If `padding` is specified, then any row *suffix*
consisting entirely of `padding` will be excluded from the returned
`RaggedTensor`.  If neither `lengths` nor `padding` is specified, then the
returned `RaggedTensor` will have no absent/default values.

#### Examples:



```python
>>> dt = tf.constant([[5, 7, 0], [0, 3, 0], [6, 0, 0]])
>>> tf.RaggedTensor.from_tensor(dt)
<tf.RaggedTensor [[5, 7, 0], [0, 3, 0], [6, 0, 0]]>
>>> tf.RaggedTensor.from_tensor(dt, lengths=[1, 0, 3])
<tf.RaggedTensor [[5], [], [6, 0, 0]]>

>>> tf.RaggedTensor.from_tensor(dt, padding=0)
<tf.RaggedTensor [[5, 7], [0, 3], [6]]>

>>> dt = tf.constant([[[5, 0], [7, 0], [0, 0]],
                      [[0, 0], [3, 0], [0, 0]],
                      [[6, 0], [0, 0], [0, 0]]])
>>> tf.RaggedTensor.from_tensor(dt, lengths=([2, 0, 3], [1, 1, 2, 0, 1]))
<tf.RaggedTensor [[[5], [7]], [], [[6, 0], [], [0]]]>
```

#### Args:


* <b>`tensor`</b>: The `Tensor` to convert.  Must have rank `ragged_rank + 1` or
  higher.
* <b>`lengths`</b>: An optional set of row lengths, specified using a 1-D integer
  `Tensor` whose length is equal to `tensor.shape[0]` (the number of rows
  in `tensor`).  If specified, then `output[row]` will contain
  `tensor[row][:lengths[row]]`.  Negative lengths are treated as zero. You
  may optionally pass a list or tuple of lengths to this argument, which
  will be used as nested row lengths to construct a ragged tensor with
  multiple ragged dimensions.
* <b>`padding`</b>: An optional padding value.  If specified, then any row suffix
  consisting entirely of `padding` will be excluded from the returned
  RaggedTensor.  `padding` is a `Tensor` with the same dtype as `tensor`
  and with `shape=tensor.shape[ragged_rank + 1:]`.
* <b>`ragged_rank`</b>: Integer specifying the ragged rank for the returned
  `RaggedTensor`.  Must be greater than zero.
* <b>`name`</b>: A name prefix for the returned tensors (optional).
* <b>`row_splits_dtype`</b>: `dtype` for the returned `RaggedTensor`'s `row_splits`
  tensor.  One of <a href="../tf#int32"><code>tf.int32</code></a> or <a href="../tf#int64"><code>tf.int64</code></a>.


#### Returns:

A `RaggedTensor` with the specified `ragged_rank`.  The shape of the
returned ragged tensor is compatible with the shape of `tensor`.


#### Raises:


* <b>`ValueError`</b>: If both `lengths` and `padding` are specified.

<h3 id="from_value_rowids"><code>from_value_rowids</code></h3>

``` python
@classmethod
from_value_rowids(
    cls,
    values,
    value_rowids,
    nrows=None,
    name=None,
    validate=True
)
```

Creates a `RaggedTensor` with rows partitioned by `value_rowids`.

The returned `RaggedTensor` corresponds with the python list defined by:

```python
result = [[values[i] for i in range(len(values)) if value_rowids[i] == row]
          for row in range(nrows)]
```

#### Args:


* <b>`values`</b>: A potentially ragged tensor with shape `[nvals, ...]`.
* <b>`value_rowids`</b>: A 1-D integer tensor with shape `[nvals]`, which corresponds
  one-to-one with `values`, and specifies each value's row index.  Must be
  nonnegative, and must be sorted in ascending order.
* <b>`nrows`</b>: An integer scalar specifying the number of rows.  This should be
  specified if the `RaggedTensor` may containing empty training rows. Must
  be greater than `value_rowids[-1]` (or zero if `value_rowids` is empty).
  Defaults to `value_rowids[-1]` (or zero if `value_rowids` is empty).
* <b>`name`</b>: A name prefix for the RaggedTensor (optional).
* <b>`validate`</b>: If true, then use assertions to check that the arguments form
  a valid `RaggedTensor`.


#### Returns:

A `RaggedTensor`.  `result.rank = values.rank + 1`.
`result.ragged_rank = values.ragged_rank + 1`.



#### Raises:


* <b>`ValueError`</b>: If `nrows` is incompatible with `value_rowids`.

#### Example:

>     >>> print(tf.RaggedTensor.from_value_rowids(
>     ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
>     ...     value_rowids=[0, 0, 0, 0, 2, 2, 2, 3],
>     ...     nrows=5))
>     <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

<h3 id="nested_row_lengths"><code>nested_row_lengths</code></h3>

``` python
nested_row_lengths(name=None)
```

Returns a tuple containing the row_lengths for all ragged dimensions.

`rtnested_row_lengths()` is a tuple containing the `row_lengths` tensors for
all ragged dimensions in `rt`, ordered from outermost to innermost.

#### Args:


* <b>`name`</b>: A name prefix for the returned tensors (optional).


#### Returns:

A `tuple` of 1-D integer `Tensors`.  The length of the tuple is equal to
`self.ragged_rank`.


<h3 id="nrows"><code>nrows</code></h3>

``` python
nrows(
    out_type=None,
    name=None
)
```

Returns the number of rows in this ragged tensor.

I.e., the size of the outermost dimension of the tensor.

#### Args:


* <b>`out_type`</b>: `dtype` for the returned tensor.  Defaults to
  `self.row_splits.dtype`.
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A scalar `Tensor` with dtype `out_type`.


#### Example:

>     >>> rt = ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>     >>> rt.nrows()  # rt has 5 rows.
>     5

<h3 id="row_lengths"><code>row_lengths</code></h3>

``` python
row_lengths(
    axis=1,
    name=None
)
```

Returns the lengths of the rows in this ragged tensor.

`rt.row_lengths()[i]` indicates the number of values in the
`i`th row of `rt`.

#### Args:


* <b>`axis`</b>: An integer constant indicating the axis whose row lengths should be
  returned.
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A potentially ragged integer Tensor with shape `self.shape[:axis]`.



#### Raises:


* <b>`ValueError`</b>: If `axis` is out of bounds.

#### Example:

>     >>> rt = ragged.constant([[[3, 1, 4], [1]], [], [[5, 9], [2]], [[6]], []])
>     >>> rt.row_lengths(rt)  # lengths of rows in rt
>     tf.Tensor([2, 0, 2, 1, 0])
>     >>> rt.row_lengths(axis=2)  # lengths of axis=2 rows.
>     <tf.RaggedTensor [[3, 1], [], [2, 1], [1], []]>

<h3 id="row_limits"><code>row_limits</code></h3>

``` python
row_limits(name=None)
```

Returns the limit indices for rows in this ragged tensor.

These indices specify where the values for each row end in
`self.values`.  `rt.row_limits(self)` is equal to `rt.row_splits[:-1]`.

#### Args:


* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A 1-D integer Tensor with shape `[nrows]`.
The returned tensor is nonnegative, and is sorted in ascending order.


#### Example:

>     >>> rt = ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>     >>> rt.values
>     tf.Tensor([3, 1, 4, 1, 5, 9, 2, 6])
>     >>> rt.row_limits()  # indices of row limits in rt.values
>     tf.Tensor([4, 4, 7, 8, 8])

<h3 id="row_starts"><code>row_starts</code></h3>

``` python
row_starts(name=None)
```

Returns the start indices for rows in this ragged tensor.

These indices specify where the values for each row begin in
`self.values`.  `rt.row_starts()` is equal to `rt.row_splits[:-1]`.

#### Args:


* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A 1-D integer Tensor with shape `[nrows]`.
The returned tensor is nonnegative, and is sorted in ascending order.


#### Example:

>     >>> rt = ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>     >>> rt.values
>     tf.Tensor([3, 1, 4, 1, 5, 9, 2, 6])
>     >>> rt.row_starts()  # indices of row starts in rt.values
>     tf.Tensor([0, 4, 4, 7, 8])

<h3 id="to_list"><code>to_list</code></h3>

``` python
to_list()
```

Returns a nested Python `list` with the values for this `RaggedTensor`.

Requires that `rt` was constructed in eager execution mode.

#### Returns:

A nested Python `list`.


<h3 id="to_sparse"><code>to_sparse</code></h3>

``` python
to_sparse(name=None)
```

Converts this `RaggedTensor` into a <a href="../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a>.


#### Example:



```python
>>> rt = ragged.constant([[1, 2, 3], [4], [], [5, 6]])
>>> rt.to_sparse().eval()
SparseTensorValue(indices=[[0, 0], [0, 1], [0, 2], [1, 0], [3, 0], [3, 1]],
                  values=[1, 2, 3, 4, 5, 6],
                  dense_shape=[4, 3])
```

#### Args:


* <b>`name`</b>: A name prefix for the returned tensors (optional).


#### Returns:

A SparseTensor with the same values as `self`.


<h3 id="to_tensor"><code>to_tensor</code></h3>

``` python
to_tensor(
    default_value=None,
    name=None
)
```

Converts this `RaggedTensor` into a <a href="../tf/Tensor"><code>tf.Tensor</code></a>.


#### Example:



```python
>>> rt = ragged.constant([[9, 8, 7], [], [6, 5], [4]])
>>> print rt.to_tensor()
[[9 8 7]
 [0 0 0]
 [6 5 0]
 [4 0 0]]
```

#### Args:


* <b>`default_value`</b>: Value to set for indices not specified in `self`. Defaults
  to zero.  `default_value` must be broadcastable to
  `self.shape[self.ragged_rank + 1:]`.
* <b>`name`</b>: A name prefix for the returned tensors (optional).


#### Returns:

A `Tensor` with shape `ragged.bounding_shape(self)` and the
values specified by the non-empty values in `self`.  Empty values are
assigned `default_value`.


<h3 id="value_rowids"><code>value_rowids</code></h3>

``` python
value_rowids(name=None)
```

Returns the row indices for the `values` in this ragged tensor.

`rt.value_rowids()` corresponds one-to-one with the outermost dimension of
`rt.values`, and specifies the row containing each value.  In particular,
the row `rt[row]` consists of the values `rt.values[j]` where
`rt.value_rowids()[j] == row`.

#### Args:


* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A 1-D integer `Tensor` with shape `self.values.shape[:1]`.
The returned tensor is nonnegative, and is sorted in ascending order.


#### Example:

>     >>> rt = ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
>     >>> rt.values
>     tf.Tensor([3, 1, 4, 1, 5, 9, 2, 6])
>     >>> rt.value_rowids()
>     tf.Tensor([0, 0, 0, 0, 2, 2, 2, 3])  # corresponds 1:1 with rt.values

<h3 id="with_flat_values"><code>with_flat_values</code></h3>

``` python
with_flat_values(new_values)
```

Returns a copy of `self` with `flat_values` replaced by `new_value`.

Preserves cached row-partitioning tensors such as `self.cached_nrows` and
`self.cached_value_rowids` if they have values.

#### Args:


* <b>`new_values`</b>: Potentially ragged tensor that should replace
`self.flat_values`.  Must have `rank > 0`, and must have the same
number of rows as `self.flat_values`.


#### Returns:

A `RaggedTensor`.
`result.rank = self.ragged_rank + new_values.rank`.
`result.ragged_rank = self.ragged_rank + new_values.ragged_rank`.


<h3 id="with_row_splits_dtype"><code>with_row_splits_dtype</code></h3>

``` python
with_row_splits_dtype(dtype)
```

Returns a copy of this RaggedTensor with the given `row_splits` dtype.

For RaggedTensors with multiple ragged dimensions, the `row_splits` for all
nested `RaggedTensor` objects are cast to the given dtype.

#### Args:


* <b>`dtype`</b>: The dtype for `row_splits`.  One of <a href="../tf#int32"><code>tf.int32</code></a> or <a href="../tf#int64"><code>tf.int64</code></a>.


#### Returns:

A copy of this RaggedTensor, with the `row_splits` cast to the given
type.


<h3 id="with_values"><code>with_values</code></h3>

``` python
with_values(new_values)
```

Returns a copy of `self` with `values` replaced by `new_value`.

Preserves cached row-partitioning tensors such as `self.cached_nrows` and
`self.cached_value_rowids` if they have values.

#### Args:


* <b>`new_values`</b>: Potentially ragged tensor to use as the `values` for the
  returned `RaggedTensor`.  Must have `rank > 0`, and must have the same
  number of rows as `self.values`.


#### Returns:

A `RaggedTensor`.  `result.rank = 1 + new_values.rank`.
`result.ragged_rank = 1 + new_values.ragged_rank`




