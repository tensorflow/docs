


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.SparseFeature

### `class tf.SparseFeature`

See the guide: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting)

Configuration for parsing a sparse input feature.

#### Fields:

* <b>`index_key`</b>: Name of index feature.  The underlying feature's type must
    be `int64` and its length must always match that of the `value_key`
    feature.
* <b>`value_key`</b>: Name of value feature.  The underlying feature's type must
    be `dtype` and its length must always match that of the `index_key`
    feature.
* <b>`dtype`</b>: Data type of the `value_key` feature.
* <b>`size`</b>: A Python int to specify a dimension of the dense shape. Each value in
    the `index_key` feature must be in `[0, size)`.
* <b>`already_sorted`</b>: A Python boolean to specify whether the values in
    `index_key` are already sorted. If so skip sorting.
    False by default (optional).

## Properties

<h3 id="already_sorted"><code>already_sorted</code></h3>

Alias for field number 4

<h3 id="dtype"><code>dtype</code></h3>

Alias for field number 2

<h3 id="index_key"><code>index_key</code></h3>

Alias for field number 0

<h3 id="size"><code>size</code></h3>

Alias for field number 3

<h3 id="value_key"><code>value_key</code></h3>

Alias for field number 1



## Class Members

<h3 id="__init__"><code>__init__</code></h3>

<h3 id="count"><code>count</code></h3>

<h3 id="index"><code>index</code></h3>



Defined in [`tensorflow/python/ops/parsing_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/parsing_ops.py).

