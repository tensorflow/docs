description: Creates a dataset that applies f to the outputs of input_dataset.

robots: noindex

# tf.raw_ops.ParallelInterleaveDatasetV3

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that applies `f` to the outputs of `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParallelInterleaveDatasetV3`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParallelInterleaveDatasetV3(
    input_dataset, other_arguments, cycle_length, block_length, num_parallel_calls,
    f, output_types, output_shapes, deterministic='default', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The resulting dataset is similar to the `InterleaveDataset`, except that the
dataset will fetch records from the interleaved datasets in parallel.

The <a href="../../tf/data.md"><code>tf.data</code></a> Python API creates instances of this op from
<a href="../../tf/data/Dataset.md#interleave"><code>Dataset.interleave()</code></a> when the `num_parallel_calls` parameter of that method
is set to any value other than `None`.

By default, the output of this dataset will be deterministic, which may result
in the dataset blocking if the next data item to be returned isn't available.
In order to avoid head-of-line blocking, one can either set the `deterministic`
attribute to "false", or leave it as "default" and set the
`experimental_deterministic` parameter of <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a> to `False`.
This can improve performance at the expense of non-determinism.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
Dataset that produces a stream of arguments for the function `f`.
</td>
</tr><tr>
<td>
`other_arguments`
</td>
<td>
A list of `Tensor` objects.
Additional arguments to pass to `f` beyond those produced by `input_dataset`.
Evaluated once when the dataset is instantiated.
</td>
</tr><tr>
<td>
`cycle_length`
</td>
<td>
A `Tensor` of type `int64`.
Number of datasets (each created by applying `f` to the elements of
`input_dataset`) among which the `ParallelInterleaveDatasetV2` will cycle in a
round-robin fashion.
</td>
</tr><tr>
<td>
`block_length`
</td>
<td>
A `Tensor` of type `int64`.
Number of elements at a time to produce from each interleaved invocation of a
dataset returned by `f`.
</td>
</tr><tr>
<td>
`num_parallel_calls`
</td>
<td>
A `Tensor` of type `int64`.
Determines the number of threads that should be used for fetching data from
input datasets in parallel. The Python API <a href="../../tf/data/experimental.md#AUTOTUNE"><code>tf.data.experimental.AUTOTUNE</code></a>
constant can be used to indicate that the level of parallelism should be autotuned.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun.
A function mapping elements of `input_dataset`, concatenated with
`other_arguments`, to a Dataset variant that contains elements matching
`output_types` and `output_shapes`.
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
`deterministic`
</td>
<td>
An optional `string`. Defaults to `"default"`.
A string indicating the op-level determinism to use. Deterministic controls
whether the interleave is allowed to return elements out of order if the next
element to be returned isn't available, but a later element is. Options are
"true", "false", and "default". "default" indicates that determinism should be
decided by the `experimental_deterministic` parameter of <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a>.
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

