page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.set_epsilon


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend_config.py#L47-L57">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the value of the fuzz factor used in numeric expressions.

### Aliases:

* `tf.compat.v1.keras.backend.set_epsilon`
* `tf.compat.v2.keras.backend.set_epsilon`


``` python
tf.keras.backend.set_epsilon(value)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`value`</b>: float. New value of epsilon.
Example: ```python from keras import backend as K K.epsilon() >>> 1e-07
  K.set_epsilon(1e-05) K.epsilon() >>> 1e-05 ```
