description: A conditional accumulator for aggregating gradients.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.ConditionalAccumulator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="apply_grad"/>
<meta itemprop="property" content="num_accumulated"/>
<meta itemprop="property" content="set_global_step"/>
<meta itemprop="property" content="take_grad"/>
</div>

# tf.compat.v1.ConditionalAccumulator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/data_flow_ops.py#L1320-L1407">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A conditional accumulator for aggregating gradients.

Inherits From: [`ConditionalAccumulatorBase`](../../../tf/compat/v1/ConditionalAccumulatorBase.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.ConditionalAccumulator(
    dtype, shape=None, shared_name=None, name='conditional_accumulator',
    reduction_type='MEAN'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Up-to-date gradients (i.e., time step at which gradient was computed is
equal to the accumulator's time step) are added to the accumulator.

Extraction of the average gradient is blocked until the required number of
gradients has been accumulated.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
Datatype of the accumulated gradients.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Shape of the accumulated gradients.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
Optional. If non-empty, this accumulator will be shared under
the given name across multiple sessions.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the accumulator.
</td>
</tr><tr>
<td>
`reduction_type`
</td>
<td>
Reduction type to use when taking the gradient.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`accumulator_ref`
</td>
<td>
The underlying accumulator reference.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The datatype of the gradients accumulated by this accumulator.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the underlying accumulator.
</td>
</tr>
</table>



## Methods

<h3 id="apply_grad"><code>apply_grad</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/data_flow_ops.py#L1358-L1380">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_grad(
    grad, local_step=0, name=None
)
</code></pre>

Attempts to apply a gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., local_step
is less than the accumulator's global time step.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grad`
</td>
<td>
The gradient tensor to be applied.
</td>
</tr><tr>
<td>
`local_step`
</td>
<td>
Time step at which the gradient was computed.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The operation that (conditionally) applies a gradient to the accumulator.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If grad is of the wrong shape
</td>
</tr>
</table>



<h3 id="num_accumulated"><code>num_accumulated</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/data_flow_ops.py#L1285-L1298">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>num_accumulated(
    name=None
)
</code></pre>

Number of gradients that have currently been aggregated in accumulator.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Number of accumulated gradients currently in accumulator.
</td>
</tr>

</table>



<h3 id="set_global_step"><code>set_global_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/data_flow_ops.py#L1300-L1316">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_global_step(
    new_global_step, name=None
)
</code></pre>

Sets the global time step of the accumulator.

The operation logs a warning if we attempt to set to a time step that is
lower than the accumulator's own time step.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`new_global_step`
</td>
<td>
Value of new time step. Can be a variable or a constant
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Operation that sets the accumulator's time step.
</td>
</tr>

</table>



<h3 id="take_grad"><code>take_grad</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/data_flow_ops.py#L1382-L1407">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>take_grad(
    num_required, name=None
)
</code></pre>

Attempts to extract the average gradient from the accumulator.

The operation blocks until sufficient number of gradients have been
successfully applied to the accumulator.

Once successful, the following actions are also triggered:

- Counter of accumulated gradients is reset to 0.
- Aggregated gradient is reset to 0 tensor.
- Accumulator's internal time step is incremented by 1.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`num_required`
</td>
<td>
Number of gradients that needs to have been aggregated
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor holding the value of the average gradient.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
If num_required < 1
</td>
</tr>
</table>





