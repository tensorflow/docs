page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.CategoricalCrossentropy

## Class `CategoricalCrossentropy`





Defined in [`tensorflow/python/keras/losses.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/losses.py).

Computes categorical cross entropy loss between the `y_true` and `y_pred`.

Usage:

```python
cce = tf.keras.losses.CategoricalCrossentropy()
loss = cce(
  [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]],
  [[.9, .05, .05], [.5, .89, .6], [.05, .01, .94]])
print('Loss: ', loss.numpy())  # Loss: 0.3239
```

Usage with tf.keras API:

```python
model = keras.models.Model(inputs, outputs)
model.compile('sgd', loss=tf.keras.losses.CategoricalCrossentropy())
````

#### Args:

* <b>`from_logits`</b>: Whether `output` is expected to be a logits tensor. By default,
    we consider that `output` encodes a probability distribution.
* <b>`label_smoothing`</b>: If greater than `0` then smooth the labels. This option is
    currently not supported when `y_pred` is a sparse input (not one-hot).
* <b>`reduction`</b>: Type of <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> to apply to loss. Default value is
    `SUM_OVER_BATCH_SIZE`.
* <b>`name`</b>: Optional name for the op.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    from_logits=False,
    label_smoothing=0,
    reduction=losses_impl.ReductionV2.SUM_OVER_BATCH_SIZE,
    name=None
)
```

Initialize self.  See help(type(self)) for accurate signature.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    y_true,
    y_pred,
    sample_weight=None
)
```

Invokes the `Loss` instance.

#### Args:

* <b>`y_true`</b>: Ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional `Tensor` whose rank is either 0, or the same rank
    as `y_true`, or is broadcastable to `y_true`. `sample_weight` acts as a
    coefficient for the loss. If a scalar is provided, then the loss is
    simply scaled by the given value. If `sample_weight` is a tensor of size
    `[batch_size]`, then the total loss for each sample of the batch is
    rescaled by the corresponding element in the `sample_weight` vector. If
    the shape of `sample_weight` matches the shape of `y_pred`, then the
    loss of each measurable element of `y_pred` is scaled by the
    corresponding value of `sample_weight`.


#### Returns:

Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same
  shape as `y_true`; otherwise, it is scalar.


#### Raises:

* <b>`ValueError`</b>: If the shape of `sample_weight` is invalid.

<h3 id="call"><code>call</code></h3>

``` python
call(
    y_true,
    y_pred
)
```

Invokes the `CategoricalCrossentropy` instance.

#### Args:

* <b>`y_true`</b>: Ground truth values.
* <b>`y_pred`</b>: The predicted values.


#### Returns:

Categorical cross entropy losses.

<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```

Instantiates a `Loss` from its config (output of `get_config()`).

#### Args:

* <b>`config`</b>: Output of `get_config()`.


#### Returns:

A `Loss` instance.

<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```





