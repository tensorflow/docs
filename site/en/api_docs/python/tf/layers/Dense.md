page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.Dense

## Class `Dense`

Densely-connected layer class.

Inherits From: [`Dense`](../../tf/keras/layers/Dense), [`Layer`](../../tf/layers/Layer)

### Aliases:

* Class `tf.compat.v1.layers.Dense`
* Class `tf.layers.Dense`



Defined in [`python/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/layers/core.py).

<!-- Placeholder for "Used in" -->

This layer implements the operation:
`outputs = activation(inputs * kernel + bias)`
Where `activation` is the activation function passed as the `activation`
argument (if not `None`), `kernel` is a weights matrix created by the layer,
and `bias` is a bias vector created by the layer
(only if `use_bias` is `True`).

#### Arguments:


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
* <b>`name`</b>: String, the name of the layer. Layers with the same name will
  share weights, but to avoid mistakes we require reuse=True in such cases.
* <b>`_reuse`</b>: Boolean, whether to reuse the weights of a previous layer
  by the same name.


#### Properties:


* <b>`units`</b>: Python integer, dimensionality of the output space.
* <b>`activation`</b>: Activation function (callable).
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias.
* <b>`kernel_initializer`</b>: Initializer instance (or name) for the kernel matrix.
* <b>`bias_initializer`</b>: Initializer instance (or name) for the bias.
* <b>`kernel_regularizer`</b>: Regularizer instance for the kernel matrix (callable)
* <b>`bias_regularizer`</b>: Regularizer instance for the bias (callable).
* <b>`activity_regularizer`</b>: Regularizer instance for the output (callable)
* <b>`kernel_constraint`</b>: Constraint function for the kernel matrix.
* <b>`bias_constraint`</b>: Constraint function for the bias.
* <b>`kernel`</b>: Weight matrix (TensorFlow variable or tensor).
* <b>`bias`</b>: Bias vector, if applicable (TensorFlow variable or tensor).

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
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
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="scope_name"><code>scope_name</code></h3>






