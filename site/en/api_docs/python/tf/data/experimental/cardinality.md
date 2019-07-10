page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.cardinality

Returns the cardinality of `dataset`, if known.

### Aliases:

* `tf.compat.v1.data.experimental.cardinality`
* `tf.compat.v2.data.experimental.cardinality`
* `tf.data.experimental.cardinality`

``` python
tf.data.experimental.cardinality(dataset)
```



Defined in [`python/data/experimental/ops/cardinality.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/cardinality.py).

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
