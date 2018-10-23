

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.rewrite

``` python
rewrite(
    computation,
    inputs=None,
    infeed_queue=None,
    global_tpu_id=None,
    name=None
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/tpu/python/tpu/tpu.py).

Rewrites `computation` for execution on a TPU system.

#### Args:

* <b>`computation`</b>: a Python function that builds a computation to apply
    to the input. If the function takes n inputs, 'inputs' should be
    a list of n tensors. If the function returns m outputs, rewrite
    will return a list of m tensors.
* <b>`inputs`</b>: a list of input tensors or None (equivalent to an empty list).
* <b>`infeed_queue`</b>: if not None, the InfeedQueue from which to append a tuple
    of arguments as inputs to `computation`.
* <b>`global_tpu_id`</b>: if not None, a Numpy 2D array indicating the global
    id of each TPU device in the system. The outer dimension of the
    array is host task id, and the inner dimension is device ordinal,
    so e.g., global_tpu_id[x][y] indicates the global id of device
    /task:x/device:TPU_NODE:y.
* <b>`name`</b>: name of the operator.

#### Returns:

A list of output tensors.