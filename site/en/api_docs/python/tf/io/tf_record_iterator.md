page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.tf_record_iterator

An iterator that read the records from a TFRecords file. (deprecated)

### Aliases:

* `tf.compat.v1.io.tf_record_iterator`
* `tf.compat.v1.python_io.tf_record_iterator`
* `tf.io.tf_record_iterator`
* `tf.python_io.tf_record_iterator`

``` python
tf.io.tf_record_iterator(
    path,
    options=None
)
```



Defined in [`python/lib/io/tf_record.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/tf_record.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use eager execution and: 
<a href="../../tf/data/TFRecordDataset"><code>tf.data.TFRecordDataset(path)</code></a>

#### Args:


* <b>`path`</b>: The path to the TFRecords file.
* <b>`options`</b>: (optional) A TFRecordOptions object.


#### Yields:

Strings.



#### Raises:


* <b>`IOError`</b>: If `path` cannot be opened for reading.