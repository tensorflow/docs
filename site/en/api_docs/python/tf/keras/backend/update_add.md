page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.update_add


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L1582-L1593">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Update the value of `x` by adding `increment`.

### Aliases:

* `tf.compat.v1.keras.backend.update_add`
* `tf.compat.v2.keras.backend.update_add`


``` python
tf.keras.backend.update_add(
    x,
    increment
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A Variable.
* <b>`increment`</b>: A tensor of same shape as `x`.


#### Returns:

The variable `x` updated.
