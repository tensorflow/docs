page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.maybe_shuffle_batch


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/input.py#L1350-L1411">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates batches by randomly shuffling conditionally-enqueued tensors. (deprecated)

``` python
tf.compat.v1.train.maybe_shuffle_batch(
    tensors,
    batch_size,
    capacity,
    min_after_dequeue,
    keep_input,
    num_threads=1,
    seed=None,
    enqueue_many=False,
    shapes=None,
    allow_smaller_final_batch=False,
    shared_name=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data"><code>tf.data</code></a>. Use `tf.data.Dataset.filter(...).shuffle(min_after_dequeue).batch(batch_size)`.

See docstring in `shuffle_batch` for more details.

#### Args:


* <b>`tensors`</b>: The list or dictionary of tensors to enqueue.
* <b>`batch_size`</b>: The new batch size pulled from the queue.
* <b>`capacity`</b>: An integer. The maximum number of elements in the queue.
* <b>`min_after_dequeue`</b>: Minimum number elements in the queue after a
  dequeue, used to ensure a level of mixing of elements.
* <b>`keep_input`</b>: A `bool` Tensor.  This tensor controls whether the input is
  added to the queue or not.  If it is a scalar and evaluates `True`, then
  `tensors` are all added to the queue. If it is a vector and `enqueue_many`
  is `True`, then each example is added to the queue only if the
  corresponding value in `keep_input` is `True`. This tensor essentially
  acts as a filtering mechanism.
* <b>`num_threads`</b>: The number of threads enqueuing `tensor_list`.
* <b>`seed`</b>: Seed for the random shuffling within the queue.
* <b>`enqueue_many`</b>: Whether each tensor in `tensor_list` is a single example.
* <b>`shapes`</b>: (Optional) The shapes for each example.  Defaults to the
  inferred shapes for `tensor_list`.
* <b>`allow_smaller_final_batch`</b>: (Optional) Boolean. If `True`, allow the final
  batch to be smaller if there are insufficient items left in the queue.
* <b>`shared_name`</b>: (Optional) If set, this queue will be shared under the given
  name across multiple sessions.
* <b>`name`</b>: (Optional) A name for the operations.


#### Returns:

A list or dictionary of tensors with the types as `tensors`.



#### Raises:


* <b>`ValueError`</b>: If the `shapes` are not specified, and cannot be
  inferred from the elements of `tensors`.



#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../../../tf/data"><code>tf.data</code></a> API to ingest data under eager execution.
