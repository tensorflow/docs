description: An optimizer that applies loss scaling.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.experimental.MixedPrecisionLossScaleOptimizer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="apply_gradients"/>
<meta itemprop="property" content="compute_gradients"/>
<meta itemprop="property" content="get_name"/>
<meta itemprop="property" content="get_slot"/>
<meta itemprop="property" content="get_slot_names"/>
<meta itemprop="property" content="minimize"/>
<meta itemprop="property" content="variables"/>
<meta itemprop="property" content="GATE_GRAPH"/>
<meta itemprop="property" content="GATE_NONE"/>
<meta itemprop="property" content="GATE_OP"/>
</div>

# tf.compat.v1.train.experimental.MixedPrecisionLossScaleOptimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/experimental/loss_scale_optimizer.py#L31-L250">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An optimizer that applies loss scaling.

Inherits From: [`Optimizer`](../../../../../tf/compat/v1/train/Optimizer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.experimental.MixedPrecisionLossScaleOptimizer(
    opt, loss_scale
)
</code></pre>



<!-- Placeholder for "Used in" -->

Loss scaling is a process that multiplies the loss by a multiplier called the
loss scale, and divides each gradient by the same multiplier. The pseudocode
for this process is:

```
loss = ...
loss *= loss_scale
grads = gradients(loss, vars)
grads /= loss_scale
```

Mathematically, loss scaling has no effect, but can help avoid numerical
underflow in intermediate gradients when float16 tensors are used for mixed
precision training. By multiplying the loss, each intermediate gradient will
have the same multiplier applied.

The loss scale can either be a fixed constant, chosen by the user, or be
dynamically determined. Dynamically determining the loss scale is convenient
as a loss scale does not have to be explicitly chosen. However it reduces
performance.

This optimizer wraps another optimizer and applies loss scaling to it via a
`LossScale`. Loss scaling is applied whenever gradients are
computed, such as through `minimize()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`use_locking`
</td>
<td>
Bool. If True apply use locks to prevent concurrent updates
to variables.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A non-empty string.  The name to use for accumulators created
for the optimizer.
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
If name is malformed.
</td>
</tr>
</table>



## Methods

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/experimental/loss_scale_optimizer.py#L152-L185">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_gradients(
    grads_and_vars, global_step=None, name=None
)
</code></pre>

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
conditionally applies gradients if all gradient values are finite.
Otherwise no update is performed (nor is `global_step` incremented).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grads_and_vars`
</td>
<td>
List of (gradient, variable) pairs as returned by
`compute_gradients()`.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Optional `Variable` to increment by one after the variables
have been updated.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation.  Default to the name
passed to the `Optimizer` constructor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` that conditionally applies the specified gradients. If
`global_step` was not None, that operation also increments `global_step`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If you should use `_distributed_apply()` instead.
</td>
</tr>
</table>



<h3 id="compute_gradients"><code>compute_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/experimental/loss_scale_optimizer.py#L80-L126">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>compute_gradients(
    loss, var_list=None, gate_gradients=optimizer.Optimizer.GATE_OP,
    aggregation_method=None, colocate_gradients_with_ops=(False), grad_loss=None
)
</code></pre>

Compute gradients of `loss` for the variables in `var_list`.

This adjusts the dynamic range of the gradient evaluation by scaling up
the `loss` value. The gradient values are then scaled back down by the
reciprocal of the loss scale. This is useful in reduced precision training
where small gradient values would otherwise underflow the representable
range.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
A Tensor containing the value to minimize or a callable taking no
arguments which returns the value to minimize. When eager execution is
enabled it must be a callable.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
Optional list or tuple of <a href="../../../../../tf/Variable.md"><code>tf.Variable</code></a> to update to minimize
`loss`.  Defaults to the list of variables collected in the graph under
the key `GraphKeys.TRAINABLE_VARIABLES`.
</td>
</tr><tr>
<td>
`gate_gradients`
</td>
<td>
How to gate the computation of gradients.  Can be
`GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`.
</td>
</tr><tr>
<td>
`aggregation_method`
</td>
<td>
Specifies the method used to combine gradient terms.
Valid values are defined in the class `AggregationMethod`.
</td>
</tr><tr>
<td>
`colocate_gradients_with_ops`
</td>
<td>
If True, try colocating gradients with the
corresponding op.
</td>
</tr><tr>
<td>
`grad_loss`
</td>
<td>
Optional. A `Tensor` holding the gradient computed for `loss`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of (gradient, variable) pairs. Variable is always present, but
gradient can be `None`.
</td>
</tr>

</table>



<h3 id="get_name"><code>get_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/optimizer.py#L352-L353">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_name()
</code></pre>




<h3 id="get_slot"><code>get_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/optimizer.py#L737-L773">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot(
    var, name
)
</code></pre>

Return a slot named `name` created for `var` by the Optimizer.

Some `Optimizer` subclasses use additional variables.  For example
`Momentum` and `Adagrad` use variables to accumulate updates.  This method
gives access to these `Variable` objects if for some reason you need them.

Use `get_slot_names()` to get the list of slot names created by the
`Optimizer`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var`
</td>
<td>
A variable passed to `minimize()` or `apply_gradients()`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The `Variable` for the slot if it was created, `None` otherwise.
</td>
</tr>

</table>



<h3 id="get_slot_names"><code>get_slot_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/optimizer.py#L775-L783">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_slot_names()
</code></pre>

Return a list of the names of slots created by the `Optimizer`.

See `get_slot()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of strings.
</td>
</tr>

</table>



<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/optimizer.py#L355-L413">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>minimize(
    loss, global_step=None, var_list=None, gate_gradients=GATE_OP,
    aggregation_method=None, colocate_gradients_with_ops=(False), name=None,
    grad_loss=None
)
</code></pre>

Add operations to minimize `loss` by updating `var_list`.

This method simply combines calls `compute_gradients()` and
`apply_gradients()`. If you want to process the gradient before applying
them call `compute_gradients()` and `apply_gradients()` explicitly instead
of using this function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
A `Tensor` containing the value to minimize.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Optional `Variable` to increment by one after the
variables have been updated.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
Optional list or tuple of `Variable` objects to update to
minimize `loss`.  Defaults to the list of variables collected in
the graph under the key `GraphKeys.TRAINABLE_VARIABLES`.
</td>
</tr><tr>
<td>
`gate_gradients`
</td>
<td>
How to gate the computation of gradients.  Can be
`GATE_NONE`, `GATE_OP`, or  `GATE_GRAPH`.
</td>
</tr><tr>
<td>
`aggregation_method`
</td>
<td>
Specifies the method used to combine gradient terms.
Valid values are defined in the class `AggregationMethod`.
</td>
</tr><tr>
<td>
`colocate_gradients_with_ops`
</td>
<td>
If True, try colocating gradients with
the corresponding op.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation.
</td>
</tr><tr>
<td>
`grad_loss`
</td>
<td>
Optional. A `Tensor` holding the gradient computed for `loss`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An Operation that updates the variables in `var_list`.  If `global_step`
was not `None`, that operation also increments `global_step`.
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
If some of the variables are not `Variable` objects.
</td>
</tr>
</table>




#### Eager Compatibility
When eager execution is enabled, `loss` should be a Python function that
takes no arguments and computes the value to be minimized. Minimization (and
gradient computation) is done with respect to the elements of `var_list` if
not None, else with respect to any trainable variables created during the
execution of the `loss` function. `gate_gradients`, `aggregation_method`,
`colocate_gradients_with_ops` and `grad_loss` are ignored when eager
execution is enabled.



<h3 id="variables"><code>variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/experimental/loss_scale_optimizer.py#L247-L250">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variables()
</code></pre>

Returns the variables of the Optimizer.




## Class Variables

* `GATE_GRAPH = 2` <a id="GATE_GRAPH"></a>
* `GATE_NONE = 0` <a id="GATE_NONE"></a>
* `GATE_OP = 1` <a id="GATE_OP"></a>
