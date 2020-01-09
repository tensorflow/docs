page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.permute_dimensions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/permute_dimensions">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2626-L2654">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Permutes axes in a tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/permute_dimensions"><code>tf.compat.v1.keras.backend.permute_dimensions</code></a>
* <a href="/api_docs/python/tf/keras/backend/permute_dimensions"><code>tf.compat.v2.keras.backend.permute_dimensions</code></a>


``` python
tf.keras.backend.permute_dimensions(
    x,
    pattern
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`pattern`</b>: A tuple of
    dimension indices, e.g. `(0, 2, 1)`.


#### Returns:

A tensor.



#### Example:

```python
>>> a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
>>> a
<tf.Tensor: id=49, shape=(4, 3), dtype=int32, numpy=
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]], dtype=int32)>
>>> tf.keras.backend.permute_dimensions(a, pattern=(1, 0))
<tf.Tensor: id=52, shape=(3, 4), dtype=int32, numpy=
array([[ 1,  4,  7, 10],
       [ 2,  5,  8, 11],
       [ 3,  6,  9, 12]], dtype=int32)>
```
