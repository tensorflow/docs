

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.get_uid

### `tf.contrib.keras.backend.get_uid`

``` python
get_uid(prefix='')
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

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