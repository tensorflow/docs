page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Permute

## Class `Permute`

Permutes the dimensions of the input according to a given pattern.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Permute`
* Class `tf.compat.v2.keras.layers.Permute`
* Class `tf.keras.layers.Permute`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

<!-- Placeholder for "Used in" -->

Useful for e.g. connecting RNNs and convnets together.

#### Example:



```python
model = Sequential()
model.add(Permute((2, 1), input_shape=(10, 64)))
# now: model.output_shape == (None, 64, 10)
# note: `None` is the batch dimension
```

#### Arguments:


* <b>`dims`</b>: Tuple of integers. Permutation pattern, does not include the
  samples dimension. Indexing starts at 1.
  For instance, `(2, 1)` permutes the first and second dimensions
  of the input.


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same as the input shape, but with the dimensions re-ordered according
to the specified pattern.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    dims,
    **kwargs
)
```






