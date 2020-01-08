page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.all_reduce.build_nccl_all_reduce

``` python
tf.contrib.all_reduce.build_nccl_all_reduce(
    input_tensors,
    red_op,
    un_op=None
)
```



Defined in [`tensorflow/contrib/all_reduce/python/all_reduce.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/all_reduce/python/all_reduce.py).

Build a subgraph that does one full all-reduce, using NCCL.

#### Args:

* <b>`input_tensors`</b>: list of T <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of same-shape and type values to
    be reduced.
* <b>`red_op`</b>: binary elementwise reduction operator.  Must be one of
    {tf.add}
* <b>`un_op`</b>: optional unary elementwise Op to apply to fully-reduce values.


#### Returns:

list of T <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of reduced values.


#### Raises:

* <b>`ValueError`</b>: red_op not supported.