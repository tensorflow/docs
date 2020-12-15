description: Optimizer that implements the Adadelta algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.Adadelta" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.optimizers.Adadelta

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/adadelta.py#L32-L160">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the Adadelta algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.Adadelta`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.Adadelta`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.Adadelta(
    learning_rate=0.001, rho=0.95, epsilon=1e-07, name='Adadelta', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Adadelta optimization is a stochastic gradient descent method that is based on
adaptive learning rate per dimension to address two drawbacks:

- The continual decay of learning rates throughout training
- The need for a manually selected global learning rate

Adadelta is a more robust extension of Adagrad that adapts learning rates
based on a moving window of gradient updates, instead of accumulating all
past gradients. This way, Adadelta continues learning even when many updates
have been done. Compared to Adagrad, in the original version of Adadelta you
don't have to set an initial learning rate. In this version, initial
learning rate can be set, as in most other Keras optimizers.

According to section 4.3 ("Effective Learning rates"), near the end of
training step sizes converge to 1 which is effectively a high learning
rate which would cause divergence. This occurs only near the end of the
training as gradients and step sizes are small, and the epsilon constant
in the numerator and denominator dominate past gradients and parameter
updates which converge the learning rate to 1.

According to section 4.4("Speech Data"),where a large neural network with
4 hidden layers was trained on a corpus of US English data, ADADELTA was
used with 100 network replicas.The epsilon used is 1e-6 with rho=0.95
which converged faster than ADAGRAD, by the following construction:
def __init__(self, lr=1.0, rho=0.95, epsilon=1e-6, decay=0., **kwargs):

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
A `Tensor`, floating point value, or a schedule that is a
<a href="../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a>. The learning rate.
To match the exact form in the original paper use 1.0.
</td>
</tr><tr>
<td>
`rho`
</td>
<td>
A `Tensor` or a floating point value. The decay rate.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A `Tensor` or a floating point value.  A constant epsilon used
to better conditioning the grad update.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients.  Defaults to `"Adadelta"`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments. Allowed to be one of
`"clipnorm"` or `"clipvalue"`.
`"clipnorm"` (float) clips gradients by norm; `"clipvalue"` (float) clips
gradients by value.
</td>
</tr>
</table>



#### Reference:

- [Zeiler, 2012](http://arxiv.org/abs/1212.5701)


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
String. The name to use for momentum accumulator weights created
by the optimizer.
</td>
</tr><tr>
<td>
`gradient_aggregator`
</td>
<td>
The function to use to aggregate gradients across
devices (when using <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>). If `None`, defaults to
summing the gradients across devices. The function should accept and
return a list of `(gradient, variable)` tuples.
</td>
</tr><tr>
<td>
`gradient_transformers`
</td>
<td>
Optional. List of functions to use to transform
gradients before applying updates to Variables. The functions are
applied after `gradient_aggregator`. The functions should accept and
return a list of `(gradient, variable)` tuples.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
keyword arguments. Allowed arguments are `clipvalue`,
`clipnorm`, `global_clipnorm`.
If `clipvalue` (float) is set, the gradient of each weight
is clipped to be no higher than this value.
If `clipnorm` (float) is set, the gradient of each weight
is individually clipped so that its norm is no higher than this value.
If `global_clipnorm` (float) is set the gradient of all weights is
clipped so that their global norm is no higher than this value.
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
in case of any invalid argument.
</td>
</tr>
</table>



