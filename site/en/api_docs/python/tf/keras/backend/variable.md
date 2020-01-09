page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/variable">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L763-L812">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Instantiates a variable and returns it.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/variable"><code>tf.compat.v1.keras.backend.variable</code></a>
* <a href="/api_docs/python/tf/keras/backend/variable"><code>tf.compat.v2.keras.backend.variable</code></a>


``` python
tf.keras.backend.variable(
    value,
    dtype=None,
    name=None,
    constraint=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`value`</b>: Numpy array, initial value of the tensor.
* <b>`dtype`</b>: Tensor type.
* <b>`name`</b>: Optional name string for the tensor.
* <b>`constraint`</b>: Optional projection function to be
    applied to the variable after an optimizer update.


#### Returns:

A variable instance (with Keras metadata included).



#### Examples:


```python
>>> import numpy as np
>>> from keras import backend as K
>>> val = np.array([[1, 2], [3, 4]])
>>> kvar = K.variable(value=val, dtype='float64', name='example_var')
>>> K.dtype(kvar)
'float64'
>>> print(kvar)
example_var
>>> kvar.eval()
array([[ 1.,  2.],
       [ 3.,  4.]])
```
