page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.reshape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/reshape">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2597-L2623">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Reshapes a tensor to the specified shape.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/reshape"><code>tf.compat.v1.keras.backend.reshape</code></a>
* <a href="/api_docs/python/tf/keras/backend/reshape"><code>tf.compat.v2.keras.backend.reshape</code></a>


``` python
tf.keras.backend.reshape(
    x,
    shape
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`shape`</b>: Target shape tuple.


#### Returns:

A tensor.



#### Example:

```python
>>> a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
>>> a
<tf.Tensor: id=32, shape=(4, 3), dtype=int32, numpy=
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]], dtype=int32)>
>>> tf.keras.backend.reshape(a, shape=(2, 6))
<tf.Tensor: id=35, shape=(2, 6), dtype=int32, numpy=
array([[ 1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12]], dtype=int32)>
```
