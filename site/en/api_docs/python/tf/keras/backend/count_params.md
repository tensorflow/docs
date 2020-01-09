page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.count_params


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/count_params">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1513-L1533">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the static number of elements in a variable or tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/count_params"><code>tf.compat.v1.keras.backend.count_params</code></a>
* <a href="/api_docs/python/tf/keras/backend/count_params"><code>tf.compat.v2.keras.backend.count_params</code></a>


``` python
tf.keras.backend.count_params(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Variable or tensor.


#### Returns:

Integer, the number of scalars in `x`.



#### Example:


```python
>>> kvar = K.zeros((2,3))
>>> K.count_params(kvar)
6
>>> K.eval(kvar)
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.]], dtype=float32)
```
