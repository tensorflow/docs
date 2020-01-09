page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.to_dense


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/to_dense">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L708-L732">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a sparse tensor into a dense tensor and returns it.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/to_dense"><code>tf.compat.v1.keras.backend.to_dense</code></a>
* <a href="/api_docs/python/tf/keras/backend/to_dense"><code>tf.compat.v2.keras.backend.to_dense</code></a>


``` python
tf.keras.backend.to_dense(tensor)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`tensor`</b>: A tensor instance (potentially sparse).


#### Returns:

A dense tensor.



#### Examples:


```python
>>> from keras import backend as K
>>> b = K.placeholder((2, 2), sparse=True)
>>> print(K.is_sparse(b))
True
>>> c = K.to_dense(b)
>>> print(K.is_sparse(c))
False
```
