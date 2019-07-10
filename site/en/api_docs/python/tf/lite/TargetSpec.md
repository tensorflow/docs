page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.TargetSpec

## Class `TargetSpec`

Specification of target device.



### Aliases:

* Class `tf.compat.v1.lite.TargetSpec`
* Class `tf.compat.v2.lite.TargetSpec`
* Class `tf.lite.TargetSpec`



Defined in [`lite/python/lite.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/lite/python/lite.py).

<!-- Placeholder for "Used in" -->

Details about target device. Converter optimizes the generated model for
specific device.

#### Attributes:


* <b>`supported_ops`</b>: Experimental flag, subject to change. Set of OpsSet options
  supported by the device. (default set([OpsSet.TFLITE_BUILTINS]))

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(supported_ops=None)
```






