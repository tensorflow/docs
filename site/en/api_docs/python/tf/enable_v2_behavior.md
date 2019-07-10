page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.enable_v2_behavior

``` python
tf.enable_v2_behavior()
```



Defined in [`tensorflow/python/compat/compat.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/compat/compat.py).

Enables TensorFlow 2.x behaviors.

This function can be called at the beginning of the program (before `Tensors`,
`Graphs` or other structures have been created, and before devices have been
initialized. It switches all global behaviors that are different between
TensorFlow 1.x and 2.x to behave as intended for 2.x.

This function is called in the main TensorFlow `__init__.py` file, user should
not need to call it, except during complex migrations.