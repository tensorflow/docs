page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.create_global_step

Create global step tensor in graph.

### Aliases:

* `tf.compat.v1.train.create_global_step`
* `tf.train.create_global_step`

``` python
tf.train.create_global_step(graph=None)
```



Defined in [`python/training/training_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/training_util.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`graph`</b>: The graph in which to create the global step tensor. If missing, use
  default graph.


#### Returns:

Global step tensor.



#### Raises:


* <b>`ValueError`</b>: if global step tensor is already defined.