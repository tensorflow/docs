page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.repeat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/repeat">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2813-L2845">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Repeats a 2D tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/repeat"><code>tf.compat.v1.keras.backend.repeat</code></a>
* <a href="/api_docs/python/tf/keras/backend/repeat"><code>tf.compat.v2.keras.backend.repeat</code></a>


``` python
tf.keras.backend.repeat(
    x,
    n
)
```



<!-- Placeholder for "Used in" -->

if `x` has shape (samples, dim) and `n` is `2`,
the output will have shape `(samples, 2, dim)`.

#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`n`</b>: Python integer, number of times to repeat.


#### Returns:

A tensor.



#### Example:

```python
>>> b = tf.constant([[1, 2], [3, 4]])
>>> b
<tf.Tensor: id=78, shape=(2, 2), dtype=int32, numpy=
array([[1, 2],
       [3, 4]], dtype=int32)>
>>> tf.keras.backend.repeat(b, n=2)
<tf.Tensor: id=82, shape=(2, 2, 2), dtype=int32, numpy=
array([[[1, 2],
        [1, 2]],
       [[3, 4],
        [3, 4]]], dtype=int32)>
```
