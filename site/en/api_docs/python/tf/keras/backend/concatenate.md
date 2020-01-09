page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.concatenate


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/concatenate">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2562-L2594">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Concatenates a list of tensors alongside the specified axis.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/concatenate"><code>tf.compat.v1.keras.backend.concatenate</code></a>
* <a href="/api_docs/python/tf/keras/backend/concatenate"><code>tf.compat.v2.keras.backend.concatenate</code></a>


``` python
tf.keras.backend.concatenate(
    tensors,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`tensors`</b>: list of tensors to concatenate.
* <b>`axis`</b>: concatenation axis.


#### Returns:

A tensor.



#### Example:

```python
>>> a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> b = tf.constant([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
>>> tf.keras.backend.concatenate((a, b), axis=-1)
<tf.Tensor: id=14, shape=(3, 6), dtype=int32, numpy=
array([[ 1,  2,  3, 10, 20, 30],
       [ 4,  5,  6, 40, 50, 60],
       [ 7,  8,  9, 70, 80, 90]], dtype=int32)>
```
