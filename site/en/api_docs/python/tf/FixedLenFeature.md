

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.FixedLenFeature

## Class `FixedLenFeature`





Defined in [`tensorflow/python/ops/parsing_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/parsing_ops.py).

See the guide: [Inputs and Readers > Converting](../../../api_guides/python/io_ops#Converting)

Configuration for parsing a fixed-length input feature.

To treat sparse input as dense, provide a `default_value`; otherwise,
the parse functions will fail on any examples missing this feature.

#### Fields:

* <b>`shape`</b>: Shape of input data.
* <b>`dtype`</b>: Data type of input.
* <b>`default_value`</b>: Value to be used if an example is missing this feature. It
      must be compatible with `dtype` and of the specified `shape`.

## Properties

<h3 id="default_value"><code>default_value</code></h3>

Alias for field number 2

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
    default_value=None
)
```





