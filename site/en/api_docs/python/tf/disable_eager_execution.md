page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.disable_eager_execution

Disables eager execution.

### Aliases:

* `tf.compat.v1.disable_eager_execution`
* `tf.disable_eager_execution`

``` python
tf.disable_eager_execution()
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->

This function can only be called before any Graphs, Ops, or Tensors have been
created. It can be used at the beginning of the program for complex migration
projects from TensorFlow 1.x to 2.x.