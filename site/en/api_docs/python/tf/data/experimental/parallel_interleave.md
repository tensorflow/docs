description: A parallel version of the <a href="../../../tf/data/Dataset.md#interleave"><code>Dataset.interleave()</code></a> transformation. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.parallel_interleave" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.parallel_interleave

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/interleave_ops.py#L37-L101">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A parallel version of the <a href="../../../tf/data/Dataset.md#interleave"><code>Dataset.interleave()</code></a> transformation. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.parallel_interleave`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.parallel_interleave(
    map_func, cycle_length, block_length=1, sloppy=(False),
    buffer_output_elements=None, prefetch_input_elements=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/Dataset.md#interleave"><code>tf.data.Dataset.interleave(map_func, cycle_length, block_length, num_parallel_calls=tf.data.experimental.AUTOTUNE)</code></a> instead. If sloppy execution is desired, use <a href="../../../tf/data/Options.md#experimental_deterministic"><code>tf.data.Options.experimental_deterministic</code></a>.

`parallel_interleave()` maps `map_func` across its input to produce nested
datasets, and outputs their elements interleaved. Unlike
<a href="../../../tf/data/Dataset.md#interleave"><code>tf.data.Dataset.interleave</code></a>, it gets elements from `cycle_length` nested
datasets in parallel, which increases the throughput, especially in the
presence of stragglers. Furthermore, the `sloppy` argument can be used to
improve performance, by relaxing the requirement that the outputs are produced
in a deterministic order, and allowing the implementation to skip over nested
datasets whose elements are not readily available when requested.

#### Example usage:



```python
# Preprocess 4 files concurrently.
filenames = tf.data.Dataset.list_files("/path/to/data/train*.tfrecords")
dataset = filenames.apply(
    tf.data.experimental.parallel_interleave(
        lambda filename: tf.data.TFRecordDataset(filename),
        cycle_length=4))
```

WARNING: If `sloppy` is `True`, the order of produced elements is not
deterministic.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`map_func`
</td>
<td>
A function mapping a nested structure of tensors to a `Dataset`.
</td>
</tr><tr>
<td>
`cycle_length`
</td>
<td>
The number of input `Dataset`s to interleave from in parallel.
</td>
</tr><tr>
<td>
`block_length`
</td>
<td>
The number of consecutive elements to pull from an input
`Dataset` before advancing to the next input `Dataset`.
</td>
</tr><tr>
<td>
`sloppy`
</td>
<td>
A boolean controlling whether determinism should be traded for
performance by allowing elements to be produced out of order.  If
`sloppy` is `None`, the <a href="../../../tf/data/Options.md#experimental_deterministic"><code>tf.data.Options.experimental_deterministic</code></a>
dataset option (`True` by default) is used to decide whether to enforce a
deterministic order.
</td>
</tr><tr>
<td>
`buffer_output_elements`
</td>
<td>
The number of elements each iterator being
interleaved should buffer (similar to the `.prefetch()` transformation for
each interleaved iterator).
</td>
</tr><tr>
<td>
`prefetch_input_elements`
</td>
<td>
The number of input elements to transform to
iterators before they are needed for interleaving.
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

