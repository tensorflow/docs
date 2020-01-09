page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.image_data_format


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/image_data_format">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend_config.py#L95-L107">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the default image data format convention.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/image_data_format"><code>tf.compat.v1.keras.backend.image_data_format</code></a>
* <a href="/api_docs/python/tf/keras/backend/image_data_format"><code>tf.compat.v2.keras.backend.image_data_format</code></a>


``` python
tf.keras.backend.image_data_format()
```



<!-- Placeholder for "Used in" -->


#### Returns:

A string, either `'channels_first'` or `'channels_last'`



#### Example:


```python
keras.backend.image_data_format() >>> 'channels_first'
```
