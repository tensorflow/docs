page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.string_input_producer

Output strings (e.g. filenames) to a queue for an input pipeline. (deprecated)

### Aliases:

* `tf.compat.v1.train.string_input_producer`
* `tf.train.string_input_producer`

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



Defined in [`python/training/input.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/input.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../tf/data"><code>tf.data</code></a>. Use `tf.data.Dataset.from_tensor_slices(string_tensor).shuffle(tf.shape(input_tensor, out_type=tf.int64)[0]).repeat(num_epochs)`. If `shuffle=False`, omit the `.shuffle(...)`.

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

