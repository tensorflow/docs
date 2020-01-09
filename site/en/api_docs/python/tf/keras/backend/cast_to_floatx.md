page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.cast_to_floatx


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/cast_to_floatx">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L150-L175">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Cast a Numpy array to the default Keras float type.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/cast_to_floatx"><code>tf.compat.v1.keras.backend.cast_to_floatx</code></a>
* <a href="/api_docs/python/tf/keras/backend/cast_to_floatx"><code>tf.compat.v2.keras.backend.cast_to_floatx</code></a>


``` python
tf.keras.backend.cast_to_floatx(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Numpy array.


#### Returns:

The same Numpy array, cast to its new type.



#### Example:


```python
    >>> from tensorflow.keras import backend as K
    >>> K.floatx()
    'float32'
    >>> arr = numpy.array([1.0, 2.0], dtype='float64')
    >>> arr.dtype
    dtype('float64')
    >>> new_arr = K.cast_to_floatx(arr)
    >>> new_arr
    array([ 1.,  2.], dtype=float32)
    >>> new_arr.dtype
    dtype('float32')
```
