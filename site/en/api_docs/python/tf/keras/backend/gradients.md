page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.gradients


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3785-L3797">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the gradients of `loss` w.r.t. `variables`.

### Aliases:

* `tf.compat.v1.keras.backend.gradients`
* `tf.compat.v2.keras.backend.gradients`


``` python
tf.keras.backend.gradients(
    loss,
    variables
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`loss`</b>: Scalar tensor to minimize.
* <b>`variables`</b>: List of variables.


#### Returns:

A gradients tensor.
