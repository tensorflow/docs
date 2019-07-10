page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.outside_compilation

``` python
tf.contrib.tpu.outside_compilation(
    computation,
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/tpu/python/tpu/tpu.py).

Builds part of a computation outside any current TPU replicate scope.

#### Args:

* <b>`computation`</b>: A Python function that builds the computation to
    place on the host.
* <b>`*args`</b>: the positional arguments for the computation.
* <b>`**kwargs`</b>: the keyword arguments for the computation.


#### Returns:

The Tensors returned by computation.