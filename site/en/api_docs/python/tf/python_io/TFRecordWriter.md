


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.python_io.TFRecordWriter

### `class tf.python_io.TFRecordWriter`

See the guide: [Data IO (Python functions)](../../../../api_guides/python/python_io)

A class to write records to a TFRecords file.

This class implements `__enter__` and `__exit__`, and can be used
in `with` blocks like a normal file.

## Methods

<h3 id="__init__"><code>__init__(path, options=None)</code></h3>

Opens file `path` and creates a `TFRecordWriter` writing to it.

#### Args:

* <b>`path`</b>: The path to the TFRecords file.
* <b>`options`</b>: (optional) A TFRecordOptions object.


#### Raises:

* <b>`IOError`</b>: If `path` cannot be opened for writing.

<h3 id="close"><code>close()</code></h3>

Close the file.

<h3 id="write"><code>write(record)</code></h3>

Write a string record to the file.

#### Args:

* <b>`record`</b>: str





Defined in [`tensorflow/python/lib/io/tf_record.py`](https://www.tensorflow.org/code/tensorflow/python/lib/io/tf_record.py).

