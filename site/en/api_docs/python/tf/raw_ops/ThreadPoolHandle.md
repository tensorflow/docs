description: Creates a dataset that uses a custom thread pool to compute input_dataset.

robots: noindex

# tf.raw_ops.ThreadPoolHandle

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that uses a custom thread pool to compute `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ThreadPoolHandle`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ThreadPoolHandle(
    num_threads, display_name, max_intra_op_parallelism=1, container='',
    shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_threads`
</td>
<td>
An `int`. The number of threads in the thread pool.
</td>
</tr><tr>
<td>
`display_name`
</td>
<td>
A `string`.
A human-readable name for the threads that may be visible in some
visualizations.
threadpool.
</td>
</tr><tr>
<td>
`max_intra_op_parallelism`
</td>
<td>
An optional `int`. Defaults to `1`.
The maximum degree of parallelism to use within operations that execute on this
threadpool.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
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
A `Tensor` of type `resource`.
</td>
</tr>

</table>

