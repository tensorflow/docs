page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.bfloat16_scope

``` python
tf.contrib.tpu.bfloat16_scope()
```



Defined in [`tensorflow/contrib/tpu/python/tpu/bfloat16.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/tpu/python/tpu/bfloat16.py).

Scope class for bfloat16 variables so that the model uses custom getter.

This enables variables to be read as bfloat16 type when using get_variable.