

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.flatten

``` python
tf.layers.flatten(
    inputs,
    name=None
)
```



Defined in [`tensorflow/python/layers/core.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/layers/core.py).

Flattens an input tensor while preserving the batch axis (axis 0).

#### Arguments:

* <b>`inputs`</b>: Tensor input.
* <b>`name`</b>: The name of the layer (string).


#### Returns:

  Reshaped tensor.

Examples:

```
  x = tf.placeholder(shape=(None, 4, 4), dtype='float32')
  y = flatten(x)
  # now `y` has shape `(None, 16)`

  x = tf.placeholder(shape=(None, 3, None), dtype='float32')
  y = flatten(x)
  # now `y` has shape `(None, None)`
```