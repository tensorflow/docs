page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.TimeDistributed

## Class `TimeDistributed`

This wrapper allows to apply a layer to every temporal slice of an input.

Inherits From: [`Wrapper`](../../../tf/keras/layers/Wrapper)

### Aliases:

* Class `tf.compat.v1.keras.layers.TimeDistributed`
* Class `tf.compat.v2.keras.layers.TimeDistributed`
* Class `tf.keras.layers.TimeDistributed`



Defined in [`python/keras/layers/wrappers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/wrappers.py).

<!-- Placeholder for "Used in" -->

The input should be at least 3D, and the dimension of index one
will be considered to be the temporal dimension.

Consider a batch of 32 samples,
where each sample is a sequence of 10 vectors of 16 dimensions.
The batch input shape of the layer is then `(32, 10, 16)`,
and the `input_shape`, not including the samples dimension, is `(10, 16)`.

You can then use `TimeDistributed` to apply a `Dense` layer
to each of the 10 timesteps, independently:

```python
# as the first layer in a model
model = Sequential()
model.add(TimeDistributed(Dense(8), input_shape=(10, 16)))
# now model.output_shape == (None, 10, 8)
```

The output will then have shape `(32, 10, 8)`.

In subsequent layers, there is no need for the `input_shape`:

```python
model.add(TimeDistributed(Dense(32)))
# now model.output_shape == (None, 10, 32)
```

The output will then have shape `(32, 10, 32)`.

`TimeDistributed` can be used with arbitrary layers, not just `Dense`,
for instance with a `Conv2D` layer:

```python
model = Sequential()
model.add(TimeDistributed(Conv2D(64, (3, 3)),
                          input_shape=(10, 299, 299, 3)))
```

#### Arguments:


* <b>`layer`</b>: a layer instance.


#### Call arguments:


* <b>`inputs`</b>: Input tensor.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. This argument is passed to the
  wrapped layer (only if the layer supports this argument).
* <b>`mask`</b>: Binary tensor of shape `(samples, timesteps)` indicating whether
  a given timestep should be masked. This argument is passed to the
  wrapped layer (only if the layer supports this argument).


#### Raises:


* <b>`ValueError`</b>: If not initialized with a `Layer` instance.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    layer,
    **kwargs
)
```






