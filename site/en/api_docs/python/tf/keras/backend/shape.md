page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.shape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L1129-L1159">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the symbolic shape of a tensor or variable.

### Aliases:

* `tf.compat.v1.keras.backend.shape`
* `tf.compat.v2.keras.backend.shape`


``` python
tf.keras.backend.shape(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.


#### Returns:

A symbolic shape (which is itself a tensor).



#### Examples:



```python
    # TensorFlow example
    >>> from keras import backend as K
    >>> tf_session = K.get_session()
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val)
    >>> input = keras.backend.placeholder(shape=(2, 4, 5))
    >>> K.shape(kvar)
    <tf.Tensor 'Shape_8:0' shape=(2,) dtype=int32>
    >>> K.shape(input)
    <tf.Tensor 'Shape_9:0' shape=(3,) dtype=int32>
    # To get integer shape (Instead, you can use K.int_shape(x))
    >>> K.shape(kvar).eval(session=tf_session)
    array([2, 2], dtype=int32)
    >>> K.shape(input).eval(session=tf_session)
    array([2, 4, 5], dtype=int32)
```
