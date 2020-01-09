page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.expand_dims


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3069-L3080">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds a 1-sized dimension at index "axis".

### Aliases:

* `tf.compat.v1.keras.backend.expand_dims`
* `tf.compat.v2.keras.backend.expand_dims`


``` python
tf.keras.backend.expand_dims(
    x,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: Position where to add a new axis.


#### Returns:

A tensor with expanded dimensions.
