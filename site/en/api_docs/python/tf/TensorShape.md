


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.TensorShape

### `class tf.TensorShape`

See the guide: [Building Graphs > Defining new operations](../../../api_guides/python/framework#Defining_new_operations)

Represents the shape of a `Tensor`.

A `TensorShape` represents a possibly-partial shape specification for a
`Tensor`. It may be one of the following:

* *Fully-known shape:* has a known number of dimensions and a known size
  for each dimension.
* *Partially-known shape:* has a known number of dimensions, and an unknown
  size for one or more dimension.
* *Unknown shape:* has an unknown number of dimensions, and an unknown
  size in all dimensions.

If a tensor is produced by an operation of type `"Foo"`, its shape
may be inferred if there is a registered shape function for
`"Foo"`. See [`Shape functions in   C++`](../../../extend/adding_an_op#shape_functions_in_c) for
details of shape functions and how to register them. Alternatively,
the shape may be set explicitly using
[`tf.Tensor.set_shape`](../tf/Tensor#set_shape).

## Properties

<h3 id="dims"><code>dims</code></h3>

Returns a list of Dimensions, or None if the shape is unspecified.

<h3 id="ndims"><code>ndims</code></h3>

Returns the rank of this shape, or None if it is unspecified.



## Methods

<h3 id="__init__"><code>__init__(dims)</code></h3>

Creates a new TensorShape with the given dimensions.

#### Args:

* <b>`dims`</b>: A list of Dimensions, or None if the shape is unspecified.
    DEPRECATED: A single integer is treated as a singleton list.


#### Raises:

* <b>`TypeError`</b>: If dims cannot be converted to a list of dimensions.

<h3 id="as_list"><code>as_list()</code></h3>

Returns a list of integers or `None` for each dimension.

#### Returns:

  A list of integers or `None` for each dimension.


#### Raises:

* <b>`ValueError`</b>: If `self` is an unknown shape with an unknown rank.

<h3 id="as_proto"><code>as_proto()</code></h3>

Returns this shape as a `TensorShapeProto`.

<h3 id="assert_has_rank"><code>assert_has_rank(rank)</code></h3>

Raises an exception if `self` is not compatible with the given `rank`.

#### Args:

* <b>`rank`</b>: An integer.


#### Raises:

* <b>`ValueError`</b>: If `self` does not represent a shape with the given `rank`.

<h3 id="assert_is_compatible_with"><code>assert_is_compatible_with(other)</code></h3>

Raises exception if `self` and `other` do not represent the same shape.

This method can be used to assert that there exists a shape that both
`self` and `other` represent.

#### Args:

* <b>`other`</b>: Another TensorShape.


#### Raises:

* <b>`ValueError`</b>: If `self` and `other` do not represent the same shape.

<h3 id="assert_is_fully_defined"><code>assert_is_fully_defined()</code></h3>

Raises an exception if `self` is not fully defined in every dimension.

#### Raises:

* <b>`ValueError`</b>: If `self` does not have a known value for every dimension.

<h3 id="assert_same_rank"><code>assert_same_rank(other)</code></h3>

Raises an exception if `self` and `other` do not have compatible ranks.

#### Args:

* <b>`other`</b>: Another `TensorShape`.


#### Raises:

* <b>`ValueError`</b>: If `self` and `other` do not represent shapes with the
    same rank.

<h3 id="concatenate"><code>concatenate(other)</code></h3>

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

<h3 id="is_compatible_with"><code>is_compatible_with(other)</code></h3>

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

<h3 id="is_fully_defined"><code>is_fully_defined()</code></h3>

Returns True iff `self` is fully defined in every dimension.

<h3 id="merge_with"><code>merge_with(other)</code></h3>

Returns a `TensorShape` combining the information in `self` and `other`.

The dimensions in `self` and `other` are merged elementwise,
according to the rules defined for `Dimension.merge_with()`.

#### Args:

* <b>`other`</b>: Another `TensorShape`.


#### Returns:

  A `TensorShape` containing the combined information of `self` and
  `other`.


#### Raises:

* <b>`ValueError`</b>: If `self` and `other` are not compatible.

<h3 id="num_elements"><code>num_elements()</code></h3>

Returns the total number of elements, or none for incomplete shapes.

<h3 id="with_rank"><code>with_rank(rank)</code></h3>

Returns a shape based on `self` with the given rank.

This method promotes a completely unknown shape to one with a
known rank.

#### Args:

* <b>`rank`</b>: An integer.


#### Returns:

  A shape that is at least as specific as `self` with the given rank.


#### Raises:

* <b>`ValueError`</b>: If `self` does not represent a shape with the given `rank`.

<h3 id="with_rank_at_least"><code>with_rank_at_least(rank)</code></h3>

Returns a shape based on `self` with at least the given rank.

#### Args:

* <b>`rank`</b>: An integer.


#### Returns:

  A shape that is at least as specific as `self` with at least the given
  rank.


#### Raises:

* <b>`ValueError`</b>: If `self` does not represent a shape with at least the given
    `rank`.

<h3 id="with_rank_at_most"><code>with_rank_at_most(rank)</code></h3>

Returns a shape based on `self` with at most the given rank.

#### Args:

* <b>`rank`</b>: An integer.


#### Returns:

  A shape that is at least as specific as `self` with at most the given
  rank.


#### Raises:

* <b>`ValueError`</b>: If `self` does not represent a shape with at most the given
    `rank`.





Defined in [`tensorflow/python/framework/tensor_shape.py`](https://www.tensorflow.org/code/tensorflow/python/framework/tensor_shape.py).

