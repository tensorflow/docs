description: Batches the computation done by the decorated function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nondifferentiable_batch_function" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nondifferentiable_batch_function

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/batch_ops.py#L31-L122">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batches the computation done by the decorated function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nondifferentiable_batch_function`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nondifferentiable_batch_function(
    num_batch_threads, max_batch_size, batch_timeout_micros,
    allowed_batch_sizes=None, max_enqueued_batches=10, autograph=(True),
    enable_large_batch_splitting=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

So, for example, in the following code

```python
@batch_function(1, 2, 3)
def layer(a):
  return tf.matmul(a, a)

b = layer(w)
```

if more than one session.run call is simultaneously trying to compute `b`
the values of `w` will be gathered, non-deterministically concatenated
along the first axis, and only one thread will run the computation. See the
documentation of the `Batch` op for more details.

Assumes that all arguments of the decorated function are Tensors which will
be batched along their first dimension.

SparseTensor is not supported. The return value of the decorated function
must be a Tensor or a list/tuple of Tensors.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_batch_threads`
</td>
<td>
Number of scheduling threads for processing batches
of work. Determines the number of batches processed in parallel.
</td>
</tr><tr>
<td>
`max_batch_size`
</td>
<td>
Batch sizes will never be bigger than this.
</td>
</tr><tr>
<td>
`batch_timeout_micros`
</td>
<td>
Maximum number of microseconds to wait before
outputting an incomplete batch.
</td>
</tr><tr>
<td>
`allowed_batch_sizes`
</td>
<td>
Optional list of allowed batch sizes. If left empty,
does nothing. Otherwise, supplies a list of batch sizes, causing the op
to pad batches up to one of those sizes. The entries must increase
monotonically, and the final entry must equal max_batch_size.
</td>
</tr><tr>
<td>
`max_enqueued_batches`
</td>
<td>
The maximum depth of the batch queue. Defaults to 10.
</td>
</tr><tr>
<td>
`autograph`
</td>
<td>
Whether to use autograph to compile python and eager style code
for efficient graph-mode execution.
</td>
</tr><tr>
<td>
`enable_large_batch_splitting`
</td>
<td>
The value of this option doesn't affect
processing output given the same input; it affects implementation details
as stated below: 1. Improve batching efficiency by eliminating unnecessary
adding. 2.`max_batch_size` specifies the limit of input and
`allowed_batch_sizes` specifies the limit of a task to be processed. API
user can give an input of size 128 when 'max_execution_batch_size'
is 32 -> implementation can split input of 128 into 4 x 32, schedule
concurrent processing, and then return concatenated results corresponding
to 128.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The decorated function will return the unbatched computation output Tensors.
</td>
</tr>

</table>

