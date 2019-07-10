page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.experimental.get_potentially_supported_ops

Returns operations potentially supported by TensorFlow Lite.

### Aliases:

* `tf.compat.v1.lite.experimental.get_potentially_supported_ops`
* `tf.lite.experimental.get_potentially_supported_ops`

``` python
tf.lite.experimental.get_potentially_supported_ops()
```



Defined in [`lite/experimental/tensorboard/ops_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/lite/experimental/tensorboard/ops_util.py).

<!-- Placeholder for "Used in" -->

The potentially support list contains a list of ops that are partially or
fully supported, which is derived by simply scanning op names to check whether
they can be handled without real conversion and specific parameters.

Given that some ops may be partially supported, the optimal way to determine
if a model's operations are supported is by converting using the TensorFlow
Lite converter.

#### Returns:

A list of SupportedOp.
