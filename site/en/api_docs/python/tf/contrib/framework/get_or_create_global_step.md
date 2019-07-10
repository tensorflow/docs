page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_or_create_global_step

Returns and create (if necessary) the global step tensor. (deprecated)

``` python
tf.contrib.framework.get_or_create_global_step(graph=None)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.train.get_or_create_global_step

#### Args:


* <b>`graph`</b>: The graph in which to create the global step tensor. If missing, use
  default graph.


#### Returns:

The global step tensor.
