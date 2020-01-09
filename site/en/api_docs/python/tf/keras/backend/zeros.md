page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.zeros


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/zeros">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1268-L1305">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Instantiates an all-zeros variable and returns it.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/zeros"><code>tf.compat.v1.keras.backend.zeros</code></a>
* <a href="/api_docs/python/tf/keras/backend/zeros"><code>tf.compat.v2.keras.backend.zeros</code></a>


``` python
tf.keras.backend.zeros(
    shape,
    dtype=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`shape`</b>: Tuple or list of integers, shape of returned Keras variable
* <b>`dtype`</b>: data type of returned Keras variable
* <b>`name`</b>: name of returned Keras variable


#### Returns:

A variable (including Keras metadata), filled with `0.0`.
Note that if `shape` was symbolic, we cannot return a variable,
and will return a dynamically-shaped tensor instead.



#### Example:



```python
from tensorflow.keras import backend as K
kvar = K.zeros((3,4))
K.eval(kvar)
# array([[ 0.,  0.,  0.,  0.], [ 0.,  0.,  0.,  0.],
#       [ 0.,  0.,  0.,  0.]], dtype=float32)
A = tf.constant([1,2,3])
kvar2 = K.zeros(A.shape) # [0., 0., 0.] float32 by default
kvar3 = K.zeros(A.shape,dtype=tf.int32) # [0, 0, 0] with int32 dtype
kvar4 = K.zeros([2,3]) # [[0., 0., 0.], [0., 0., 0.]]
```
