page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.FixedLenFeature

## Class `FixedLenFeature`

Configuration for parsing a fixed-length input feature.



### Aliases:

* Class `tf.FixedLenFeature`
* Class `tf.compat.v1.FixedLenFeature`
* Class `tf.compat.v1.io.FixedLenFeature`
* Class `tf.compat.v2.io.FixedLenFeature`
* Class `tf.io.FixedLenFeature`



Defined in [`python/ops/parsing_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/parsing_ops.py).

<!-- Placeholder for "Used in" -->

To treat sparse input as dense, provide a `default_value`; otherwise,
the parse functions will fail on any examples missing this feature.

#### Fields:


* <b>`shape`</b>: Shape of input data.
* <b>`dtype`</b>: Data type of input.
* <b>`default_value`</b>: Value to be used if an example is missing this feature. It
    must be compatible with `dtype` and of the specified `shape`.

## Properties

<h3 id="shape"><code>shape</code></h3>




<h3 id="dtype"><code>dtype</code></h3>




<h3 id="default_value"><code>default_value</code></h3>






