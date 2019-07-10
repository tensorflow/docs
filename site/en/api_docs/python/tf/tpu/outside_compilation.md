page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.outside_compilation

Builds part of a computation outside any current TPU replicate scope.

### Aliases:

* `tf.compat.v1.tpu.outside_compilation`
* `tf.contrib.tpu.outside_compilation`
* `tf.tpu.outside_compilation`

``` python
tf.tpu.outside_compilation(
    computation,
    *args,
    **kwargs
)
```



Defined in [`python/tpu/tpu.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/tpu/tpu.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`computation`</b>: A Python function that builds the computation to
  place on the host.
* <b>`*args`</b>: the positional arguments for the computation.
* <b>`**kwargs`</b>: the keyword arguments for the computation.


#### Returns:

The Tensors returned by computation.
