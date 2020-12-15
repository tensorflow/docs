description: Optimizer that implements the FTRL algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.FtrlOptimizer" />
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

# tf.compat.v1.train.FtrlOptimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/ftrl.py#L29-L290">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the FTRL algorithm.

Inherits From: [`Optimizer`](../../../../tf/compat/v1/train/Optimizer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.FtrlOptimizer(
    learning_rate, learning_rate_power=-0.5, initial_accumulator_value=0.1,
    l1_regularization_strength=0.0, l2_regularization_strength=0.0,
    use_locking=(False), name='Ftrl', accum_name=None, linear_name=None,
    l2_shrinkage_regularization_strength=0.0, beta=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This version has support for both online L2 (McMahan et al., 2013) and
shrinkage-type L2, which is the addition of an L2 penalty
to the loss function.

#### References:

Ad-click prediction:
  [McMahan et al., 2013](https://dl.acm.org/citation.cfm?id=2488200)
  ([pdf](https://dl.acm.org/ft_gateway.cfm?id=2488200&ftid=1388399&dwn=1&CFID=32233078&CFTOKEN=d60fe57a294c056a-CB75C374-F915-E7A6-1573FBBC7BF7D526))


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
A float value or a constant float `Tensor`.
</td>
</tr><tr>
<td>
`learning_rate_power`
</td>
<td>
A float value, must be less or equal to zero.
Controls how the learning rate decreases during training. Use zero for
a fixed learning rate. See section 3.1 in (McMahan et al., 2013).
</td>
</tr><tr>
<td>
`initial_accumulator_value`
</td>
<td>
The starting value for accumulators.
Only zero or positive values are allowed.
</td>
</tr><tr>
<td>
`l1_regularization_strength`
</td>
<td>
A float value, must be greater than or
equal to zero.
</td>
</tr><tr>
<td>
`l2_regularization_strength`
</td>
<td>
A float value, must be greater than or
equal to zero.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
If `True` use locks for update operations.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients.  Defaults to "Ftrl".
</td>
</tr><tr>
<td>
`accum_name`
</td>
<td>
The suffix for the variable that keeps the gradient squared
accumulator.  If not present, defaults to name.
</td>
</tr><tr>
<td>
`linear_name`
</td>
<td>
The suffix for the variable that keeps the linear gradient
accumulator.  If not present, defaults to name + "_1".
</td>
</tr><tr>
<td>
`l2_shrinkage_regularization_strength`
</td>
<td>
A float value, must be greater than
or equal to zero. This differs from L2 above in that the L2 above is a
stabilization penalty, whereas this L2 shrinkage is a magnitude penalty.
The FTRL formulation can be written as:
w_{t+1} = argmin_w(\hat{g}_{1:t}w + L1*||w||_1 + L2*||w||_2^2), where
\hat{g} = g + (2*L2_shrinkage*w), and g is the gradient of the loss
function w.r.t. the weights w.
Specifically, in the absence of L1 regularization, it is equivalent to
the following update rule:
w_{t+1} = w_t - lr_t / (beta + 2*L2*lr_t) * g_t -
2*L2_shrinkage*lr_t / (beta + 2*L2*lr_t) * w_t
where lr_t is the learning rate at t.
When input is sparse shrinkage will only happen on the active weights.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
A float value; corresponds to the beta parameter in the paper.
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
If one of the arguments is invalid.
</td>
</tr>
</table>



## Methods

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/optimizer.py#L531-L640">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_gradients(
    grads_and_vars, global_step=None, name=None
)
</code></pre>

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
applies gradients.

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
Optional `Variable` to increment by one after the
variables have been updated.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the returned operation.  Default to the
name passed to the `Optimizer` constructor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Operation` that applies the specified gradients. If `global_step`
was not None, that operation also increments `global_step`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `grads_and_vars` is malformed.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If none of the variables have gradients.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If you should use `_distributed_apply()` instead.
</td>
</tr>
</table>



<h3 id="compute_gradients"><code>compute_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/optimizer.py#L415-L519">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>compute_gradients(
    loss, var_list=None, gate_gradients=GATE_OP, aggregation_method=None,
    colocate_gradients_with_ops=(False), grad_loss=None
)
</code></pre>

Compute gradients of `loss` for the variables in `var_list`.

This is the first part of `minimize()`.  It returns a list
of (gradient, variable) pairs where "gradient" is the gradient
for "variable".  Note that "gradient" can be a `Tensor`, an
`IndexedSlices`, or `None` if there is no gradient for the
given variable.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
A Tensor containing the value to minimize or a callable taking
no arguments which returns the value to minimize. When eager execution
is enabled it must be a callable.
</td>
</tr><tr>
<td>
`var_list`
</td>
<td>
Optional list or tuple of <a href="../../../../tf/Variable.md"><code>tf.Variable</code></a> to update to minimize
`loss`.  Defaults to the list of variables collected in the graph
under the key `GraphKeys.TRAINABLE_VARIABLES`.
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
If True, try colocating gradients with
the corresponding op.
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



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `var_list` contains anything else than `Variable` objects.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If some arguments are invalid.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called with eager execution enabled and `loss` is
not callable.
</td>
</tr>
</table>




#### Eager Compatibility
When eager execution is enabled, `gate_gradients`, `aggregation_method`,
and `colocate_gradients_with_ops` are ignored.



<h3 id="get_name"><code>get_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/optimizer.py#L352-L353">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_name()
</code></pre>




<h3 id="get_slot"><code>get_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/optimizer.py#L737-L773">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/optimizer.py#L775-L783">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/optimizer.py#L355-L413">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/optimizer.py#L785-L811">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variables()
</code></pre>

A list of variables which encode the current state of `Optimizer`.

Includes slot variables and additional global variables created by the
optimizer in the current default graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of variables.
</td>
</tr>

</table>





## Class Variables

* `GATE_GRAPH = 2` <a id="GATE_GRAPH"></a>
* `GATE_NONE = 0` <a id="GATE_NONE"></a>
* `GATE_OP = 1` <a id="GATE_OP"></a>
