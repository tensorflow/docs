page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.deserialize


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/optimizers/deserialize">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizers.py#L785-L815">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Inverse of the `serialize` function.

### Aliases:

* <a href="/api_docs/python/tf/keras/optimizers/deserialize"><code>tf.compat.v1.keras.optimizers.deserialize</code></a>
* <a href="/api_docs/python/tf/keras/optimizers/deserialize"><code>tf.compat.v2.keras.optimizers.deserialize</code></a>
* <a href="/api_docs/python/tf/keras/optimizers/deserialize"><code>tf.compat.v2.optimizers.deserialize</code></a>


``` python
tf.keras.optimizers.deserialize(
    config,
    custom_objects=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`config`</b>: Optimizer configuration dictionary.
* <b>`custom_objects`</b>: Optional dictionary mapping names (strings) to custom
  objects (classes and functions) to be considered during deserialization.


#### Returns:

A Keras Optimizer instance.
