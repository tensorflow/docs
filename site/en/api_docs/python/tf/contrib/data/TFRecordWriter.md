page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.TFRecordWriter

## Class `TFRecordWriter`

Writes data to a TFRecord file.

Inherits From: [`TFRecordWriter`](../../../tf/data/experimental/TFRecordWriter)



Defined in [`contrib/data/python/ops/writers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/writers.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    filename,
    compression_type=None
)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/TFRecordWriter"><code>tf.data.experimental.TFRecordWriter(...)</code></a>.



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




