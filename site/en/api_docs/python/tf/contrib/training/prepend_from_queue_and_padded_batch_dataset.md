page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.prepend_from_queue_and_padded_batch_dataset

``` python
tf.contrib.training.prepend_from_queue_and_padded_batch_dataset(
    batch_size,
    padding_values=None,
    padded_shapes=None
)
```



Defined in [`tensorflow/contrib/training/python/training/tensor_queue_dataset.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/training/python/training/tensor_queue_dataset.py).

A transformation that prepends a queue to a `Dataset` and batches results.

A vector of handles to the queue is returned as the first component of the
associated iterator.  This vector can be passed to `enqueue_in_queue_dataset`
to add new elements to the queue.

Below is an example of how this dataset might be used to split incoming
variable-length sequences into "head" and "rest" parts, where "rest" parts
are re-enqueued back into the dataset.  A more realistic example would
perform some calculation on the "head" and modify some components of "rest"
with the result (before re-enqueueing).

```python
dataset = tf.data.Dataset.from_tensor_slices([2*x for x in range(10)])
# Make a dataset of variable-length vectors and their lengths.
dataset = dataset.map(lambda count: (count, tf.ones((count,))))
# Emit a queue we can prepend to, and counts/values as padded batch.
dataset = dataset.apply(
    tf.contrib.training.prepend_from_queue_and_padded_batch_dataset(
      batch_size=10))
dataset = dataset.prefetch(1)

iterator = dataset.make_one_shot_iterator()
queue, (count, padded_value) = iterator.get_next()

# Split the padded_value into two pieces: head and rest
rest_indices = tf.squeeze(tf.where(count > 3), axis=1)
bound = tf.minimum(3, tf.reduce_max(count))
value_head = padded_value[:, :bound]
count_rest = tf.gather(count - 3, rest_indices)
value_rest = tf.gather(padded_value[:, bound:], rest_indices)
queue_rest = tf.gather(queue, rest_indices)
enqueue_rest_op = tf.contrib.training.enqueue_in_queue_dataset(
  queue_rest, (count_rest, value_rest))
with tf.control_dependencies([enqueue_rest_op]):
  calculation = fn(value_head)

while True:  # Will raise OutOfRange when finished with all pieces.
  session.run(calculation)
```

#### Args:

* <b>`batch_size`</b>: `int64` scalar tensor.  The batch size to use when performing
    padded batching.
* <b>`padding_values`</b>: (optional) Nested tuple of scalar tensors.  If provided,
    the structure and dtypes of padding_values should match that of
    incoming dataset's `output_types`.
* <b>`padded_shapes`</b>: (optional) Nested tuple of `int64` vector tensors.
    If provided, the structure must match that of the incoming dataset's
    `output_types`.  If not provided, the incoming dataset's `output_shapes`
    is used.  Any unknown (`None` or `-1`) dimensions in the shapes are
    treated as being unique per-batch: for each batch time, an unknown
    dimension is replaced with the maximum given value of this dimension
    across all tensors for the given component in the batch.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.