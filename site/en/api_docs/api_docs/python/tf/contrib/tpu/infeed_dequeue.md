

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.infeed_dequeue

``` python
infeed_dequeue(
    dtype,
    shape,
    name=None
)
```



Defined in `tensorflow/contrib/tpu/ops/gen_tpu_ops.py`.

A placeholder op for a value that will be fed into the computation.

#### Args:

* <b>`dtype`</b>: A `tf.DType`. The type of elements in the tensor.
* <b>`shape`</b>: A `tf.TensorShape` or list of `ints`. The shape of the tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `dtype`.
A tensor that will be provided using the infeed mechanism.