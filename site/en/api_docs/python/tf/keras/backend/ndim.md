page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ndim


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/ndim">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1187-L1212">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the number of axes in a tensor, as an integer.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/ndim"><code>tf.compat.v1.keras.backend.ndim</code></a>
* <a href="/api_docs/python/tf/keras/backend/ndim"><code>tf.compat.v2.keras.backend.ndim</code></a>


``` python
tf.keras.backend.ndim(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.


#### Returns:

Integer (scalar), number of axes.



#### Examples:


```python
>>> from keras import backend as K
>>> input = K.placeholder(shape=(2, 4, 5))
>>> val = np.array([[1, 2], [3, 4]])
>>> kvar = K.variable(value=val)
>>> K.ndim(input)
3
>>> K.ndim(kvar)
2
```
