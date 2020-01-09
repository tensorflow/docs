page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.read_keyed_batch_features


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/learn_io/graph_io.py#L464-L550">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds operations to read, queue, batch and parse `Example` protos. (deprecated)

``` python
tf.contrib.learn.read_keyed_batch_features(
    file_pattern,
    batch_size,
    features,
    reader,
    randomize_input=True,
    num_epochs=None,
    queue_capacity=10000,
    reader_num_threads=1,
    feature_queue_capacity=100,
    num_enqueue_threads=2,
    parse_fn=None,
    name=None,
    read_batch_size=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.data.

Given file pattern (or list of files), will setup a queue for file names,
read `Example` proto using provided `reader`, use batch queue to create
batches of examples of size `batch_size` and parse example given `features`
specification.

All queue runners are added to the queue runners collection, and may be
started via `start_queue_runners`.

All ops are added to the default graph.

#### Args:


* <b>`file_pattern`</b>: List of files or patterns of file paths containing
    `Example` records. See <a href="../../../tf/io/gfile/glob"><code>tf.io.gfile.glob</code></a> for pattern rules.
* <b>`batch_size`</b>: An int or scalar `Tensor` specifying the batch size to use.
* <b>`features`</b>: A `dict` mapping feature keys to `FixedLenFeature` or
  `VarLenFeature` values.
* <b>`reader`</b>: A function or class that returns an object with
  `read` method, (filename tensor) -> (example tensor).
* <b>`randomize_input`</b>: Whether the input should be randomized.
* <b>`num_epochs`</b>: Integer specifying the number of times to read through the
  dataset. If None, cycles through the dataset forever. NOTE - If specified,
  creates a variable that must be initialized, so call
  tf.compat.v1.local_variables_initializer() and run the op in a session.
* <b>`queue_capacity`</b>: Capacity for input queue.
* <b>`reader_num_threads`</b>: The number of threads to read examples. In order to have
  predictable and repeatable order of reading and enqueueing, such as in
  prediction and evaluation mode, `reader_num_threads` should be 1.
* <b>`feature_queue_capacity`</b>: Capacity of the parsed features queue.
* <b>`num_enqueue_threads`</b>: Number of threads to enqueue the parsed example queue.
  Using multiple threads to enqueue the parsed example queue helps maintain
  a full queue when the subsequent computations overall are cheaper than
  parsing. In order to have predictable and repeatable order of reading and
  enqueueing, such as in prediction and evaluation mode,
  `num_enqueue_threads` should be 1.
* <b>`parse_fn`</b>: Parsing function, takes `Example` Tensor returns parsed
  representation. If `None`, no parsing is done.
* <b>`name`</b>: Name of resulting op.
* <b>`read_batch_size`</b>: An int or scalar `Tensor` specifying the number of
  records to read at once. If `None`, defaults to `batch_size`.


#### Returns:

Returns tuple of:
- `Tensor` of string keys.
- A dict of `Tensor` or `SparseTensor` objects for each in `features`.



#### Raises:


* <b>`ValueError`</b>: for invalid inputs.
