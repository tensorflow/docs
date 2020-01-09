page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.flatten


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/flatten">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2903-L2925">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Flatten a tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/flatten"><code>tf.compat.v1.keras.backend.flatten</code></a>
* <a href="/api_docs/python/tf/keras/backend/flatten"><code>tf.compat.v2.keras.backend.flatten</code></a>


``` python
tf.keras.backend.flatten(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.


#### Returns:

A tensor, reshaped into 1-D



#### Example:

```python
>>> b = tf.constant([[1, 2], [3, 4]])
>>> b
<tf.Tensor: id=102, shape=(2, 2), dtype=int32, numpy=
array([[1, 2],
       [3, 4]], dtype=int32)>
>>> tf.keras.backend.flatten(b)
<tf.Tensor: id=105, shape=(4,), dtype=int32,
    numpy=array([1, 2, 3, 4], dtype=int32)>
```
