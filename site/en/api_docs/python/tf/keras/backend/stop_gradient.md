page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.stop_gradient


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3800-L3815">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns `variables` but with zero gradient w.r.t. every other variable.

### Aliases:

* `tf.compat.v1.keras.backend.stop_gradient`
* `tf.compat.v2.keras.backend.stop_gradient`


``` python
tf.keras.backend.stop_gradient(variables)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`variables`</b>: Tensor or list of tensors to consider constant with respect
  to any other variable.



#### Returns:

A single tensor or a list of tensors (depending on the passed argument)
that has no gradient with respect to any other variable.
