page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.is_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L689-L710">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns whether a tensor is a sparse tensor.

### Aliases:

* `tf.compat.v1.keras.backend.is_sparse`
* `tf.compat.v2.keras.backend.is_sparse`


``` python
tf.keras.backend.is_sparse(tensor)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`tensor`</b>: A tensor instance.


#### Returns:

A boolean.



#### Example:


```python
    >>> from keras import backend as K
    >>> a = K.placeholder((2, 2), sparse=False)
    >>> print(K.is_sparse(a))
    False
    >>> b = K.placeholder((2, 2), sparse=True)
    >>> print(K.is_sparse(b))
    True
```
