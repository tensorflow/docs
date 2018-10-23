

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.summary.FileWriterCache

## Class `FileWriterCache`





Defined in [`tensorflow/python/summary/writer/writer_cache.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/summary/writer/writer_cache.py).

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Cache for file writers.

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



