page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.normalize


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/normalize">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/np_utils.py#L55-L69">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Normalizes a Numpy array.

### Aliases:

* <a href="/api_docs/python/tf/keras/utils/normalize"><code>tf.compat.v1.keras.utils.normalize</code></a>
* <a href="/api_docs/python/tf/keras/utils/normalize"><code>tf.compat.v2.keras.utils.normalize</code></a>


``` python
tf.keras.utils.normalize(
    x,
    axis=-1,
    order=2
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Numpy array to normalize.
* <b>`axis`</b>: axis along which to normalize.
* <b>`order`</b>: Normalization order (e.g. 2 for L2 norm).


#### Returns:

A normalized copy of the array.
