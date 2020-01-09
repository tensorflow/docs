page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.temporal_padding


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3097-L3111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Pads the middle dimension of a 3D tensor.

### Aliases:

* `tf.compat.v1.keras.backend.temporal_padding`
* `tf.compat.v2.keras.backend.temporal_padding`


``` python
tf.keras.backend.temporal_padding(
    x,
    padding=(1, 1)
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`padding`</b>: Tuple of 2 integers, how many zeros to
    add at the start and end of dim 1.


#### Returns:

A padded 3D tensor.
