page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.is_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/is_sparse">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L684-L705">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns whether a tensor is a sparse tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/is_sparse"><code>tf.compat.v1.keras.backend.is_sparse</code></a>
* <a href="/api_docs/python/tf/keras/backend/is_sparse"><code>tf.compat.v2.keras.backend.is_sparse</code></a>


``` python
tf.keras.backend.is_sparse(tensor)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`tensor`</b>: A tensor instance.


#### Returns:

A boolean.



#### Example:


```python
>>> from keras import backend as K
>>> a = K.placeholder((2, 2), sparse=False)
>>> print(K.is_sparse(a))
False
>>> b = K.placeholder((2, 2), sparse=True)
>>> print(K.is_sparse(b))
True
```
