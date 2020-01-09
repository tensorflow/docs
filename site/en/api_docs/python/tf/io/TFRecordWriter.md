page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.TFRecordWriter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L192-L246">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TFRecordWriter`

A class to write records to a TFRecords file.



### Aliases:

* Class `tf.compat.v1.io.TFRecordWriter`
* Class `tf.compat.v1.python_io.TFRecordWriter`
* Class `tf.compat.v2.io.TFRecordWriter`


### Used in the tutorials:

* [TFRecord and tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)



This class implements `__enter__` and `__exit__`, and can be used
in `with` blocks like a normal file.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L200-L218">View source</a>

``` python
__init__(
    path,
    options=None
)
```

Opens file `path` and creates a `TFRecordWriter` writing to it.


#### Args:


* <b>`path`</b>: The path to the TFRecords file.
* <b>`options`</b>: (optional) String specifying compression type,
    `TFRecordCompressionType`, or `TFRecordOptions` object.


#### Raises:


* <b>`IOError`</b>: If `path` cannot be opened for writing.
* <b>`ValueError`</b>: If valid compression_type can't be determined from `options`.



## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L221-L223">View source</a>

``` python
__enter__()
```

Enter a `with` block.


<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L225-L227">View source</a>

``` python
__exit__(
    unused_type,
    unused_value,
    unused_traceback
)
```

Exit a `with` block, closing the file.


<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L243-L246">View source</a>

``` python
close()
```

Close the file.


<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L238-L241">View source</a>

``` python
flush()
```

Flush the file.


<h3 id="write"><code>write</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/tf_record.py#L229-L236">View source</a>

``` python
write(record)
```

Write a string record to the file.


#### Args:


* <b>`record`</b>: str
