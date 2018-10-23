


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.FixedLenFeature

### `class tf.FixedLenFeature`

See the guide: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting)

Configuration for parsing a fixed-length input feature.

To treat sparse input as dense, provide a `default_value`; otherwise,
the parse functions will fail on any examples missing this feature.

#### Fields:

* <b>`shape`</b>: Shape of input data.
* <b>`dtype`</b>: Data type of input.
* <b>`default_value`</b>: Value to be used if an example is missing this feature. It
      must be compatible with `dtype`.

## Properties

<h3 id="default_value"><code>default_value</code></h3>

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

