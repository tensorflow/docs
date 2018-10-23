


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.truncated_normal_initializer

### `class tf.truncated_normal_initializer`

See the guide: [Variables > Sharing Variables](../../../api_guides/python/state_ops#Sharing_Variables)

Initializer that generates a truncated normal distribution.

These values are similar to values from a `random_normal_initializer`
except that values more than two standard deviations from the mean
are discarded and re-drawn. This is the recommended initializer for
neural network weights and filters.

#### Args:

* <b>`mean`</b>: a python scalar or a scalar tensor. Mean of the random values
    to generate.
* <b>`stddev`</b>: a python scalar or a scalar tensor. Standard deviation of the
    random values to generate.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    [`tf.set_random_seed`](../tf/set_random_seed)
    for behavior.
* <b>`dtype`</b>: The data type. Only floating point types are supported.

## Methods

<h3 id="__init__"><code>__init__(mean=0.0, stddev=1.0, seed=None, dtype=tf.float32)</code></h3>







Defined in [`tensorflow/python/ops/init_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/init_ops.py).

