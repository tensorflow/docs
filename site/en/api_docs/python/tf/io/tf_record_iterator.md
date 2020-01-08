page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.tf_record_iterator

### Aliases:

* `tf.io.tf_record_iterator`
* `tf.python_io.tf_record_iterator`

``` python
tf.io.tf_record_iterator(
    path,
    options=None
)
```



Defined in [`tensorflow/python/lib/io/tf_record.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/lib/io/tf_record.py).

An iterator that read the records from a TFRecords file.

#### Args:

* <b>`path`</b>: The path to the TFRecords file.
* <b>`options`</b>: (optional) A TFRecordOptions object.


#### Yields:

Strings.


#### Raises:

* <b>`IOError`</b>: If `path` cannot be opened for reading.