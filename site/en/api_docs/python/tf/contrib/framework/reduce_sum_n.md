page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.reduce_sum_n

``` python
tf.contrib.framework.reduce_sum_n(
    tensors,
    name=None
)
```



Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/framework/python/framework/tensor_util.py).

See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Reduce tensors to a scalar sum.

This reduces each tensor in `tensors` to a scalar via <a href="../../../tf/reduce_sum"><code>tf.reduce_sum</code></a>, then
adds them via <a href="../../../tf/add_n"><code>tf.add_n</code></a>.

#### Args:

* <b>`tensors`</b>: List of tensors, all of the same numeric type.
* <b>`name`</b>: Tensor name, and scope for all other ops.


#### Returns:

Total loss tensor, or None if no losses have been configured.


#### Raises:

* <b>`ValueError`</b>: if `losses` is missing or empty.