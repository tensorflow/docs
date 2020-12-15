description: Outputs random values from a truncated normal distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.stateless_parameterized_truncated_normal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.stateless_parameterized_truncated_normal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/stateless_random_ops.py#L665-L732">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs random values from a truncated normal distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.stateless_parameterized_truncated_normal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.stateless_parameterized_truncated_normal(
    shape, seed, means=0.0, stddevs=1.0, minvals=-2.0, maxvals=2.0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values follow a normal distribution with specified mean and
standard deviation, except that values whose magnitude is more than 2 standard
deviations from the mean are dropped and re-picked.


#### Examples:



Sample from a Truncated normal, with deferring shape parameters that
broadcast.

```
>>> means = 0.
>>> stddevs = tf.math.exp(tf.random.uniform(shape=[2, 3]))
>>> minvals = [-1., -2., -1000.]
>>> maxvals = [[10000.], [1.]]
>>> y = tf.random.stateless_parameterized_truncated_normal(
...   shape=[10, 2, 3], seed=[7, 17],
...   means=means, stddevs=stddevs, minvals=minvals, maxvals=maxvals)
>>> y.shape
TensorShape([10, 2, 3])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer `Tensor` or Python array. The shape of the output
tensor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A shape [2] Tensor, the seed to the random number generator. Must have
dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
</td>
</tr><tr>
<td>
`means`
</td>
<td>
A `Tensor` or Python value of type `dtype`. The mean of the truncated
normal distribution. This must broadcast with `stddevs`, `minvals` and
`maxvals`, and the broadcasted shape must be dominated by `shape`.
</td>
</tr><tr>
<td>
`stddevs`
</td>
<td>
A `Tensor` or Python value of type `dtype`. The standard deviation
of the truncated normal distribution. This must broadcast with `means`,
`minvals` and `maxvals`, and the broadcasted shape must be dominated by
`shape`.
</td>
</tr><tr>
<td>
`minvals`
</td>
<td>
A `Tensor` or Python value of type `dtype`. The minimum value of
the truncated normal distribution. This must broadcast with `means`,
`stddevs` and `maxvals`, and the broadcasted shape must be dominated by
`shape`.
</td>
</tr><tr>
<td>
`maxvals`
</td>
<td>
A `Tensor` or Python value of type `dtype`. The maximum value of
the truncated normal distribution. This must broadcast with `means`,
`stddevs` and `minvals`, and the broadcasted shape must be dominated by
`shape`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of the specified shape filled with random truncated normal values.
</td>
</tr>

</table>

