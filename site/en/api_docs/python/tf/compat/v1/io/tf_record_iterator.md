page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.io.tf_record_iterator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L153-L186">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



An iterator that read the records from a TFRecords file. (deprecated)

### Aliases:

* `tf.compat.v1.python_io.tf_record_iterator`


``` python
tf.compat.v1.io.tf_record_iterator(
    path,
    options=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use eager execution and: 
<a href="../../../../tf/data/TFRecordDataset"><code>tf.data.TFRecordDataset(path)</code></a>

#### Args:


* <b>`path`</b>: The path to the TFRecords file.
* <b>`options`</b>: (optional) A TFRecordOptions object.


#### Yields:

Strings.



#### Raises:


* <b>`IOError`</b>: If `path` cannot be opened for reading.
