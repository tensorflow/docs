description: Fused implementation of map and batch. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.map_and_batch" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.map_and_batch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/batching.py#L207-L264">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Fused implementation of `map` and `batch`. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.map_and_batch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.map_and_batch(
    map_func, batch_size, num_parallel_batches=None, drop_remainder=(False),
    num_parallel_calls=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/Dataset.md#map"><code>tf.data.Dataset.map(map_func, num_parallel_calls)</code></a> followed by <a href="../../../tf/data/Dataset.md#batch"><code>tf.data.Dataset.batch(batch_size, drop_remainder)</code></a>. Static tf.data optimizations will take care of using the fused implementation.

Maps `map_func` across `batch_size` consecutive elements of this dataset
and then combines them into a batch. Functionally, it is equivalent to `map`
followed by `batch`. This API is temporary and deprecated since input pipeline
optimization now fuses consecutive `map` and `batch` operations automatically.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`map_func`
</td>
<td>
A function mapping a nested structure of tensors to another
nested structure of tensors.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing the number of
consecutive elements of this dataset to combine in a single batch.
</td>
</tr><tr>
<td>
`num_parallel_batches`
</td>
<td>
(Optional.) A <a href="../../../tf.md#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>,
representing the number of batches to create in parallel. On one hand,
higher values can help mitigate the effect of stragglers. On the other
hand, higher values can increase contention if CPU is scarce.
</td>
</tr><tr>
<td>
`drop_remainder`
</td>
<td>
(Optional.) A <a href="../../../tf.md#bool"><code>tf.bool</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing
whether the last batch should be dropped in case its size is smaller than
desired; the default behavior is not to drop the smaller batch.
</td>
</tr><tr>
<td>
`num_parallel_calls`
</td>
<td>
(Optional.) A <a href="../../../tf.md#int32"><code>tf.int32</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>,
representing the number of elements to process in parallel. If not
specified, `batch_size * num_parallel_batches` elements will be processed
in parallel. If the value <a href="../../../tf/data.md#AUTOTUNE"><code>tf.data.AUTOTUNE</code></a> is used, then
the number of parallel calls is set dynamically based on available CPU.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
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
If both `num_parallel_batches` and `num_parallel_calls` are
specified.
</td>
</tr>
</table>

