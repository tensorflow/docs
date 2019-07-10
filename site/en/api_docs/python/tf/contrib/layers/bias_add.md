page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.bias_add

``` python
tf.contrib.layers.bias_add(
    inputs,
    activation_fn=None,
    initializer=tf.zeros_initializer(),
    regularizer=None,
    reuse=None,
    variables_collections=None,
    outputs_collections=None,
    trainable=True,
    data_format=DATA_FORMAT_NHWC,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/layers/python/layers/layers.py).

Adds a bias to the inputs.

Can be used as a normalizer function for conv2d and fully_connected.

#### Args:

* <b>`inputs`</b>: A tensor of with at least rank 2 and value for the last dimension,
    e.g. `[batch_size, depth]`, `[None, None, None, depth]`.
* <b>`activation_fn`</b>: Activation function, default set to None to skip it and
    maintain a linear activation.
* <b>`initializer`</b>: An initializer for the bias, defaults to 0.
* <b>`regularizer`</b>: A regularizer like the result of
    `l1_regularizer` or `l2_regularizer`.
* <b>`reuse`</b>: Whether or not the layer and its variables should be reused. To be
    able to reuse the layer scope must be given.
* <b>`variables_collections`</b>: Optional collections for the variables.
* <b>`outputs_collections`</b>: Collections to add the outputs.
* <b>`trainable`</b>: If `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
* <b>`data_format`</b>: A string. 'NHWC' and 'NCHW' are supported.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

A tensor representing the result of adding biases to the inputs.


#### Raises:

* <b>`ValueError`</b>: If `data_format` is neither `NHWC` nor `NCHW`.
* <b>`ValueError`</b>: If `data_format` is `NCHW` and rank of `inputs` is not 4.
* <b>`ValueError`</b>: If the rank of `inputs` is undefined.
* <b>`ValueError`</b>: If rank or `C` dimension of `inputs` is undefined.