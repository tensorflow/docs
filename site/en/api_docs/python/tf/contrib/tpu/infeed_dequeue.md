page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.infeed_dequeue

``` python
tf.contrib.tpu.infeed_dequeue(
    dtype,
    shape,
    name=None
)
```



Defined in [`tensorflow/contrib/tpu/python/ops/tpu_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/tpu/python/ops/tpu_ops.py).

A placeholder op for a value that will be fed into the computation.

#### Args:

* <b>`dtype`</b>: A <a href="../../../tf/dtypes/DType"><code>tf.DType</code></a>. The type of elements in the tensor.
* <b>`shape`</b>: A <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> or list of `ints`. The shape of the tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `dtype`.
A tensor that will be provided using the infeed mechanism.


#### Raises:

* <b>`TypeError`</b>: If 'dtype` is not a supported infeed type.