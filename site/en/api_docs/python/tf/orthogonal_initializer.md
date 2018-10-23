


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.orthogonal_initializer

### `class tf.orthogonal_initializer`

See the guide: [Variables > Sharing Variables](../../../api_guides/python/state_ops#Sharing_Variables)

Initializer that generates an orthogonal matrix.

If the shape of the tensor to initialize is two-dimensional, i is initialized 
with an orthogonal matrix obtained from the singular value decomposition of a 
matrix of uniform random numbers.

If the shape of the tensor to initialize is more than two-dimensional,
a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])`
is initialized, where `n` is the length of the shape vector.
The matrix is subsequently reshaped to give a tensor of the desired shape.

#### Args:

* <b>`gain`</b>: multiplicative factor to apply to the orthogonal matrix
* <b>`dtype`</b>: The type of the output.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    [`tf.set_random_seed`](../tf/set_random_seed)
    for behavior.

## Methods

<h3 id="__init__"><code>__init__(gain=1.0, dtype=tf.float32, seed=None)</code></h3>







Defined in [`tensorflow/python/ops/init_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/init_ops.py).

