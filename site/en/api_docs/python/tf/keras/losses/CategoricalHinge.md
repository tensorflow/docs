page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.CategoricalHinge

## Class `CategoricalHinge`

Computes the categorical hinge loss between `y_true` and `y_pred`.



### Aliases:

* Class `tf.compat.v1.keras.losses.CategoricalHinge`
* Class `tf.compat.v2.keras.losses.CategoricalHinge`
* Class `tf.compat.v2.losses.CategoricalHinge`
* Class `tf.keras.losses.CategoricalHinge`



Defined in [`python/keras/losses.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/losses.py).

<!-- Placeholder for "Used in" -->


#### Usage:



```python
ch = tf.keras.losses.CategoricalHinge()
loss = ch([0., 1., 1.], [1., 0., 1.])
print('Loss: ', loss.numpy())  # Loss: 1.0
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss=tf.keras.losses.CategoricalHinge())
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    reduction=losses_utils.ReductionV2.AUTO,
    name='categorical_hinge'
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






