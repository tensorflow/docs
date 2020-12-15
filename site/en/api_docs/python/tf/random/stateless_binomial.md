description: Outputs deterministic pseudorandom values from a binomial distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.stateless_binomial" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.stateless_binomial

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/stateless_random_ops.py#L243-L310">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs deterministic pseudorandom values from a binomial distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.stateless_binomial`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.stateless_binomial(
    shape, seed, counts, probs, output_dtype=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values follow a binomial distribution with specified count and
probability of success parameters.

This is a stateless version of <a href="../../tf/random/Generator.md#binomial"><code>tf.random.Generator.binomial</code></a>: if run twice
with the same seeds and shapes, it will produce the same pseudorandom numbers.
The output is consistent across multiple runs on the same hardware (and
between CPU and GPU), but may change between versions of TensorFlow or on
non-CPU/GPU hardware.

#### Example:



```python
counts = [10., 20.]
# Probability of success.
probs = [0.8]

binomial_samples = tf.random.stateless_binomial(
    shape=[2], seed=[123, 456], counts=counts, probs=probs)

counts = ... # Shape [3, 1, 2]
probs = ...  # Shape [1, 4, 2]
shape = [3, 4, 3, 4, 2]
# Sample shape will be [3, 4, 3, 4, 2]
binomial_samples = tf.random.stateless_binomial(
    shape=shape, seed=[123, 456], counts=counts, probs=probs)
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
`counts`
</td>
<td>
Tensor. The counts of the binomial distribution. Must be
broadcastable with `probs`, and broadcastable with the rightmost
dimensions of `shape`.
</td>
</tr><tr>
<td>
`probs`
</td>
<td>
Tensor. The probability of success for the binomial distribution.
Must be broadcastable with `counts` and broadcastable with the rightmost
dimensions of `shape`.
</td>
</tr><tr>
<td>
`output_dtype`
</td>
<td>
The type of the output. Default: tf.int32
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

<tr>
<td>
`samples`
</td>
<td>
A Tensor of the specified shape filled with random binomial
values.  For each i, each samples[..., i] is an independent draw from
the binomial distribution on counts[i] trials with probability of
success probs[i].
</td>
</tr>
</table>

