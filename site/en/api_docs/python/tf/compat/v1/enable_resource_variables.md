page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.enable_resource_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/variable_scope.py#L214-L232">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates resource variables by default.

``` python
tf.compat.v1.enable_resource_variables()
```



<!-- Placeholder for "Used in" -->

Resource variables are improved versions of TensorFlow variables with a
well-defined memory model. Accessing a resource variable reads its value, and
all ops which access a specific read value of the variable are guaranteed to
see the same value for that tensor. Writes which happen after a read (by
having a control or data dependency on the read) are guaranteed not to affect
the value of the read tensor, and similarly writes which happen before a read
are guaranteed to affect the value. No guarantees are made about unordered
read/write pairs.

Calling tf.enable_resource_variables() lets you opt-in to this TensorFlow 2.0
feature.
