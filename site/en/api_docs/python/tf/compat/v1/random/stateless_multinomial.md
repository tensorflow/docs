description: Draws deterministic pseudorandom samples from a multinomial distribution. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.random.stateless_multinomial" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.random.stateless_multinomial

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/stateless_random_ops.py#L442-L480">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Draws deterministic pseudorandom samples from a multinomial distribution. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.random.stateless_multinomial(
    logits, num_samples, seed, output_dtype=tf.dtypes.int64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../../tf/random/stateless_categorical.md"><code>tf.random.stateless_categorical</code></a> instead.

This is a stateless version of <a href="../../../../tf/random/categorical.md"><code>tf.random.categorical</code></a>: if run twice with the
same seeds, it will produce the same pseudorandom numbers.  The output is
consistent across multiple runs on the same hardware (and between CPU
and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
hardware.

#### Example:



```python
# samples has shape [1, 5], where each value is either 0 or 1 with equal
# probability.
samples = tf.random.stateless_categorical(
    tf.math.log([[0.5, 0.5]]), 5, seed=[7, 17])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`logits`
</td>
<td>
2-D Tensor with shape `[batch_size, num_classes]`.  Each slice
`[i, :]` represents the unnormalized log-probabilities for all classes.
</td>
</tr><tr>
<td>
`num_samples`
</td>
<td>
0-D.  Number of independent samples to draw for each row slice.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A shape [2] integer Tensor of seeds to the random number generator.
</td>
</tr><tr>
<td>
`output_dtype`
</td>
<td>
integer type to use for the output. Defaults to int64.
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
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The drawn samples of shape `[batch_size, num_samples]`.
</td>
</tr>

</table>

