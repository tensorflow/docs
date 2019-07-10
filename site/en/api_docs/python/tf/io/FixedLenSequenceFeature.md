page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.FixedLenSequenceFeature

## Class `FixedLenSequenceFeature`

Configuration for parsing a variable-length input feature into a `Tensor`.



### Aliases:

* Class `tf.FixedLenSequenceFeature`
* Class `tf.compat.v1.FixedLenSequenceFeature`
* Class `tf.compat.v1.io.FixedLenSequenceFeature`
* Class `tf.compat.v2.io.FixedLenSequenceFeature`
* Class `tf.io.FixedLenSequenceFeature`



Defined in [`python/ops/parsing_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/parsing_ops.py).

<!-- Placeholder for "Used in" -->

The resulting `Tensor` of parsing a single `SequenceExample` or `Example` has
a static `shape` of `[None] + shape` and the specified `dtype`.
The resulting `Tensor` of parsing a `batch_size` many `Example`s has
a static `shape` of `[batch_size, None] + shape` and the specified `dtype`.
The entries in the `batch` from different `Examples` will be padded with
`default_value` to the maximum length present in the `batch`.

To treat a sparse input as dense, provide `allow_missing=True`; otherwise,
the parse functions will fail on any examples missing this feature.

#### Fields:


* <b>`shape`</b>: Shape of input data for dimension 2 and higher. First dimension is
  of variable length `None`.
* <b>`dtype`</b>: Data type of input.
* <b>`allow_missing`</b>: Whether to allow this feature to be missing from a feature
  list item. Is available only for parsing `SequenceExample` not for
  parsing `Examples`.
* <b>`default_value`</b>: Scalar value to be used to pad multiple `Example`s to their
  maximum length. Irrelevant for parsing a single `Example` or
  `SequenceExample`. Defaults to "" for dtype string and 0 otherwise
  (optional).

## Properties

<h3 id="shape"><code>shape</code></h3>




<h3 id="dtype"><code>dtype</code></h3>




<h3 id="allow_missing"><code>allow_missing</code></h3>




<h3 id="default_value"><code>default_value</code></h3>






