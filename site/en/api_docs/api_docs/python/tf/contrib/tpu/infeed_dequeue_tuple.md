

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.infeed_dequeue_tuple

``` python
infeed_dequeue_tuple(
    dtypes,
    shapes,
    name=None
)
```



Defined in `tensorflow/contrib/tpu/ops/gen_tpu_ops.py`.

A placeholder op for multiple values that will be fed into the computation

simultaneously as an XLA tuple.

#### Args:

* <b>`dtypes`</b>: A list of `tf.DTypes` that has length `>= 1`.
    The element types of each element in `outputs`.
* <b>`shapes`</b>: A list of shapes (each a `tf.TensorShape` or list of `ints`).
    The shapes of each tensor in `outputs`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` objects of type `dtypes`.
A list of tensors that will be provided using the infeed mechanism.