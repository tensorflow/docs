page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ActivityRegularization

## Class `ActivityRegularization`

Layer that applies an update to the cost function based input activity.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.ActivityRegularization`
* Class `tf.compat.v2.keras.layers.ActivityRegularization`
* Class `tf.keras.layers.ActivityRegularization`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`l1`</b>: L1 regularization factor (positive float).
* <b>`l2`</b>: L2 regularization factor (positive float).


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    l1=0.0,
    l2=0.0,
    **kwargs
)
```






