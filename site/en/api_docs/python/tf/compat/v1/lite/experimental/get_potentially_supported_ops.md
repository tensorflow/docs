page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.lite.experimental.get_potentially_supported_ops


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/experimental/tensorboard/ops_util.py#L34-L50">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns operations potentially supported by TensorFlow Lite.

``` python
tf.compat.v1.lite.experimental.get_potentially_supported_ops()
```



<!-- Placeholder for "Used in" -->

The potentially support list contains a list of ops that are partially or
fully supported, which is derived by simply scanning op names to check whether
they can be handled without real conversion and specific parameters.

Given that some ops may be partially supported, the optimal way to determine
if a model's operations are supported is by converting using the TensorFlow
Lite converter.

#### Returns:

A list of SupportedOp.
