


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.FixedLenSequenceFeature

### `class tf.FixedLenSequenceFeature`

See the guide: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting)

Configuration for a dense input feature in a sequence item.

To treat a sparse input as dense, provide `allow_missing=True`; otherwise,
the parse functions will fail on any examples missing this feature.

#### Fields:

* <b>`shape`</b>: Shape of input data.
* <b>`dtype`</b>: Data type of input.
* <b>`allow_missing`</b>: Whether to allow this feature to be missing from a feature
    list item.

## Properties

<h3 id="allow_missing"><code>allow_missing</code></h3>

Alias for field number 2

<h3 id="dtype"><code>dtype</code></h3>

Alias for field number 1

<h3 id="shape"><code>shape</code></h3>

Alias for field number 0



## Class Members

<h3 id="__init__"><code>__init__</code></h3>

<h3 id="count"><code>count</code></h3>

<h3 id="index"><code>index</code></h3>



Defined in [`tensorflow/python/ops/parsing_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/parsing_ops.py).

