page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.range_input_producer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/input.py#L280-L319">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Produces the integers from 0 to limit-1 in a queue. (deprecated)

``` python
tf.compat.v1.train.range_input_producer(
    limit,
    num_epochs=None,
    shuffle=True,
    seed=None,
    capacity=32,
    shared_name=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data"><code>tf.data</code></a>. Use `tf.data.Dataset.range(limit).shuffle(limit).repeat(num_epochs)`. If `shuffle=False`, omit the `.shuffle(...)`.

Note: if `num_epochs` is not `None`, this function creates local counter
`epochs`. Use `local_variables_initializer()` to initialize local variables.

#### Args:


* <b>`limit`</b>: An int32 scalar tensor.
* <b>`num_epochs`</b>: An integer (optional). If specified, `range_input_producer`
  produces each integer `num_epochs` times before generating an
  OutOfRange error. If not specified, `range_input_producer` can cycle
  through the integers an unlimited number of times.
* <b>`shuffle`</b>: Boolean. If true, the integers are randomly shuffled within each
  epoch.
* <b>`seed`</b>: An integer (optional). Seed used if shuffle == True.
* <b>`capacity`</b>: An integer. Sets the queue capacity.
* <b>`shared_name`</b>: (optional). If set, this queue will be shared under the given
  name across multiple sessions.
* <b>`name`</b>: A name for the operations (optional).


#### Returns:

A Queue with the output integers.  A `QueueRunner` for the Queue
is added to the current `Graph`'s `QUEUE_RUNNER` collection.




#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../../../tf/data"><code>tf.data</code></a> API to ingest data under eager execution.
