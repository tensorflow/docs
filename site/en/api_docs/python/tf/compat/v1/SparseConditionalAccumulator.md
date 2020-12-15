description: A conditional accumulator for aggregating sparse gradients.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.SparseConditionalAccumulator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="apply_grad"/>
<meta itemprop="property" content="apply_indexed_slices_grad"/>
<meta itemprop="property" content="num_accumulated"/>
<meta itemprop="property" content="set_global_step"/>
<meta itemprop="property" content="take_grad"/>
<meta itemprop="property" content="take_indexed_slices_grad"/>
</div>

# tf.compat.v1.SparseConditionalAccumulator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L1412-L1603">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A conditional accumulator for aggregating sparse gradients.

Inherits From: [`ConditionalAccumulatorBase`](../../../tf/compat/v1/ConditionalAccumulatorBase.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.SparseConditionalAccumulator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.SparseConditionalAccumulator(
    dtype, shape=None, shared_name=None, name='sparse_conditional_accumulator',
    reduction_type='MEAN'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Sparse gradients are represented by `IndexedSlices`.

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
`accumulator_ref`
</td>
<td>
A handle to the conditional accumulator, created by sub-
classes
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L1471-L1517">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_grad(
    grad_indices, grad_values, grad_shape=None, local_step=0, name=None
)
</code></pre>

Attempts to apply a sparse gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., `local_step`
is less than the accumulator's global time step.

A sparse gradient is represented by its indices, values and possibly empty
or None shape. Indices must be a vector representing the locations of
non-zero entries in the tensor. Values are the non-zero slices of the
gradient, and must have the same first dimension as indices, i.e., the nnz
represented by indices and values must be consistent. Shape, if not empty or
None, must be consistent with the accumulator's shape (if also provided).

#### Example:

A tensor [[0, 0], [0, 1], [2, 3]] can be represented
  indices: [1,2]
  values: [[0,1],[2,3]]
  shape: [3, 2]



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grad_indices`
</td>
<td>
Indices of the sparse gradient to be applied.
</td>
</tr><tr>
<td>
`grad_values`
</td>
<td>
Values of the sparse gradient to be applied.
</td>
</tr><tr>
<td>
`grad_shape`
</td>
<td>
Shape of the sparse gradient to be applied.
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
`InvalidArgumentError`
</td>
<td>
If grad is of the wrong shape
</td>
</tr>
</table>



<h3 id="apply_indexed_slices_grad"><code>apply_indexed_slices_grad</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L1447-L1469">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_indexed_slices_grad(
    grad, local_step=0, name=None
)
</code></pre>

Attempts to apply a gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., `local_step`
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
The gradient `IndexedSlices` to be applied.
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
`InvalidArgumentError`
</td>
<td>
If grad is of the wrong shape
</td>
</tr>
</table>



<h3 id="num_accumulated"><code>num_accumulated</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L1572-L1585">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L1587-L1603">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L1519-L1541">View source</a>

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
A tuple of indices, values, and shape representing the average gradient.
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
If `num_required` < 1
</td>
</tr>
</table>



<h3 id="take_indexed_slices_grad"><code>take_indexed_slices_grad</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L1543-L1569">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>take_indexed_slices_grad(
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
An `IndexedSlices` holding the value of the average gradient.
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
If `num_required` < 1
</td>
</tr>
</table>





