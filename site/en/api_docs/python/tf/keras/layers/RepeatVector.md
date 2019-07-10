page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.RepeatVector

## Class `RepeatVector`

Repeats the input n times.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.RepeatVector`
* Class `tf.compat.v2.keras.layers.RepeatVector`
* Class `tf.keras.layers.RepeatVector`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

<!-- Placeholder for "Used in" -->


#### Example:



```python
model = Sequential()
model.add(Dense(32, input_dim=32))
# now: model.output_shape == (None, 32)
# note: `None` is the batch dimension

model.add(RepeatVector(3))
# now: model.output_shape == (None, 3, 32)
```

#### Arguments:


* <b>`n`</b>: Integer, repetition factor.


#### Input shape:

2D tensor of shape `(num_samples, features)`.



#### Output shape:

3D tensor of shape `(num_samples, n, features)`.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    n,
    **kwargs
)
```






