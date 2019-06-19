

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.batching.batch_function

``` python
tf.contrib.batching.batch_function(
    num_batch_threads,
    max_batch_size,
    batch_timeout_micros,
    allowed_batch_sizes=None,
    grad_timeout_micros=(60 * 1000 * 1000),
    unbatch_timeout_micros=(60 * 1000 * 1000),
    max_enqueued_batches=10
)
```



Defined in [`tensorflow/contrib/batching/python/ops/batch_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/batching/python/ops/batch_ops.py).

Batches the computation done by the decorated function.

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
* <b>`grad_timeout_micros`</b>: The timeout to use for the gradient. See the
   documentation of the unbatch op for more details. Defaults to 60s.
* <b>`unbatch_timeout_micros`</b>: The timeout to use for unbatching. See the
   documentation of the unbatch op for more details. Defaults to 60s.
* <b>`max_enqueued_batches`</b>: The maximum depth of the batch queue. Defaults to 10.


#### Returns:

The decorated function will return the unbatched computation output Tensors.