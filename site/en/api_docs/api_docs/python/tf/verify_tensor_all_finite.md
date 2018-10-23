

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.verify_tensor_all_finite

``` python
verify_tensor_all_finite(
    t,
    msg,
    name=None
)
```



Defined in [`tensorflow/python/ops/numerics.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/numerics.py).

See the guide: [Control Flow > Debugging Operations](../../../api_guides/python/control_flow_ops#Debugging_Operations)

Assert that the tensor does not contain any NaN's or Inf's.

#### Args:

* <b>`t`</b>: Tensor to check.
* <b>`msg`</b>: Message to log on failure.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Same tensor as `t`.