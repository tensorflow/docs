page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.multinomial

Draws samples from a multinomial distribution. (deprecated)

### Aliases:

* `tf.compat.v1.multinomial`
* `tf.compat.v1.random.multinomial`
* `tf.multinomial`
* `tf.random.multinomial`

``` python
tf.random.multinomial(
    logits,
    num_samples,
    seed=None,
    name=None,
    output_dtype=None
)
```



Defined in [`python/ops/random_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/random_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/random/categorical"><code>tf.random.categorical</code></a> instead.

#### Example:



```python
# samples has shape [1, 5], where each value is either 0 or 1 with equal
# probability.
samples = tf.random.categorical(tf.math.log([[10., 10.]]), 5)
```

#### Args:


* <b>`logits`</b>: 2-D Tensor with shape `[batch_size, num_classes]`.  Each slice
  `[i, :]` represents the unnormalized log-probabilities for all classes.
* <b>`num_samples`</b>: 0-D.  Number of independent samples to draw for each row slice.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distribution.
  See <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`name`</b>: Optional name for the operation.
* <b>`output_dtype`</b>: integer type to use for the output. Defaults to int64.


#### Returns:

The drawn samples of shape `[batch_size, num_samples]`.
