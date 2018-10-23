


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.bias_add

### `tf.contrib.layers.bias_add`

```
tf.contrib.layers.bias_add(*args, **kwargs)
```


Adds a bias to the inputs.

Can be used as a normalizer function for conv2d and fully_connected.

#### Args:

* <b>`inputs`</b>: a tensor of with at least rank 2 and value for the last dimension,
    e.g. `[batch_size, depth]`, `[None, None, None, depth]`.
* <b>`activation_fn`</b>: activation function, default set to None to skip it and
    maintain a linear activation.
* <b>`initializer`</b>: An initializer for the bias, defaults to 0.
* <b>`regularizer`</b>: A regularizer like the result of
    `l1_regularizer` or `l2_regularizer`.
* <b>`reuse`</b>: whether or not the layer and its variables should be reused. To be
    able to reuse the layer scope must be given.
* <b>`variables_collections`</b>: optional collections for the variables.
* <b>`outputs_collections`</b>: collections to add the outputs.
* <b>`trainable`</b>: If `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
* <b>`data_format`</b>: A string. 'NHWC' and 'NCHW' are supported.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

  a tensor representing the result of adding biases to the inputs.


#### Raises:

* <b>`ValueError`</b>: if `data_format` is neither `NHWC` nor `NCHW`.
* <b>`ValueError`</b>: if `data_format` is `NCHW` and rank of `inputs` is not 4.
* <b>`ValueError`</b>: if the rank of `inputs` is undefined.
* <b>`ValueError`</b>: if rank or `C` dimension of `inputs` is undefined.

Defined in [`tensorflow/contrib/framework/python/ops/arg_scope.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/ops/arg_scope.py).

