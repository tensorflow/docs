page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/stack">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L3075-L3098">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stacks a list of rank `R` tensors into a rank `R+1` tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/stack"><code>tf.compat.v1.keras.backend.stack</code></a>
* <a href="/api_docs/python/tf/keras/backend/stack"><code>tf.compat.v2.keras.backend.stack</code></a>


``` python
tf.keras.backend.stack(
    x,
    axis=0
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: List of tensors.
* <b>`axis`</b>: Axis along which to perform stacking.


#### Returns:

A tensor.



#### Example:

```python
>>> a = tf.constant([[1, 2],[3, 4]])
>>> b = tf.constant([[10, 20],[30, 40]])
>>> tf.keras.backend.stack((a, b))
<tf.Tensor: id=146, shape=(2, 2, 2), dtype=int32, numpy=
array([[[ 1,  2],
        [ 3,  4]],
       [[10, 20],
        [30, 40]]], dtype=int32)>
```
