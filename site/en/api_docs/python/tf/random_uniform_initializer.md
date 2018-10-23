


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.random_uniform_initializer

### `class tf.random_uniform_initializer`

See the guide: [Variables > Sharing Variables](../../../api_guides/python/state_ops#Sharing_Variables)

Initializer that generates tensors with a uniform distribution.

#### Args:

* <b>`minval`</b>: A python scalar or a scalar tensor. Lower bound of the range
    of random values to generate.
* <b>`maxval`</b>: A python scalar or a scalar tensor. Upper bound of the range
    of random values to generate.  Defaults to 1 for float types.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    [`tf.set_random_seed`](../tf/set_random_seed)
    for behavior.
* <b>`dtype`</b>: The data type.

## Methods

<h3 id="__init__"><code>__init__(minval=0, maxval=None, seed=None, dtype=tf.float32)</code></h3>







Defined in [`tensorflow/python/ops/init_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/init_ops.py).

