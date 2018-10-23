

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.get_or_create_global_step

``` python
tf.train.get_or_create_global_step(graph=None)
```



Defined in [`tensorflow/python/training/training_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/training/training_util.py).

Returns and create (if necessary) the global step tensor.

#### Args:

* <b>`graph`</b>: The graph in which to create the global step tensor. If missing, use
    default graph.


#### Returns:

The global step tensor.