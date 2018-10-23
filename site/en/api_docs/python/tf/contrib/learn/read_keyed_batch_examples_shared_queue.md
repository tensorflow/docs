

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.read_keyed_batch_examples_shared_queue

``` python
read_keyed_batch_examples_shared_queue(
    file_pattern,
    batch_size,
    reader,
    randomize_input=True,
    num_epochs=None,
    queue_capacity=10000,
    num_threads=1,
    read_batch_size=1,
    parse_fn=None,
    name=None,
    seed=None
)
```



Defined in [`tensorflow/contrib/learn/python/learn/learn_io/graph_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/learn/python/learn/learn_io/graph_io.py).

Adds operations to read, queue, batch `Example` protos.

Given file pattern (or list of files), will setup a shared queue for file
names, setup a worker queue that pulls from the shared queue, read `Example`
protos using provided `reader`, use batch queue to create batches of examples
of size `batch_size`. This provides at most once visit guarantees. Note that
this only works if the parameter servers are not pre-empted or restarted or
the session is not restored from a checkpoint since the state of a queue
is not checkpointed and we will end up restarting from the entire list of
files.

All queue runners are added to the queue runners collection, and may be
started via `start_queue_runners`.

All ops are added to the default graph.

Use `parse_fn` if you need to do parsing / processing on single examples.

#### Args:

* <b>`file_pattern`</b>: List of files or patterns of file paths containing
      `Example` records. See `tf.gfile.Glob` for pattern rules.
* <b>`batch_size`</b>: An int or scalar `Tensor` specifying the batch size to use.
* <b>`reader`</b>: A function or class that returns an object with
    `read` method, (filename tensor) -> (example tensor).
* <b>`randomize_input`</b>: Whether the input should be randomized.
* <b>`num_epochs`</b>: Integer specifying the number of times to read through the
    dataset. If `None`, cycles through the dataset forever.
    NOTE - If specified, creates a variable that must be initialized, so call
    `tf.local_variables_initializer()` and run the op in a session.
* <b>`queue_capacity`</b>: Capacity for input queue.
* <b>`num_threads`</b>: The number of threads enqueuing examples.
* <b>`read_batch_size`</b>: An int or scalar `Tensor` specifying the number of
    records to read at once.
* <b>`parse_fn`</b>: Parsing function, takes `Example` Tensor returns parsed
    representation. If `None`, no parsing is done.
* <b>`name`</b>: Name of resulting op.
* <b>`seed`</b>: An integer (optional). Seed used if randomize_input == True.


#### Returns:

Returns tuple of:
- `Tensor` of string keys.
- String `Tensor` of batched `Example` proto.


#### Raises:

* <b>`ValueError`</b>: for invalid inputs.