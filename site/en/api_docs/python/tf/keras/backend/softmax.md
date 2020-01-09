page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.softmax


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L4384-L4396">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Softmax of a tensor.

### Aliases:

* `tf.compat.v1.keras.backend.softmax`
* `tf.compat.v2.keras.backend.softmax`


``` python
tf.keras.backend.softmax(
    x,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: The dimension softmax would be performed on.
    The default is -1 which indicates the last dimension.


#### Returns:

A tensor.
