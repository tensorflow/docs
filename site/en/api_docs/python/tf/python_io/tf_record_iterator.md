

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.python_io.tf_record_iterator

### `tf.python_io.tf_record_iterator`

``` python
tf_record_iterator(
    path,
    options=None
)
```



Defined in [`tensorflow/python/lib/io/tf_record.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/lib/io/tf_record.py).

See the guide: [Data IO (Python functions)](../../../../api_guides/python/python_io)

An iterator that read the records from a TFRecords file.

#### Args:

* <b>`path`</b>: The path to the TFRecords file.
* <b>`options`</b>: (optional) A TFRecordOptions object.


#### Yields:

  Strings.


#### Raises:

* <b>`IOError`</b>: If `path` cannot be opened for reading.