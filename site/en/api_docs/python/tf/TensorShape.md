page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.TensorShape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/TensorShape">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L722-L1208">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TensorShape`

Represents the shape of a `Tensor`.



### Aliases:

* Class <a href="/api_docs/python/tf/TensorShape"><code>tf.compat.v1.TensorShape</code></a>
* Class <a href="/api_docs/python/tf/TensorShape"><code>tf.compat.v2.TensorShape</code></a>


<!-- Placeholder for "Used in" -->

A `TensorShape` represents a possibly-partial shape specification for a
`Tensor`. It may be one of the following:

* *Fully-known shape:* has a known number of dimensions and a known size
  for each dimension. e.g. `TensorShape([16, 256])`
* *Partially-known shape:* has a known number of dimensions, and an unknown
  size for one or more dimension. e.g. `TensorShape([None, 256])`
* *Unknown shape:* has an unknown number of dimensions, and an unknown
  size in all dimensions. e.g. `TensorShape(None)`

If a tensor is produced by an operation of type `"Foo"`, its shape
may be inferred if there is a registered shape function for
`"Foo"`. See [Shape
functions](https://tensorflow.org/extend/adding_an_op#shape_functions_in_c)
for details of shape functions and how to register them. Alternatively,
the shape may be set explicitly using <a href="../tf/Tensor#set_shape"><code>tf.Tensor.set_shape</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L743-L776">View source</a>

``` python
__init__(dims)
```

Creates a new TensorShape with the given dimensions.


#### Args:


* <b>`dims`</b>: A list of Dimensions, or None if the shape is unspecified.


#### Raises:


* <b>`TypeError`</b>: If dims cannot be converted to a list of dimensions.



## Properties

<h3 id="dims"><code>dims</code></h3>

Returns a list of Dimensions, or None if the shape is unspecified.


<h3 id="ndims"><code>ndims</code></h3>

Deprecated accessor for `rank`.


<h3 id="rank"><code>rank</code></h3>

Returns the rank of this shape, or None if it is unspecified.




## Methods

<h3 id="__add__"><code>__add__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L936-L939">View source</a>

``` python
__add__(other)
```




<h3 id="__bool__"><code>__bool__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L830-L832">View source</a>

``` python
__bool__()
```

Returns True if this shape contains non-zero information.


<h3 id="__concat__"><code>__concat__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1207-L1208">View source</a>

``` python
__concat__(other)
```




<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1184-L1190">View source</a>

``` python
__eq__(other)
```

Returns True if `self` is equivalent to `other`.


<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L847-L895">View source</a>

``` python
__getitem__(key)
```

Returns the value of a dimension or a shape, depending on the key.


#### Args:


* <b>`key`</b>: If `key` is an integer, returns the dimension at that index;
  otherwise if `key` is a slice, returns a TensorShape whose dimensions
  are those selected by the slice from `self`.


#### Returns:

An integer if `key` is an integer, or a `TensorShape` if `key` is a
slice.



#### Raises:


* <b>`ValueError`</b>: If `key` is a slice and `self` is completely unknown and
  the step is set.

<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L837-L845">View source</a>

``` python
__iter__()
```

Returns `self.dims` if the rank is known, otherwise raises ValueError.


<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L824-L828">View source</a>

``` python
__len__()
```

Returns the rank of this shape, or raises ValueError if unspecified.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1192-L1202">View source</a>

``` python
__ne__(other)
```

Returns True if `self` is known to be different from `other`.


<h3 id="__nonzero__"><code>__nonzero__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L830-L832">View source</a>

``` python
__nonzero__()
```

Returns True if this shape contains non-zero information.


<h3 id="__radd__"><code>__radd__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L941-L944">View source</a>

``` python
__radd__(other)
```




<h3 id="as_list"><code>as_list</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1161-L1172">View source</a>

``` python
as_list()
```

Returns a list of integers or `None` for each dimension.


#### Returns:

A list of integers or `None` for each dimension.



#### Raises:


* <b>`ValueError`</b>: If `self` is an unknown shape with an unknown rank.

<h3 id="as_proto"><code>as_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1174-L1182">View source</a>

``` python
as_proto()
```

Returns this shape as a `TensorShapeProto`.


<h3 id="assert_has_rank"><code>assert_has_rank</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L985-L995">View source</a>

``` python
assert_has_rank(rank)
```

Raises an exception if `self` is not compatible with the given `rank`.


#### Args:


* <b>`rank`</b>: An integer.


#### Raises:


* <b>`ValueError`</b>: If `self` does not represent a shape with the given `rank`.

<h3 id="assert_is_compatible_with"><code>assert_is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1102-L1115">View source</a>

``` python
assert_is_compatible_with(other)
```

Raises exception if `self` and `other` do not represent the same shape.

This method can be used to assert that there exists a shape that both
`self` and `other` represent.

#### Args:


* <b>`other`</b>: Another TensorShape.


#### Raises:


* <b>`ValueError`</b>: If `self` and `other` do not represent the same shape.

<h3 id="assert_is_fully_defined"><code>assert_is_fully_defined</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1152-L1159">View source</a>

``` python
assert_is_fully_defined()
```

Raises an exception if `self` is not fully defined in every dimension.


#### Raises:


* <b>`ValueError`</b>: If `self` does not have a known value for every dimension.

<h3 id="assert_same_rank"><code>assert_same_rank</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L969-L983">View source</a>

``` python
assert_same_rank(other)
```

Raises an exception if `self` and `other` do not have compatible ranks.


#### Args:


* <b>`other`</b>: Another `TensorShape`.


#### Raises:


* <b>`ValueError`</b>: If `self` and `other` do not represent shapes with the
  same rank.

<h3 id="concatenate"><code>concatenate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L946-L967">View source</a>

``` python
concatenate(other)
```

Returns the concatenation of the dimension in `self` and `other`.

*N.B.* If either `self` or `other` is completely unknown,
concatenation will discard information about the other shape. In
future, we might support concatenation that preserves this
information for use with slicing.

#### Args:


* <b>`other`</b>: Another `TensorShape`.


#### Returns:

A `TensorShape` whose dimensions are the concatenation of the
dimensions in `self` and `other`.


<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1055-L1100">View source</a>

``` python
is_compatible_with(other)
```

Returns True iff `self` is compatible with `other`.

Two possibly-partially-defined shapes are compatible if there
exists a fully-defined shape that both shapes can represent. Thus,
compatibility allows the shape inference code to reason about
partially-defined shapes. For example:

* TensorShape(None) is compatible with all shapes.

* TensorShape([None, None]) is compatible with all two-dimensional
  shapes, such as TensorShape([32, 784]), and also TensorShape(None). It is
  not compatible with, for example, TensorShape([None]) or
  TensorShape([None, None, None]).

* TensorShape([32, None]) is compatible with all two-dimensional shapes
  with size 32 in the 0th dimension, and also TensorShape([None, None])
  and TensorShape(None). It is not compatible with, for example,
  TensorShape([32]), TensorShape([32, None, 1]) or TensorShape([64, None]).

* TensorShape([32, 784]) is compatible with itself, and also
  TensorShape([32, None]), TensorShape([None, 784]), TensorShape([None,
  None]) and TensorShape(None). It is not compatible with, for example,
  TensorShape([32, 1, 784]) or TensorShape([None]).

The compatibility relation is reflexive and symmetric, but not
transitive. For example, TensorShape([32, 784]) is compatible with
TensorShape(None), and TensorShape(None) is compatible with
TensorShape([4, 4]), but TensorShape([32, 784]) is not compatible with
TensorShape([4, 4]).

#### Args:


* <b>`other`</b>: Another TensorShape.


#### Returns:

True iff `self` is compatible with `other`.


<h3 id="is_fully_defined"><code>is_fully_defined</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1147-L1150">View source</a>

``` python
is_fully_defined()
```

Returns True iff `self` is fully defined in every dimension.


<h3 id="merge_with"><code>merge_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L907-L934">View source</a>

``` python
merge_with(other)
```

Returns a `TensorShape` combining the information in `self` and `other`.

The dimensions in `self` and `other` are merged elementwise,
according to the rules defined for <a href="../tf/Dimension#merge_with"><code>Dimension.merge_with()</code></a>.

#### Args:


* <b>`other`</b>: Another `TensorShape`.


#### Returns:

A `TensorShape` containing the combined information of `self` and
`other`.



#### Raises:


* <b>`ValueError`</b>: If `self` and `other` are not compatible.

<h3 id="most_specific_compatible_shape"><code>most_specific_compatible_shape</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1117-L1145">View source</a>

``` python
most_specific_compatible_shape(other)
```

Returns the most specific TensorShape compatible with `self` and `other`.

* TensorShape([None, 1]) is the most specific TensorShape compatible with
  both TensorShape([2, 1]) and TensorShape([5, 1]). Note that
  TensorShape(None) is also compatible with above mentioned TensorShapes.

* TensorShape([1, 2, 3]) is the most specific TensorShape compatible with
  both TensorShape([1, 2, 3]) and TensorShape([1, 2, 3]). There are more
  less specific TensorShapes compatible with above mentioned TensorShapes,
  e.g. TensorShape([1, 2, None]), TensorShape(None).

#### Args:


* <b>`other`</b>: Another `TensorShape`.


#### Returns:

A `TensorShape` which is the most specific compatible shape of `self`
and `other`.


<h3 id="num_elements"><code>num_elements</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L897-L905">View source</a>

``` python
num_elements()
```

Returns the total number of elements, or none for incomplete shapes.


<h3 id="with_rank"><code>with_rank</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L997-L1015">View source</a>

``` python
with_rank(rank)
```

Returns a shape based on `self` with the given rank.

This method promotes a completely unknown shape to one with a
known rank.

#### Args:


* <b>`rank`</b>: An integer.


#### Returns:

A shape that is at least as specific as `self` with the given rank.



#### Raises:


* <b>`ValueError`</b>: If `self` does not represent a shape with the given `rank`.

<h3 id="with_rank_at_least"><code>with_rank_at_least</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1017-L1034">View source</a>

``` python
with_rank_at_least(rank)
```

Returns a shape based on `self` with at least the given rank.


#### Args:


* <b>`rank`</b>: An integer.


#### Returns:

A shape that is at least as specific as `self` with at least the given
rank.



#### Raises:


* <b>`ValueError`</b>: If `self` does not represent a shape with at least the given
  `rank`.

<h3 id="with_rank_at_most"><code>with_rank_at_most</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_shape.py#L1036-L1053">View source</a>

``` python
with_rank_at_most(rank)
```

Returns a shape based on `self` with at most the given rank.


#### Args:


* <b>`rank`</b>: An integer.


#### Returns:

A shape that is at least as specific as `self` with at most the given
rank.



#### Raises:


* <b>`ValueError`</b>: If `self` does not represent a shape with at most the given
  `rank`.
