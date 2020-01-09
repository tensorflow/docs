page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.get_uid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/get_uid">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L184-L208">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Associates a string prefix with an integer counter in a TensorFlow graph.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/get_uid"><code>tf.compat.v1.keras.backend.get_uid</code></a>
* <a href="/api_docs/python/tf/keras/backend/get_uid"><code>tf.compat.v2.keras.backend.get_uid</code></a>


``` python
tf.keras.backend.get_uid(prefix='')
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`prefix`</b>: String prefix to index.


#### Returns:

Unique integer ID.



#### Example:



```
  >>> get_uid('dense')
  1
  >>> get_uid('dense')
  2
```
