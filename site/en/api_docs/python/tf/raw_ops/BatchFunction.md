description: Batches all the inputs tensors to the computation done by the function.

robots: noindex

# tf.raw_ops.BatchFunction

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Batches all the inputs tensors to the computation done by the function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BatchFunction`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BatchFunction(
    in_tensors, captured_tensors, f, num_batch_threads, max_batch_size,
    batch_timeout_micros, Tout, max_enqueued_batches=10, allowed_batch_sizes=[],
    container='', shared_name='', batching_queue='',
    enable_large_batch_splitting=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

So, for example, in the following code

  ```python

  # This input will be captured.
  y = tf.placeholder_with_default(1.0, shape=[])

  @tf.Defun(tf.float32)
  def computation(a):
    return tf.matmul(a, a) + y

  b = gen_batch_ops.batch_function(
          f=computation
          in_tensors=[a],
          captured_tensors=computation.captured_inputs,
          Tout=[o.type for o in computation.definition.signature.output_arg],
          num_batch_threads=1,
          max_batch_size=10,
          batch_timeout_micros=100000,  # 100ms
          allowed_batch_sizes=[3, 10],
          batching_queue="")
  ```

If more than one session.run call is simultaneously trying to compute `b`
the values of `a` will be gathered, non-deterministically concatenated
along the first axis, and only one thread will run the computation.

Assumes that all arguments of the function are Tensors which will be batched
along their first dimension.

Arguments that are captured, are not batched. The session.run call which does
the concatenation, will use the values of the captured tensors available to it.
Therefore, typical uses of captured tensors should involve values which remain
unchanged across session.run calls. Inference is a good example of this.

SparseTensor is not supported. The return value of the decorated function
must be a Tensor or a list/tuple of Tensors.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`in_tensors`
</td>
<td>
A list of `Tensor` objects. The tensors to be batched.
</td>
</tr><tr>
<td>
`captured_tensors`
</td>
<td>
A list of `Tensor` objects.
The tensors which are captured in the function, and don't need
to be batched.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun.
</td>
</tr><tr>
<td>
`num_batch_threads`
</td>
<td>
An `int`.
Number of scheduling threads for processing batches of work.
Determines the number of batches processed in parallel.
</td>
</tr><tr>
<td>
`max_batch_size`
</td>
<td>
An `int`. Batch sizes will never be bigger than this.
</td>
</tr><tr>
<td>
`batch_timeout_micros`
</td>
<td>
An `int`.
Maximum number of microseconds to wait before outputting
an incomplete batch.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
the types of the output tensors.
</td>
</tr><tr>
<td>
`max_enqueued_batches`
</td>
<td>
An optional `int`. Defaults to `10`.
Maximum number of batches enqueued. Default: 10.
</td>
</tr><tr>
<td>
`allowed_batch_sizes`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
Optional list of allowed batch sizes. If left empty, does
nothing. Otherwise, supplies a list of batch sizes, causing the op to pad
batches up to one of those sizes. The entries must increase monotonically.
If enable_large_batch_splitting is false (i.e., large-input-split is not
enabled) the final entry must equal max_batch_size.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
Controls the scope of sharing of this batch.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
Concurrently running instances of batch in the same device with the
same container and shared_name will batch their elements together. If left
empty, the op name will be used as the shared name.
</td>
</tr><tr>
<td>
`batching_queue`
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`enable_large_batch_splitting`
</td>
<td>
An optional `bool`. Defaults to `False`.
input with a large size (i.e., larger than the largest value of
`allowed_batch_sizes`) will be splitted into multiple batches with batch size.
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
A list of `Tensor` objects of type `Tout`.
</td>
</tr>

</table>

