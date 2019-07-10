page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Masking

## Class `Masking`

Masks a sequence by using a mask value to skip timesteps.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Masking`
* Class `tf.compat.v2.keras.layers.Masking`
* Class `tf.keras.layers.Masking`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

<!-- Placeholder for "Used in" -->

For each timestep in the input tensor (dimension #1 in the tensor),
if all values in the input tensor at that timestep
are equal to `mask_value`, then the timestep will be masked (skipped)
in all downstream layers (as long as they support masking).

If any downstream layer does not support masking yet receives such
an input mask, an exception will be raised.

#### Example:



Consider a Numpy data array `x` of shape `(samples, timesteps, features)`,
to be fed to an LSTM layer.
You want to mask timestep #3 and #5 because you lack data for
these timesteps. You can:

- Set `x[:, 3, :] = 0.` and `x[:, 5, :] = 0.`
- Insert a `Masking` layer with `mask_value=0.` before the LSTM layer:

```python
model = Sequential()
model.add(Masking(mask_value=0., input_shape=(timesteps, features)))
model.add(LSTM(32))
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    mask_value=0.0,
    **kwargs
)
```






