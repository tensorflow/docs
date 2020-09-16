description: Outputs random values from a truncated normal distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.truncated_normal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.truncated_normal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/random_ops.py#L156-L197">
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
<p>`tf.compat.v1.random.truncated_normal`, `tf.compat.v1.truncated_normal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.truncated_normal(
    shape, mean=0.0, stddev=1.0, dtype=tf.dtypes.float32, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values follow a normal distribution with specified mean and
standard deviation, except that values whose magnitude is more than 2 standard
deviations from the mean are dropped and re-picked.

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
`mean`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The mean of the
truncated normal distribution.
</td>
</tr><tr>
<td>
`stddev`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The standard deviation
of the normal distribution, before truncation.
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
`seed`
</td>
<td>
A Python integer. Used to create a random seed for the distribution.
See
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>
for behavior.
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

