description: Maintains moving averages of variables by employing an exponential decay.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.ExponentialMovingAverage" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="apply"/>
<meta itemprop="property" content="average"/>
<meta itemprop="property" content="average_name"/>
<meta itemprop="property" content="variables_to_restore"/>
</div>

# tf.train.ExponentialMovingAverage

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/moving_averages.py#L285-L575">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Maintains moving averages of variables by employing an exponential decay.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.ExponentialMovingAverage`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.train.ExponentialMovingAverage(
    decay, num_updates=None, zero_debias=(False), name='ExponentialMovingAverage'
)
</code></pre>



<!-- Placeholder for "Used in" -->

When training a model, it is often beneficial to maintain moving averages of
the trained parameters.  Evaluations that use averaged parameters sometimes
produce significantly better results than the final trained values.

The `apply()` method adds shadow copies of trained variables and add ops that
maintain a moving average of the trained variables in their shadow copies.
It is used when building the training model.  The ops that maintain moving
averages are typically run after each training step.
The `average()` and `average_name()` methods give access to the shadow
variables and their names.  They are useful when building an evaluation
model, or when restoring a model from a checkpoint file.  They help use the
moving averages in place of the last trained values for evaluations.

The moving averages are computed using exponential decay.  You specify the
decay value when creating the `ExponentialMovingAverage` object.  The shadow
variables are initialized with the same initial values as the trained
variables.  When you run the ops to maintain the moving averages, each
shadow variable is updated with the formula:

  `shadow_variable -= (1 - decay) * (shadow_variable - variable)`

This is mathematically equivalent to the classic formula below, but the use
of an `assign_sub` op (the `"-="` in the formula) allows concurrent lockless
updates to the variables:

  `shadow_variable = decay * shadow_variable + (1 - decay) * variable`

Reasonable values for `decay` are close to 1.0, typically in the
multiple-nines range: 0.999, 0.9999, etc.

Example usage when creating a training model:

```python
# Create variables.
var0 = tf.Variable(...)
var1 = tf.Variable(...)
# ... use the variables to build a training model...
...
# Create an op that applies the optimizer.  This is what we usually
# would use as a training op.
opt_op = opt.minimize(my_loss, [var0, var1])

# Create an ExponentialMovingAverage object
ema = tf.train.ExponentialMovingAverage(decay=0.9999)

with tf.control_dependencies([opt_op]):
    # Create the shadow variables, and add ops to maintain moving averages
    # of var0 and var1. This also creates an op that will update the moving
    # averages after each training step.  This is what we will use in place
    # of the usual training op.
    training_op = ema.apply([var0, var1])

...train the model by running training_op...
```

There are two ways to use the moving averages for evaluations:

*  Build a model that uses the shadow variables instead of the variables.
   For this, use the `average()` method which returns the shadow variable
   for a given variable.
*  Build a model normally but load the checkpoint files to evaluate by using
   the shadow variable names.  For this use the `average_name()` method.  See
   the <a href="../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a> for more
   information on restoring saved variables.

Example of restoring the shadow variable values:

```python
# Create a Saver that loads variables from their saved shadow values.
shadow_var0_name = ema.average_name(var0)
shadow_var1_name = ema.average_name(var1)
saver = tf.compat.v1.train.Saver({shadow_var0_name: var0, shadow_var1_name:
var1})
saver.restore(...checkpoint filename...)
# var0 and var1 now hold the moving average values
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`decay`
</td>
<td>
Float.  The decay to use.
</td>
</tr><tr>
<td>
`num_updates`
</td>
<td>
Optional count of number of updates applied to variables.
</td>
</tr><tr>
<td>
`zero_debias`
</td>
<td>
If `True`, zero debias moving-averages that are initialized
with tensors.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String. Optional prefix name to use for the name of ops added in
`apply()`.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of this ExponentialMovingAverage object.
</td>
</tr>
</table>



## Methods

<h3 id="apply"><code>apply</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/moving_averages.py#L403-L487">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply(
    var_list=None
)
</code></pre>

Maintains moving averages of variables.

`var_list` must be a list of `Variable` or `Tensor` objects.  This method
creates shadow variables for all elements of `var_list`.  Shadow variables
for `Variable` objects are initialized to the variable's initial value.
They will be added to the `GraphKeys.MOVING_AVERAGE_VARIABLES` collection.
For `Tensor` objects, the shadow variables are initialized to 0 and zero
debiased (see docstring in `assign_moving_average` for more details).

shadow variables are created with `trainable=False` and added to the
`GraphKeys.ALL_VARIABLES` collection.  They will be returned by calls to
<a href="../../tf/compat/v1/global_variables.md"><code>tf.compat.v1.global_variables()</code></a>.

Returns an op that updates all shadow variables from the current value of
their associated variables.

Note that `apply()` can be called multiple times. When eager execution is
enabled each call to apply will update the variables once, so this needs to
be called in a loop.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var_list`
</td>
<td>
A list of Variable or Tensor objects. The variables and Tensors
must be of types bfloat16, float16, float32, or float64.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An Operation that updates the moving averages.
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
If the arguments are not an allowed type.
</td>
</tr>
</table>



<h3 id="average"><code>average</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/moving_averages.py#L489-L499">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>average(
    var
)
</code></pre>

Returns the `Variable` holding the average of `var`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var`
</td>
<td>
A `Variable` object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Variable` object or `None` if the moving average of `var`
is not maintained.
</td>
</tr>

</table>



<h3 id="average_name"><code>average_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/moving_averages.py#L501-L526">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>average_name(
    var
)
</code></pre>

Returns the name of the `Variable` holding the average for `var`.

The typical scenario for `ExponentialMovingAverage` is to compute moving
averages of variables during training, and restore the variables from the
computed moving averages during evaluations.

To restore variables, you have to know the name of the shadow variables.
That name and the original variable can then be passed to a `Saver()` object
to restore the variable from the moving average value with:
  `saver = tf.compat.v1.train.Saver({ema.average_name(var): var})`

`average_name()` can be called whether or not `apply()` has been called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`var`
</td>
<td>
A `Variable` object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A string: The name of the variable that will be used or was used
by the `ExponentialMovingAverage class` to hold the moving average of
`var`.
</td>
</tr>

</table>



<h3 id="variables_to_restore"><code>variables_to_restore</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/moving_averages.py#L528-L575">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variables_to_restore(
    moving_avg_variables=None
)
</code></pre>

Returns a map of names to `Variables` to restore.

If a variable has a moving average, use the moving average variable name as
the restore name; otherwise, use the variable name.

For example,

```python
  variables_to_restore = ema.variables_to_restore()
  saver = tf.compat.v1.train.Saver(variables_to_restore)
```

Below is an example of such mapping:

```
  conv/batchnorm/gamma/ExponentialMovingAverage: conv/batchnorm/gamma,
  conv_4/conv2d_params/ExponentialMovingAverage: conv_4/conv2d_params,
  global_step: global_step
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`moving_avg_variables`
</td>
<td>
a list of variables that require to use of the
moving average variable name to be restored. If None, it will default to
variables.moving_average_variables() + variables.trainable_variables()
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A map from restore_names to variables. The restore_name is either the
original or the moving average version of the variable name, depending
on whether the variable name is in the `moving_avg_variables`.
</td>
</tr>

</table>





