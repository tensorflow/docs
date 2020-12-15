description: Outputs deterministic pseudorandom values from a Poisson distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.stateless_poisson" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.stateless_poisson

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/stateless_random_ops.py#L413-L473">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs deterministic pseudorandom values from a Poisson distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.stateless_poisson`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.stateless_poisson(
    shape, seed, lam, dtype=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values follow a Poisson distribution with specified rate
parameter.

This is a stateless version of <a href="../../tf/random/poisson.md"><code>tf.random.poisson</code></a>: if run twice with the same
seeds and shapes, it will produce the same pseudorandom numbers. The output is
consistent across multiple runs on the same hardware, but may change between
versions of TensorFlow or on non-CPU/GPU hardware.

A slight difference exists in the interpretation of the `shape` parameter
between `stateless_poisson` and `poisson`: in `poisson`, the `shape` is always
prepended to the shape of `lam`; whereas in `stateless_poisson` the shape of
`lam` must match the trailing dimensions of `shape`.

#### Example:



```python
samples = tf.random.stateless_poisson([10, 2], seed=[12, 34], lam=[5, 15])
# samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
# the samples drawn from each distribution

samples = tf.random.stateless_poisson([7, 5, 2], seed=[12, 34], lam=[5, 15])
# samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
# represents the 7x5 samples drawn from each of the two distributions

rate = tf.constant([[1.], [3.], [5.]])
samples = tf.random.stateless_poisson([30, 3, 1], seed=[12, 34], lam=rate)
# samples has shape [30, 3, 1], with 30 samples each of 3x1 distributions.
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
`lam`
</td>
<td>
Tensor. The rate parameter "lambda" of the Poisson distribution. Shape
must match the rightmost dimensions of `shape`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Dtype of the samples (int or float dtypes are permissible, as samples
are discrete). Default: int32.
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
A Tensor of the specified shape filled with random Poisson values.
For each i, each `samples[..., i]` is an independent draw from the Poisson
distribution with rate `lam[i]`.
</td>
</tr>
</table>

