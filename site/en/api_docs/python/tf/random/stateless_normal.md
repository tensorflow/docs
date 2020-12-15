description: Outputs deterministic pseudorandom values from a normal distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.stateless_normal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.stateless_normal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/stateless_random_ops.py#L476-L519">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs deterministic pseudorandom values from a normal distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.stateless_normal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.stateless_normal(
    shape, seed, mean=0.0, stddev=1.0, dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a stateless version of <a href="../../tf/random/normal.md"><code>tf.random.normal</code></a>: if run twice with the
same seeds and shapes, it will produce the same pseudorandom numbers.  The
output is consistent across multiple runs on the same hardware (and between
CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
hardware.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output tensor.
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
`mean`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The mean of the normal
distribution.
</td>
</tr><tr>
<td>
`stddev`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The standard deviation
of the normal distribution.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output.
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
A tensor of the specified shape filled with random normal values.
</td>
</tr>

</table>

