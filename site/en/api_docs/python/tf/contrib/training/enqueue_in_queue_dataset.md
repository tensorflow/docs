page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.enqueue_in_queue_dataset

``` python
tf.contrib.training.enqueue_in_queue_dataset(
    queue,
    components
)
```



Defined in [`tensorflow/contrib/training/python/training/tensor_queue_dataset.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/training/python/training/tensor_queue_dataset.py).

Enqueue components into queue from `PrependFromQueueAndPaddedBatchDataset`.

The components' dtypes and shapes must be compatible with the `output_shapes`
attribute of the `dataset` created by
`prepend_from_queue_and_padded_batch_dataset`.  This operation supports both
non-batched and batched modes.

For more details, see the example in the docstring for
`prepend_from_queue_and_padded_batch_dataset`.

#### Args:

* <b>`queue`</b>: `variant` scalar or vector tensor.
    The tensor emitted by the first component of the iterator associated with
    `prepend_from_queue_and_padded_batch_dataset`.  If this is a scalar,
    then the `components` input tensors should not have a prepended batch
    dimension.
* <b>`components`</b>: Nested tuple of tensors, each with a leading batch dimension
    if `queue` is a vector.  The structure, dtypes, and shapes
    (excluding batch dimension) must match the nested tuples
    `dataset.output_types[1]` and `dataset.output_shapes[1]` (the non-queue
    output types and shapes) of the `dataset` emitted by
    the original `prepend_from_queue_and_padded_batch_dataset` call.


#### Returns:

An `Operation` that enqueues `components` into the dataset(s) associated
with entries of `queue`.