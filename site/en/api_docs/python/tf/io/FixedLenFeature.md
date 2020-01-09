page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.FixedLenFeature


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/FixedLenFeature">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/parsing_ops.py#L136-L152">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `FixedLenFeature`

Configuration for parsing a fixed-length input feature.



### Aliases:

* Class <a href="/api_docs/python/tf/io/FixedLenFeature"><code>tf.FixedLenFeature</code></a>
* Class <a href="/api_docs/python/tf/io/FixedLenFeature"><code>tf.compat.v1.FixedLenFeature</code></a>
* Class <a href="/api_docs/python/tf/io/FixedLenFeature"><code>tf.compat.v1.io.FixedLenFeature</code></a>
* Class <a href="/api_docs/python/tf/io/FixedLenFeature"><code>tf.compat.v2.io.FixedLenFeature</code></a>


<!-- Placeholder for "Used in" -->

To treat sparse input as dense, provide a `default_value`; otherwise,
the parse functions will fail on any examples missing this feature.

#### Fields:


* <b>`shape`</b>: Shape of input data.
* <b>`dtype`</b>: Data type of input.
* <b>`default_value`</b>: Value to be used if an example is missing this feature. It
    must be compatible with `dtype` and of the specified `shape`.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/parsing_ops.py#L150-L152">View source</a>

``` python
@staticmethod
__new__(
    cls,
    shape,
    dtype,
    default_value=None
)
```

Create new instance of FixedLenFeature(shape, dtype, default_value)




## Properties

<h3 id="shape"><code>shape</code></h3>




<h3 id="dtype"><code>dtype</code></h3>




<h3 id="default_value"><code>default_value</code></h3>
