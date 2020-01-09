page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.stateless.stateless_multinomial

``` python
tf.contrib.stateless.stateless_multinomial(
    logits,
    num_samples,
    seed,
    output_dtype=tf.int64,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_stateless_random_ops.py`.

Draws samples from a multinomial distribution.

#### Args:

* <b>`logits`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    2-D Tensor with shape `[batch_size, num_classes]`.  Each slice `[i, :]`
    represents the unnormalized log probabilities for all classes.
* <b>`num_samples`</b>: A `Tensor` of type `int32`.
    0-D.  Number of independent samples to draw for each row slice.
* <b>`seed`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    2 seeds (shape [2]).
* <b>`output_dtype`</b>: An optional <a href="../../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../../tf#int64"><code>tf.int64</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `output_dtype`.