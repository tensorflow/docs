page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.Loss

## Class `Loss`

Loss base class.



### Aliases:

* Class `tf.compat.v1.keras.losses.Loss`
* Class `tf.compat.v2.keras.losses.Loss`
* Class `tf.compat.v2.losses.Loss`
* Class `tf.keras.losses.Loss`



Defined in [`python/keras/losses.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/losses.py).

<!-- Placeholder for "Used in" -->

To be implemented by subclasses:
* `call()`: Contains the logic for loss calculation using `y_true`, `y_pred`.

Example subclass implementation:

```
class MeanSquaredError(Loss):
  def call(self, y_true, y_pred):
    y_pred = ops.convert_to_tensor(y_pred)
    y_true = math_ops.cast(y_true, y_pred.dtype)
    return K.mean(math_ops.square(y_pred - y_true), axis=-1)
```

When used with <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>, outside of built-in training loops
such as <a href="../../../tf/keras"><code>tf.keras</code></a> `compile` and `fit`, please use 'SUM' or 'NONE' reduction
types, and reduce losses explicitly in your training loop. Using 'AUTO' or
'SUM_OVER_BATCH_SIZE' will raise an error.

Please see
https://www.tensorflow.org/alpha/tutorials/distribute/training_loops for more
details on this.

You can implement 'SUM_OVER_BATCH_SIZE' using global batch size like:

```
with strategy.scope():
  loss_obj = tf.keras.losses.CategoricalCrossentropy(
      reduction=tf.keras.losses.Reduction.NONE)
  ....
  loss = (tf.reduce_sum(loss_obj(labels, predictions)) *
          (1. / global_batch_size))
```

#### Args:


* <b>`reduction`</b>: (Optional) Type of `tf.keras.losses.Reduction` to apply to loss.
  Default value is `AUTO`. `AUTO` indicates that the reduction option will
  be determined by the usage context. For almost all cases this defaults to
  `SUM_OVER_BATCH_SIZE`.
  When used with <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>, outside of built-in training
  loops such as <a href="../../../tf/keras"><code>tf.keras</code></a> `compile` and `fit`, using `AUTO` or
  `SUM_OVER_BATCH_SIZE` will raise an error. Please see
  https://www.tensorflow.org/alpha/tutorials/distribute/training_loops
  for more details on this.
* <b>`name`</b>: Optional name for the op.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    reduction=losses_utils.ReductionV2.AUTO,
    name=None
)
```






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

Invokes the `Loss` instance.


#### Args:


* <b>`y_true`</b>: Ground truth values, with the same shape as 'y_pred'.
* <b>`y_pred`</b>: The predicted values.

<h3 id="from_config"><code>from_config</code></h3>

``` python
@classmethod
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






