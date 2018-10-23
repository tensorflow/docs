


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.Dimension

### `class tf.Dimension`

See the guide: [Building Graphs > Defining new operations](../../../api_guides/python/framework#Defining_new_operations)

Represents the value of one dimension in a TensorShape.

## Properties

<h3 id="value"><code>value</code></h3>

The value of this dimension, or None if it is unknown.



## Methods

<h3 id="__init__"><code>__init__(value)</code></h3>

Creates a new Dimension with the given value.

<h3 id="assert_is_compatible_with"><code>assert_is_compatible_with(other)</code></h3>

Raises an exception if `other` is not compatible with this Dimension.

#### Args:

* <b>`other`</b>: Another Dimension.


#### Raises:

* <b>`ValueError`</b>: If `self` and `other` are not compatible (see
    is_compatible_with).

<h3 id="is_compatible_with"><code>is_compatible_with(other)</code></h3>

Returns true if `other` is compatible with this Dimension.

Two known Dimensions are compatible if they have the same value.
An unknown Dimension is compatible with all other Dimensions.

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

  True if this Dimension and `other` are compatible.

<h3 id="merge_with"><code>merge_with(other)</code></h3>

Returns a Dimension that combines the information in `self` and `other`.

Dimensions are combined as follows:

```python
    Dimension(n)   .merge_with(Dimension(n))    == Dimension(n)
    Dimension(n)   .merge_with(Dimension(None)) == Dimension(n)
    Dimension(None).merge_with(Dimension(n))    == Dimension(n)
    Dimension(None).merge_with(Dimension(None)) == Dimension(None)
    Dimension(n)   .merge_with(Dimension(m)) raises ValueError for n != m
```

#### Args:

* <b>`other`</b>: Another Dimension.


#### Returns:

  A Dimension containing the combined information of `self` and
  `other`.


#### Raises:

* <b>`ValueError`</b>: If `self` and `other` are not compatible (see
    is_compatible_with).





Defined in [`tensorflow/python/framework/tensor_shape.py`](https://www.tensorflow.org/code/tensorflow/python/framework/tensor_shape.py).

