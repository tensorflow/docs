page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.eval


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/eval">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1246-L1265">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Evaluates the value of a variable.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/eval"><code>tf.compat.v1.keras.backend.eval</code></a>
* <a href="/api_docs/python/tf/keras/backend/eval"><code>tf.compat.v2.keras.backend.eval</code></a>


``` python
tf.keras.backend.eval(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A variable.


#### Returns:

A Numpy array.



#### Examples:


```python
>>> from keras import backend as K
>>> kvar = K.variable(np.array([[1, 2], [3, 4]]), dtype='float32')
>>> K.eval(kvar)
array([[ 1.,  2.],
       [ 3.,  4.]], dtype=float32)
```
