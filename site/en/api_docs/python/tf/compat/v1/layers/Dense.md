description: Densely-connected layer class.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.Dense" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.compat.v1.layers.Dense

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/legacy_tf_layers/core.py#L33-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Densely-connected layer class.

Inherits From: [`Dense`](../../../../tf/keras/layers/Dense.md), [`Layer`](../../../../tf/compat/v1/layers/Layer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.Dense(
    units, activation=None, use_bias=(True), kernel_initializer=None,
    bias_initializer=tf.zeros_initializer(), kernel_regularizer=None,
    bias_regularizer=None, activity_regularizer=None, kernel_constraint=None,
    bias_constraint=None, trainable=(True), name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer implements the operation:
`outputs = activation(inputs * kernel + bias)`
Where `activation` is the activation function passed as the `activation`
argument (if not `None`), `kernel` is a weights matrix created by the layer,
and `bias` is a bias vector created by the layer
(only if `use_bias` is `True`).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`units`
</td>
<td>
Integer or Long, dimensionality of the output space.
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function (callable). Set it to None to maintain a
linear activation.
</td>
</tr><tr>
<td>
`use_bias`
</td>
<td>
Boolean, whether the layer uses a bias.
</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>
Initializer function for the weight matrix.
If `None` (default), weights are initialized using the default
initializer used by <a href="../../../../tf/compat/v1/get_variable.md"><code>tf.compat.v1.get_variable</code></a>.
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
Initializer function for the bias.
</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>
Regularizer function for the weight matrix.
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Regularizer function for the bias.
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Regularizer function for the output.
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
An optional projection function to be applied to the
kernel after being updated by an `Optimizer` (e.g. used to implement
norm constraints or value constraints for layer weights). The function
must take as input the unprojected variable and must return the
projected variable (which must have the same shape). Constraints are
not safe to use when doing asynchronous distributed training.
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
An optional projection function to be applied to the
bias after being updated by an `Optimizer`.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` also add variables to the graph collection
`GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a>).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String, the name of the layer. Layers with the same name will
share weights, but to avoid mistakes we require reuse=True in such cases.
</td>
</tr><tr>
<td>
`_reuse`
</td>
<td>
Boolean, whether to reuse the weights of a previous layer
by the same name.
</td>
</tr>
</table>



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




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.
</td>
</tr><tr>
<td>
`scope_name`
</td>
<td>

</td>
</tr>
</table>



