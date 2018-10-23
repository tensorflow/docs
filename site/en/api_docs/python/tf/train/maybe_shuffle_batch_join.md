

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.maybe_shuffle_batch_join

``` python
tf.train.maybe_shuffle_batch_join(
    tensors_list,
    batch_size,
    capacity,
    min_after_dequeue,
    keep_input,
    seed=None,
    enqueue_many=False,
    shapes=None,
    allow_smaller_final_batch=False,
    shared_name=None,
    name=None
)
```



Defined in [`tensorflow/python/training/input.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/training/input.py).

See the guide: [Inputs and Readers > Input pipeline](../../../../api_guides/python/io_ops#Input_pipeline)

Create batches by randomly shuffling conditionally-enqueued tensors.

See docstring in `shuffle_batch_join` for more details.

#### Args:

* <b>`tensors_list`</b>: A list of tuples or dictionaries of tensors to enqueue.
* <b>`batch_size`</b>: An integer. The new batch size pulled from the queue.
* <b>`capacity`</b>: An integer. The maximum number of elements in the queue.
* <b>`min_after_dequeue`</b>: Minimum number elements in the queue after a
    dequeue, used to ensure a level of mixing of elements.
* <b>`keep_input`</b>: A `bool` Tensor.  This tensor controls whether the input is
    added to the queue or not.  If it is a scalar and evaluates `True`, then
    `tensors` are all added to the queue. If it is a vector and `enqueue_many`
    is `True`, then each example is added to the queue only if the
    corresponding value in `keep_input` is `True`. This tensor essentially
    acts as a filtering mechanism.
* <b>`seed`</b>: Seed for the random shuffling within the queue.
* <b>`enqueue_many`</b>: Whether each tensor in `tensor_list_list` is a single
    example.
* <b>`shapes`</b>: (Optional) The shapes for each example.  Defaults to the
    inferred shapes for `tensors_list[i]`.
* <b>`allow_smaller_final_batch`</b>: (Optional) Boolean. If `True`, allow the final
    batch to be smaller if there are insufficient items left in the queue.
* <b>`shared_name`</b>: (optional). If set, this queue will be shared under the given
    name across multiple sessions.
* <b>`name`</b>: (Optional) A name for the operations.


#### Returns:

A list or dictionary of tensors with the same number and types as
`tensors_list[i]`.


#### Raises:

* <b>`ValueError`</b>: If the `shapes` are not specified, and cannot be
    inferred from the elements of `tensors_list`.



#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../tf/data"><code>tf.data</code></a> API to ingest data under eager execution.

