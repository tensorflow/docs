page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.int_shape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/int_shape">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1156-L1184">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the shape of tensor or variable as a tuple of int or None entries.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/int_shape"><code>tf.compat.v1.keras.backend.int_shape</code></a>
* <a href="/api_docs/python/tf/keras/backend/int_shape"><code>tf.compat.v2.keras.backend.int_shape</code></a>


``` python
tf.keras.backend.int_shape(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.


#### Returns:

A tuple of integers (or None entries).



#### Examples:


```python
>>> from keras import backend as K
>>> input = K.placeholder(shape=(2, 4, 5))
>>> K.int_shape(input)
(2, 4, 5)
>>> val = np.array([[1, 2], [3, 4]])
>>> kvar = K.variable(value=val)
>>> K.int_shape(kvar)
(2, 2)
```
