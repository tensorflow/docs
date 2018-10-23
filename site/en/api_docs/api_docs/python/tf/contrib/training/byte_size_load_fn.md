

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.byte_size_load_fn

``` python
tf.contrib.training.byte_size_load_fn(op)
```



Defined in [`tensorflow/contrib/training/python/training/device_setter.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/training/python/training/device_setter.py).

Load function that computes the byte size of a single-output `Operation`.

This is intended to be used with `"Variable"` ops, which have a single
`Tensor` output with the contents of the variable.  However, it can also be
used for calculating the size of any op that has a single output.

Intended to be used with `GreedyLoadBalancingStrategy`.

#### Args:

* <b>`op`</b>: An `Operation` with a single output, typically a "Variable" op.


#### Returns:

The number of bytes in the output `Tensor`.


#### Raises:

* <b>`ValueError`</b>: if `op` does not have a single output, or if the shape of the
    single output is not fully-defined.