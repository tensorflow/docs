page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.batch_get_value


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3282-L3302">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the value of more than one tensor variable.

### Aliases:

* `tf.compat.v1.keras.backend.batch_get_value`
* `tf.compat.v2.keras.backend.batch_get_value`


``` python
tf.keras.backend.batch_get_value(tensors)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`tensors`</b>: list of ops to run.


#### Returns:

A list of Numpy arrays.



#### Raises:


* <b>`RuntimeError`</b>: If this method is called inside defun.
