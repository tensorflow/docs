page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ones_like


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/ones_like">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1399-L1422">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Instantiates an all-ones variable of the same shape as another tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/ones_like"><code>tf.compat.v1.keras.backend.ones_like</code></a>
* <a href="/api_docs/python/tf/keras/backend/ones_like"><code>tf.compat.v2.keras.backend.ones_like</code></a>


``` python
tf.keras.backend.ones_like(
    x,
    dtype=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Keras variable or tensor.
* <b>`dtype`</b>: String, dtype of returned Keras variable.
     None uses the dtype of x.
* <b>`name`</b>: String, name for the variable to create.


#### Returns:

A Keras variable with the shape of x filled with ones.



#### Example:


```python
>>> from keras import backend as K
>>> kvar = K.variable(np.random.random((2,3)))
>>> kvar_ones = K.ones_like(kvar)
>>> K.eval(kvar_ones)
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.]], dtype=float32)
```
