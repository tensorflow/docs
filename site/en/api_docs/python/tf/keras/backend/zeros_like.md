page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.zeros_like


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/zeros_like">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1372-L1396">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Instantiates an all-zeros variable of the same shape as another tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/zeros_like"><code>tf.compat.v1.keras.backend.zeros_like</code></a>
* <a href="/api_docs/python/tf/keras/backend/zeros_like"><code>tf.compat.v2.keras.backend.zeros_like</code></a>


``` python
tf.keras.backend.zeros_like(
    x,
    dtype=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Keras variable or Keras tensor.
* <b>`dtype`</b>: dtype of returned Keras variable.
       `None` uses the dtype of `x`.
* <b>`name`</b>: name for the variable to create.


#### Returns:

A Keras variable with the shape of `x` filled with zeros.



#### Example:



```python
from tensorflow.keras import backend as K
kvar = K.variable(np.random.random((2,3)))
kvar_zeros = K.zeros_like(kvar)
K.eval(kvar_zeros)
# array([[ 0.,  0.,  0.], [ 0.,  0.,  0.]], dtype=float32)
```
