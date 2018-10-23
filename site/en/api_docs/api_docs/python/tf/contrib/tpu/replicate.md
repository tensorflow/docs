

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.replicate

``` python
replicate(
    computation,
    inputs=None,
    infeed_queue=None,
    global_tpu_id=None,
    name=None
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/tpu/python/tpu/tpu.py).

Builds a graph operator that runs a replicated TPU computation.

#### Args:

* <b>`computation`</b>: a Python function that builds the computation to replicate.
* <b>`inputs`</b>: a list of lists of input tensors or None (equivalent to
    [[]]), indexed by [replica_num][input_num]. All replicas must
    have the same number of inputs.
* <b>`infeed_queue`</b>: if not None, the InfeedQueue from which to append a tuple
    of arguments as inputs to computation.
* <b>`global_tpu_id`</b>: if not None, a Numpy 2D array indicating the global
    id of each TPU device in the system. The outer dimension of the
    array is host task id, and the inner dimension is device ordinal,
    so e.g., global_tpu_id[x][y] indicates the global id of device
    /task:x/device:TPU_NODE:y.
* <b>`name`</b>: name of the operator.

#### Returns:

A list of lists of output tensors, indexed by [replica_num][output_num].

#### Raises:

* <b>`ValueError`</b>: if all replicas do not have equal numbers of input tensors.
* <b>`ValueError`</b>: if the number of inputs per replica does not match
    the number of formal parameters to `computation`.