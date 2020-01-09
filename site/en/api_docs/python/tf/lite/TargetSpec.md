page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.TargetSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/lite.py#L134-L155">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TargetSpec`

Specification of target device.



### Aliases:

* Class `tf.compat.v1.lite.TargetSpec`
* Class `tf.compat.v2.lite.TargetSpec`


<!-- Placeholder for "Used in" -->

Details about target device. Converter optimizes the generated model for
specific device.

#### Attributes:


* <b>`supported_ops`</b>: Experimental flag, subject to change. Set of OpsSet options
  supported by the device. (default set([OpsSet.TFLITE_BUILTINS]))
* <b>`supported_types`</b>: List of types for constant values on the target device.
  Supported values are types exported by lite.constants. Frequently, an
  optimization choice is driven by the most compact (i.e. smallest)
  type in this list (default [constants.FLOAT])

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/lite.py#L149-L155">View source</a>

``` python
__init__(
    supported_ops=None,
    supported_types=None
)
```

Initialize self.  See help(type(self)) for accurate signature.
