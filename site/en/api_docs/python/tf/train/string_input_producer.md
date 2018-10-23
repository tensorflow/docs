

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.string_input_producer

``` python
tf.train.string_input_producer(
    string_tensor,
    num_epochs=None,
    shuffle=True,
    seed=None,
    capacity=32,
    shared_name=None,
    name=None,
    cancel_op=None
)
```



Defined in [`tensorflow/python/training/input.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/training/input.py).

See the guides: [Inputs and Readers > Input pipeline](../../../../api_guides/python/io_ops#Input_pipeline), [Reading data > `QueueRunner`](../../../../api_guides/python/reading_data#_QueueRunner_)

Output strings (e.g. filenames) to a queue for an input pipeline.

Note: if `num_epochs` is not `None`, this function creates local counter
`epochs`. Use `local_variables_initializer()` to initialize local variables.

#### Args:

* <b>`string_tensor`</b>: A 1-D string tensor with the strings to produce.
* <b>`num_epochs`</b>: An integer (optional). If specified, `string_input_producer`
    produces each string from `string_tensor` `num_epochs` times before
    generating an `OutOfRange` error. If not specified,
    `string_input_producer` can cycle through the strings in `string_tensor`
    an unlimited number of times.
* <b>`shuffle`</b>: Boolean. If true, the strings are randomly shuffled within each
    epoch.
* <b>`seed`</b>: An integer (optional). Seed used if shuffle == True.
* <b>`capacity`</b>: An integer. Sets the queue capacity.
* <b>`shared_name`</b>: (optional). If set, this queue will be shared under the given
    name across multiple sessions. All sessions open to the device which has
    this queue will be able to access it via the shared_name. Using this in
    a distributed setting means each name will only be seen by one of the
    sessions which has access to this operation.
* <b>`name`</b>: A name for the operations (optional).
* <b>`cancel_op`</b>: Cancel op for the queue (optional).


#### Returns:

A queue with the output strings.  A `QueueRunner` for the Queue
is added to the current `Graph`'s `QUEUE_RUNNER` collection.


#### Raises:

* <b>`ValueError`</b>: If the string_tensor is a null Python list.  At runtime,
  will fail with an assertion if string_tensor becomes a null tensor.



#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../tf/data"><code>tf.data</code></a> API to ingest data under eager execution.

