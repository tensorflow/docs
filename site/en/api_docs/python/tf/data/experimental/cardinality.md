page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.cardinality


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/cardinality">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/cardinality.py#L32-L51">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the cardinality of `dataset`, if known.

### Aliases:

* <a href="/api_docs/python/tf/data/experimental/cardinality"><code>tf.compat.v1.data.experimental.cardinality</code></a>
* <a href="/api_docs/python/tf/data/experimental/cardinality"><code>tf.compat.v2.data.experimental.cardinality</code></a>


``` python
tf.data.experimental.cardinality(dataset)
```



<!-- Placeholder for "Used in" -->

The operation returns the cardinality of `dataset`. The operation may return
<a href="../../../tf/data/experimental#INFINITE_CARDINALITY"><code>tf.data.experimental.INFINITE_CARDINALITY</code></a> if `dataset` contains an infinite
number of elements or <a href="../../../tf/data/experimental#UNKNOWN_CARDINALITY"><code>tf.data.experimental.UNKNOWN_CARDINALITY</code></a> if the
analysis fails to determine the number of elements in `dataset` (e.g. when the
dataset source is a file).

#### Args:


* <b>`dataset`</b>: A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> for which to determine cardinality.


#### Returns:

A scalar <a href="../../../tf#int64"><code>tf.int64</code></a> `Tensor` representing the cardinality of `dataset`. If
the cardinality is infinite or unknown, the operation returns the named
constant `INFINITE_CARDINALITY` and `UNKNOWN_CARDINALITY` respectively.
