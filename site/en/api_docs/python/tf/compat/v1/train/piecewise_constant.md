description: Piecewise constant from boundaries and interval values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.piecewise_constant" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.piecewise_constant

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py#L106-L179">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Piecewise constant from boundaries and interval values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.piecewise_constant_decay`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.piecewise_constant(
    x, boundaries, values, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5
  for the next 10000 steps, and 0.1 for any additional steps.

```python
global_step = tf.Variable(0, trainable=False)
boundaries = [100000, 110000]
values = [1.0, 0.5, 0.1]
learning_rate = tf.compat.v1.train.piecewise_constant(global_step, boundaries,
values)

# Later, whenever we perform an optimization step, we increment global_step.
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A 0-D scalar `Tensor`. Must be one of the following types: `float32`,
`float64`, `uint8`, `int8`, `int16`, `int32`, `int64`.
</td>
</tr><tr>
<td>
`boundaries`
</td>
<td>
A list of `Tensor`s or `int`s or `float`s with strictly
increasing entries, and with all elements having the same type as `x`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A list of `Tensor`s or `float`s or `int`s that specifies the values
for the intervals defined by `boundaries`. It should have one more element
than `boundaries`, and all elements should have the same type.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string. Optional name of the operation. Defaults to
'PiecewiseConstant'.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 0-D Tensor. Its value is `values[0]` when `x <= boundaries[0]`,
`values[1]` when `x > boundaries[0]` and `x <= boundaries[1]`, ...,
and values[-1] when `x > boundaries[-1]`.
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
if types of `x` and `boundaries` do not match, or types of all
`values` do not match or
the number of elements in the lists does not match.
</td>
</tr>
</table>




#### Eager Compatibility
When eager execution is enabled, this function returns a function which in
turn returns the decayed learning rate Tensor. This can be useful for changing
the learning rate value across different invocations of optimizer functions.

