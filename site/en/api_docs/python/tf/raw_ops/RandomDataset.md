description: Creates a Dataset that returns pseudorandom numbers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RandomDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RandomDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a Dataset that returns pseudorandom numbers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RandomDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RandomDataset(
    seed, seed2, output_types, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Creates a Dataset that returns a stream of uniformly distributed
pseudorandom 64-bit signed integers.

In the TensorFlow Python API, you can instantiate this dataset via the
class <a href="../../tf/data/experimental/RandomDataset.md"><code>tf.data.experimental.RandomDataset</code></a>.

Instances of this dataset are also created as a result of the
`hoist_random_uniform` static optimization. Whether this optimization is
performed is determined by the `experimental_optimization.hoist_random_uniform`
option of <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`seed`
</td>
<td>
A `Tensor` of type `int64`.
A scalar seed for the random number generator. If either seed or
seed2 is set to be non-zero, the random number generator is seeded
by the given seed.  Otherwise, a random seed is used.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
A `Tensor` of type `int64`.
A second scalar seed to avoid seed collision.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

