page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.enable_v2_behavior

Enables TensorFlow 2.x behaviors.

### Aliases:

* `tf.compat.v1.enable_v2_behavior`
* `tf.compat.v2.enable_v2_behavior`
* `tf.enable_v2_behavior`

``` python
tf.enable_v2_behavior()
```



Defined in [`python/compat/v2_compat.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/compat/v2_compat.py).

<!-- Placeholder for "Used in" -->

This function can be called at the beginning of the program (before `Tensors`,
`Graphs` or other structures have been created, and before devices have been
initialized. It switches all global behaviors that are different between
TensorFlow 1.x and 2.x to behave as intended for 2.x.

This function is called in the main TensorFlow `__init__.py` file, user should
not need to call it, except during complex migrations.