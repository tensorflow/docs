

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.read_batch_record_features

``` python
tf.contrib.learn.read_batch_record_features(
    file_pattern,
    batch_size,
    features,
    randomize_input=True,
    num_epochs=None,
    queue_capacity=10000,
    reader_num_threads=1,
    name='dequeue_record_examples'
)
```



Defined in [`tensorflow/contrib/learn/python/learn/learn_io/graph_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/learn/python/learn/learn_io/graph_io.py).

See the guide: [Learn (contrib) > Input processing](../../../../../api_guides/python/contrib.learn#Input_processing)

Reads TFRecord, queues, batches and parses `Example` proto.

See more detailed description in `read_examples`.

#### Args:

* <b>`file_pattern`</b>: List of files or patterns of file paths containing
      `Example` records. See `tf.gfile.Glob` for pattern rules.
* <b>`batch_size`</b>: An int or scalar `Tensor` specifying the batch size to use.
* <b>`features`</b>: A `dict` mapping feature keys to `FixedLenFeature` or
    `VarLenFeature` values.
* <b>`randomize_input`</b>: Whether the input should be randomized.
* <b>`num_epochs`</b>: Integer specifying the number of times to read through the
    dataset. If None, cycles through the dataset forever. NOTE - If specified,
    creates a variable that must be initialized, so call
    tf.local_variables_initializer() and run the op in a session.
* <b>`queue_capacity`</b>: Capacity for input queue.
* <b>`reader_num_threads`</b>: The number of threads to read examples. In order to have
    predictable and repeatable order of reading and enqueueing, such as in
    prediction and evaluation mode, `reader_num_threads` should be 1.
* <b>`name`</b>: Name of resulting op.


#### Returns:

A dict of `Tensor` or `SparseTensor` objects for each in `features`.


#### Raises:

* <b>`ValueError`</b>: for invalid inputs.