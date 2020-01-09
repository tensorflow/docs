page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.FileWriterCache


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/writer/writer_cache.py#L29-L64">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `FileWriterCache`

Cache for file writers.



<!-- Placeholder for "Used in" -->

This class caches file writers, one per directory.

## Methods

<h3 id="clear"><code>clear</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/writer/writer_cache.py#L40-L48">View source</a>

``` python
@staticmethod
clear()
```

Clear cached summary writers. Currently only used for unit tests.


<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/writer/writer_cache.py#L50-L64">View source</a>

``` python
@staticmethod
get(logdir)
```

Returns the FileWriter for the specified directory.


#### Args:


* <b>`logdir`</b>: str, name of the directory.


#### Returns:

A `FileWriter`.
