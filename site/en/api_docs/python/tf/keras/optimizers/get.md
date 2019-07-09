page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.get

``` python
tf.keras.optimizers.get(identifier)
```



Defined in [`tensorflow/python/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/keras/optimizers.py).

Retrieves a Keras Optimizer instance.

#### Arguments:

* <b>`identifier`</b>: Optimizer identifier, one of
        - String: name of an optimizer
        - Dictionary: configuration dictionary.
        - Keras Optimizer instance (it will be returned unchanged).
        - TensorFlow Optimizer instance
            (it will be wrapped as a Keras Optimizer).


#### Returns:

A Keras Optimizer instance.


#### Raises:

* <b>`ValueError`</b>: If `identifier` cannot be interpreted.