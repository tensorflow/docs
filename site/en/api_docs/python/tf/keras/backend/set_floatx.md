page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.set_floatx


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/set_floatx">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend_config.py#L77-L92">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the default float type.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/set_floatx"><code>tf.compat.v1.keras.backend.set_floatx</code></a>
* <a href="/api_docs/python/tf/keras/backend/set_floatx"><code>tf.compat.v2.keras.backend.set_floatx</code></a>


``` python
tf.keras.backend.set_floatx(value)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`value`</b>: String; 'float16', 'float32', or 'float64'.
Example: ```python from keras import backend as K K.floatx() >>> 'float32'
  K.set_floatx('float16') K.floatx() >>> 'float16' ```

#### Raises:


* <b>`ValueError`</b>: In case of invalid value.
