page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.dense

Functional interface for the densely-connected layer. (deprecated)

### Aliases:

* `tf.compat.v1.layers.dense`
* `tf.layers.dense`

``` python
tf.layers.dense(
    inputs,
    units,
    activation=None,
    use_bias=True,
    kernel_initializer=None,
    bias_initializer=tf.zeros_initializer(),
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    reuse=None
)
```



Defined in [`python/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/layers/core.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use keras.layers.dense instead.

This layer implements the operation:
`outputs = activation(inputs * kernel + bias)`
where `activation` is the activation function passed as the `activation`
argument (if not `None`), `kernel` is a weights matrix created by the layer,
and `bias` is a bias vector created by the layer
(only if `use_bias` is `True`).

#### Arguments:


* <b>`inputs`</b>: Tensor input.
* <b>`units`</b>: Integer or Long, dimensionality of the output space.
* <b>`activation`</b>: Activation function (callable). Set it to None to maintain a
  linear activation.
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias.
* <b>`kernel_initializer`</b>: Initializer function for the weight matrix.
  If `None` (default), weights are initialized using the default
  initializer used by <a href="../../tf/get_variable"><code>tf.compat.v1.get_variable</code></a>.
* <b>`bias_initializer`</b>: Initializer function for the bias.
* <b>`kernel_regularizer`</b>: Regularizer function for the weight matrix.
* <b>`bias_regularizer`</b>: Regularizer function for the bias.
* <b>`activity_regularizer`</b>: Regularizer function for the output.
* <b>`kernel_constraint`</b>: An optional projection function to be applied to the
    kernel after being updated by an `Optimizer` (e.g. used to implement
    norm constraints or value constraints for layer weights). The function
    must take as input the unprojected variable and must return the
    projected variable (which must have the same shape). Constraints are
    not safe to use when doing asynchronous distributed training.
* <b>`bias_constraint`</b>: An optional projection function to be applied to the
    bias after being updated by an `Optimizer`.
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
  <a href="../../tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a> (see <a href="../../tf/Variable"><code>tf.Variable</code></a>).
* <b>`name`</b>: String, the name of the layer.
* <b>`reuse`</b>: Boolean, whether to reuse the weights of a previous layer
  by the same name.


#### Returns:

Output tensor the same shape as `inputs` except the last dimension is of
size `units`.



#### Raises:


* <b>`ValueError`</b>: if eager execution is enabled.