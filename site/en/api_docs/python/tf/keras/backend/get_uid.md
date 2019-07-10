page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.get_uid

Associates a string prefix with an integer counter in a TensorFlow graph.

### Aliases:

* `tf.compat.v1.keras.backend.get_uid`
* `tf.compat.v2.keras.backend.get_uid`
* `tf.keras.backend.get_uid`

``` python
tf.keras.backend.get_uid(prefix='')
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`prefix`</b>: String prefix to index.


#### Returns:

Unique integer ID.



#### Example:



```
  >>> get_uid('dense')
  1
  >>> get_uid('dense')
  2
```