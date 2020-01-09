page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.any


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2120-L2133">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Bitwise reduction (logical OR).

### Aliases:

* `tf.compat.v1.keras.backend.any`
* `tf.compat.v2.keras.backend.any`


``` python
tf.keras.backend.any(
    x,
    axis=None,
    keepdims=False
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`axis`</b>: axis along which to perform the reduction.
* <b>`keepdims`</b>: whether the drop or broadcast the reduction axes.


#### Returns:

A uint8 tensor (0s and 1s).
