page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.maximum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/maximum">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2302-L2325">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Element-wise maximum of two tensors.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/maximum"><code>tf.compat.v1.keras.backend.maximum</code></a>
* <a href="/api_docs/python/tf/keras/backend/maximum"><code>tf.compat.v2.keras.backend.maximum</code></a>


``` python
tf.keras.backend.maximum(
    x,
    y
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`y`</b>: Tensor or variable.


#### Returns:

A tensor with the element wise maximum value(s) of `x` and `y`.



#### Examples:


```python
# maximum of two tensors
>>> x = tf.Variable([[1, 2], [3, 4]])
>>> y = tf.Variable([[2, 1], [0, -1]])
>>> m = tf.keras.backend.maximum(x, y)
>>> m
<tf.Tensor: id=42, shape=(2, 2), dtype=int32, numpy=
array([[2, 2],
       [3, 4]], dtype=int32)>
```
