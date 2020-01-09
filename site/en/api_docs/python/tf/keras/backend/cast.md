page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.cast


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/cast">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1536-L1565">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Casts a tensor to a different dtype and returns it.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/cast"><code>tf.compat.v1.keras.backend.cast</code></a>
* <a href="/api_docs/python/tf/keras/backend/cast"><code>tf.compat.v2.keras.backend.cast</code></a>


``` python
tf.keras.backend.cast(
    x,
    dtype
)
```



<!-- Placeholder for "Used in" -->

You can cast a Keras variable but it still returns a Keras tensor.

#### Arguments:


* <b>`x`</b>: Keras tensor (or variable).
* <b>`dtype`</b>: String, either (`'float16'`, `'float32'`, or `'float64'`).


#### Returns:

Keras tensor with dtype `dtype`.



#### Examples:

Cast a float32 variable to a float64 tensor


```python
>>> import tensorflow as tf
>>> from tensorflow.keras import backend as K
>>> input = K.ones(shape=(1,3))
>>> print(input)
>>> cast_input = K.cast(input, dtype='float64')
>>> print(cast_input)

<tf.Variable 'Variable:0' shape=(1, 3) dtype=float32,
     numpy=array([[1., 1., 1.]], dtype=float32)>
tf.Tensor([[1. 1. 1.]], shape=(1, 3), dtype=float64)
```
