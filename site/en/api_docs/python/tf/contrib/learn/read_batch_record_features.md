page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.read_batch_record_features


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/learn_io/graph_io.py#L837-L882">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Reads TFRecord, queues, batches and parses `Example` proto. (deprecated)

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



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.data.

See more detailed description in `read_examples`.

#### Args:


* <b>`file_pattern`</b>: List of files or patterns of file paths containing
    `Example` records. See <a href="../../../tf/io/gfile/glob"><code>tf.io.gfile.glob</code></a> for pattern rules.
* <b>`batch_size`</b>: An int or scalar `Tensor` specifying the batch size to use.
* <b>`features`</b>: A `dict` mapping feature keys to `FixedLenFeature` or
  `VarLenFeature` values.
* <b>`randomize_input`</b>: Whether the input should be randomized.
* <b>`num_epochs`</b>: Integer specifying the number of times to read through the
  dataset. If None, cycles through the dataset forever. NOTE - If specified,
  creates a variable that must be initialized, so call
  tf.compat.v1.local_variables_initializer() and run the op in a session.
* <b>`queue_capacity`</b>: Capacity for input queue.
* <b>`reader_num_threads`</b>: The number of threads to read examples. In order to have
  predictable and repeatable order of reading and enqueueing, such as in
  prediction and evaluation mode, `reader_num_threads` should be 1.
* <b>`name`</b>: Name of resulting op.


#### Returns:

A dict of `Tensor` or `SparseTensor` objects for each in `features`.



#### Raises:


* <b>`ValueError`</b>: for invalid inputs.
