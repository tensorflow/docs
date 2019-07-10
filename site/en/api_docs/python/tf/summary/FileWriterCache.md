page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.FileWriterCache

## Class `FileWriterCache`

Cache for file writers.



### Aliases:

* Class `tf.compat.v1.summary.FileWriterCache`
* Class `tf.summary.FileWriterCache`



Defined in [`python/summary/writer/writer_cache.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/summary/writer/writer_cache.py).

<!-- Placeholder for "Used in" -->

This class caches file writers, one per directory.

## Methods

<h3 id="clear"><code>clear</code></h3>

``` python
@staticmethod
clear()
```

Clear cached summary writers. Currently only used for unit tests.


<h3 id="get"><code>get</code></h3>

``` python
@staticmethod
get(logdir)
```

Returns the FileWriter for the specified directory.


#### Args:


* <b>`logdir`</b>: str, name of the directory.


#### Returns:

A `FileWriter`.




