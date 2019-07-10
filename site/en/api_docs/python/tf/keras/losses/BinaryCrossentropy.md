page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.BinaryCrossentropy

## Class `BinaryCrossentropy`

Computes the cross-entropy loss between true labels and predicted labels.



### Aliases:

* Class `tf.compat.v1.keras.losses.BinaryCrossentropy`
* Class `tf.compat.v2.keras.losses.BinaryCrossentropy`
* Class `tf.compat.v2.losses.BinaryCrossentropy`
* Class `tf.keras.losses.BinaryCrossentropy`



Defined in [`python/keras/losses.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/losses.py).

<!-- Placeholder for "Used in" -->

Use this cross-entropy loss when there are only two label classes (assumed to
be 0 and 1). For each example, there should be a single floating-point value
per prediction.

In the snippet below, each of the four examples has only a single
floating-pointing value, and both `y_pred` and `y_true` have the shape
`[batch_size]`.

#### Usage:



```python
bce = tf.keras.losses.BinaryCrossentropy()
loss = bce([0., 0., 1., 1.], [1., 1., 1., 0.])
print('Loss: ', loss.numpy())  # Loss: 11.522857
```

Usage with the <a href="../../../tf/keras"><code>tf.keras</code></a> API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss=tf.keras.losses.BinaryCrossentropy())
```

#### Args:


* <b>`from_logits`</b>: Whether to interpret `y_pred` as a tensor of
  [logit](https://en.wikipedia.org/wiki/Logit) values. By default, we assume
    that `y_pred` contains probabilities (i.e., values in [0, 1]).
* <b>`label_smoothing`</b>: Float in [0, 1]. When 0, no smoothing occurs. When > 0, we
  compute the loss between the predicted labels and a smoothed version of
  the true labels, where the smoothing squeezes the labels towards 0.5.
  Larger values of `label_smoothing` correspond to heavier smoothing.
* <b>`reduction`</b>: (Optional) Type of `tf.keras.losses.Reduction` to apply to loss.
  Default value is `AUTO`. `AUTO` indicates that the reduction option will
  be determined by the usage context. For almost all cases this defaults to
  `SUM_OVER_BATCH_SIZE`.
  When used with <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>, outside of built-in training
  loops such as <a href="../../../tf/keras"><code>tf.keras</code></a> `compile` and `fit`, using `AUTO` or
  `SUM_OVER_BATCH_SIZE` will raise an error. Please see
  https://www.tensorflow.org/alpha/tutorials/distribute/training_loops
  for more details on this.
* <b>`name`</b>: (Optional) Name for the op.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    from_logits=False,
    label_smoothing=0,
    reduction=losses_utils.ReductionV2.AUTO,
    name='binary_crossentropy'
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






