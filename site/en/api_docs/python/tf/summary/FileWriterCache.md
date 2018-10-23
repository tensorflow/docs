


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.summary.FileWriterCache

### `class tf.summary.FileWriterCache`

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Cache for file writers.

This class caches file writers, one per directory.

## Methods

<h3 id="clear"><code>clear()</code></h3>

Clear cached summary writers. Currently only used for unit tests.

<h3 id="get"><code>get(logdir)</code></h3>

Returns the FileWriter for the specified directory.

#### Args:

* <b>`logdir`</b>: str, name of the directory.


#### Returns:

  A `FileWriter`.



## Class Members

<h3 id="__init__"><code>__init__</code></h3>



Defined in [`tensorflow/python/summary/writer/writer_cache.py`](https://www.tensorflow.org/code/tensorflow/python/summary/writer/writer_cache.py).

