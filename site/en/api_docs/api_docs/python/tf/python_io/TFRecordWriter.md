

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.python_io.TFRecordWriter

## Class `TFRecordWriter`





Defined in [`tensorflow/python/lib/io/tf_record.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/lib/io/tf_record.py).

See the guides: [Data IO (Python functions)](../../../../api_guides/python/python_io), [Reading data > Reading from files](../../../../api_guides/python/reading_data#Reading_from_files)

A class to write records to a TFRecords file.

This class implements `__enter__` and `__exit__`, and can be used
in `with` blocks like a normal file.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    path,
    options=None
)
```

Opens file `path` and creates a `TFRecordWriter` writing to it.

#### Args:

* <b>`path`</b>: The path to the TFRecords file.
* <b>`options`</b>: (optional) A TFRecordOptions object.


#### Raises:

* <b>`IOError`</b>: If `path` cannot be opened for writing.

<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```

Enter a `with` block.

<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    unused_type,
    unused_value,
    unused_traceback
)
```

Exit a `with` block, closing the file.

<h3 id="close"><code>close</code></h3>

``` python
close()
```

Close the file.

<h3 id="flush"><code>flush</code></h3>

``` python
flush()
```

Flush the file.

<h3 id="write"><code>write</code></h3>

``` python
write(record)
```

Write a string record to the file.

#### Args:

* <b>`record`</b>: str



