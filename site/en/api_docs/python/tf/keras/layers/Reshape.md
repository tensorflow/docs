page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Reshape

## Class `Reshape`

Reshapes an output to a certain shape.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Reshape`
* Class `tf.compat.v2.keras.layers.Reshape`
* Class `tf.keras.layers.Reshape`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`target_shape`</b>: Target shape. Tuple of integers,
  does not include the samples dimension (batch size).


#### Input shape:

Arbitrary, although all dimensions in the input shaped must be fixed.
Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

`(batch_size,) + target_shape`



#### Example:



```python
# as first layer in a Sequential model
model = Sequential()
model.add(Reshape((3, 4), input_shape=(12,)))
# now: model.output_shape == (None, 3, 4)
# note: `None` is the batch dimension

# as intermediate layer in a Sequential model
model.add(Reshape((6, 2)))
# now: model.output_shape == (None, 6, 2)

# also supports shape inference using `-1` as dimension
model.add(Reshape((-1, 2, 2)))
# now: model.output_shape == (None, 3, 2, 2)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    target_shape,
    **kwargs
)
```






