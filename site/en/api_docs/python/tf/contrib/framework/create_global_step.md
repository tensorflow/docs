page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.create_global_step

Create global step tensor in graph. (deprecated)

``` python
tf.contrib.framework.create_global_step(graph=None)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.train.create_global_step

This API is deprecated. Use core framework training version instead.

#### Args:


* <b>`graph`</b>: The graph in which to create the global step tensor. If missing, use
  default graph.


#### Returns:

Global step tensor.



#### Raises:


* <b>`ValueError`</b>: if global step tensor is already defined.