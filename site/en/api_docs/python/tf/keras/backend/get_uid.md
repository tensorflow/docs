

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.get_uid

``` python
tf.keras.backend.get_uid(prefix='')
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/backend.py).

Associates a string prefix with an integer counter in a TensorFlow graph.

#### Arguments:

* <b>`prefix`</b>: String prefix to index.


#### Returns:

  Unique integer ID.

Example:

```
  >>> get_uid('dense')
  1
  >>> get_uid('dense')
  2
```