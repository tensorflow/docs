page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.TFRecordWriter

## Class `TFRecordWriter`

Inherits From: [`TFRecordWriter`](../../../tf/data/experimental/TFRecordWriter)



Defined in [`tensorflow/contrib/data/python/ops/writers.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/data/python/ops/writers.py).

Writes data to a TFRecord file.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    filename,
    compression_type=None
)
```

DEPRECATED FUNCTION

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.experimental.TFRecordWriter(...)`.



## Methods

<h3 id="write"><code>write</code></h3>

``` python
write(dataset)
```

Returns a <a href="../../../tf/Operation"><code>tf.Operation</code></a> to write a dataset to a file.

#### Args:

* <b>`dataset`</b>: a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> whose elements are to be written to a file


#### Returns:

A <a href="../../../tf/Operation"><code>tf.Operation</code></a> that, when run, writes contents of `dataset` to a file.



