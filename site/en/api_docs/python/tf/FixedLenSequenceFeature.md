

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.FixedLenSequenceFeature

## Class `FixedLenSequenceFeature`





Defined in [`tensorflow/python/ops/parsing_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/parsing_ops.py).

See the guide: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting)

Configuration for parsing a variable-length input feature into a `Tensor`.

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

<h3 id="allow_missing"><code>allow_missing</code></h3>

Alias for field number 2

<h3 id="default_value"><code>default_value</code></h3>

Alias for field number 3

<h3 id="dtype"><code>dtype</code></h3>

Alias for field number 1

<h3 id="shape"><code>shape</code></h3>

Alias for field number 0



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    shape,
    dtype,
    allow_missing=False,
    default_value=None
)
```





