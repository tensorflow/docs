

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.layers.recompute_grad

``` python
tf.contrib.layers.recompute_grad(fn)
```



Defined in [`tensorflow/contrib/layers/python/layers/rev_block_lib.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/layers/python/layers/rev_block_lib.py).

Decorator that recomputes the function on the backwards pass.

#### Args:

* <b>`fn`</b>: a function that takes Tensors (all as positional arguments) and returns
    a tuple of Tensors.


#### Returns:

A wrapped fn that is identical to fn when called, but its activations will
be discarded and recomputed on the backwards pass (i.e. on a call to
tf.gradients).