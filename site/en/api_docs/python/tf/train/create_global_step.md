

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.create_global_step

``` python
tf.train.create_global_step(graph=None)
```



Defined in [`tensorflow/python/training/training_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/training/training_util.py).

Create global step tensor in graph.

#### Args:

* <b>`graph`</b>: The graph in which to create the global step tensor. If missing,
    use default graph.


#### Returns:

Global step tensor.


#### Raises:

* <b>`ValueError`</b>: if global step tensor is already defined.