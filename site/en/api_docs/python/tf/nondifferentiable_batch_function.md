page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nondifferentiable_batch_function


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nondifferentiable_batch_function">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/batch_ops.py#L31-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Batches the computation done by the decorated function.

### Aliases:

* <a href="/api_docs/python/tf/nondifferentiable_batch_function"><code>tf.compat.v1.nondifferentiable_batch_function</code></a>
* <a href="/api_docs/python/tf/nondifferentiable_batch_function"><code>tf.compat.v2.nondifferentiable_batch_function</code></a>
* <a href="/api_docs/python/tf/nondifferentiable_batch_function"><code>tf.contrib.batching.batch_function</code></a>


``` python
tf.nondifferentiable_batch_function(
    num_batch_threads,
    max_batch_size,
    batch_timeout_micros,
    allowed_batch_sizes=None,
    max_enqueued_batches=10,
    autograph=True
)
```



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

#### Args:


* <b>`num_batch_threads`</b>: Number of scheduling threads for processing batches
 of work. Determines the number of batches processed in parallel.
* <b>`max_batch_size`</b>: Batch sizes will never be bigger than this.
* <b>`batch_timeout_micros`</b>: Maximum number of microseconds to wait before
 outputting an incomplete batch.
* <b>`allowed_batch_sizes`</b>: Optional list of allowed batch sizes. If left empty,
 does nothing. Otherwise, supplies a list of batch sizes, causing the op
 to pad batches up to one of those sizes. The entries must increase
 monotonically, and the final entry must equal max_batch_size.
* <b>`max_enqueued_batches`</b>: The maximum depth of the batch queue. Defaults to 10.
* <b>`autograph`</b>: Whether to use autograph to compile python and eager style code
 for efficient graph-mode execution.


#### Returns:

The decorated function will return the unbatched computation output Tensors.
