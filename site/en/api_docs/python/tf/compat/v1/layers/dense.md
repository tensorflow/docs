description: Functional interface for the densely-connected layer. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.dense" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.layers.dense

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/legacy_tf_layers/core.py#L113-L187">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface for the densely-connected layer. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.dense(
    inputs, units, activation=None, use_bias=(True), kernel_initializer=None,
    bias_initializer=tf.zeros_initializer(), kernel_regularizer=None,
    bias_regularizer=None, activity_regularizer=None, kernel_constraint=None,
    bias_constraint=None, trainable=(True), name=None, reuse=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use keras.layers.Dense instead.

This layer implements the operation:
`outputs = activation(inputs * kernel + bias)`
where `activation` is the activation function passed as the `activation`
argument (if not `None`), `kernel` is a weights matrix created by the layer,
and `bias` is a bias vector created by the layer
(only if `use_bias` is `True`).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
Tensor input.
</td>
</tr><tr>
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
String, the name of the layer.
</td>
</tr><tr>
<td>
`reuse`
</td>
<td>
Boolean, whether to reuse the weights of a previous layer
by the same name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor the same shape as `inputs` except the last dimension is of
size `units`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if eager execution is enabled.
</td>
</tr>
</table>

