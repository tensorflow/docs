page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.clip_gradients_by_global_norm

Clips gradients of a multitask loss by their global norm.

``` python
tf.contrib.opt.clip_gradients_by_global_norm(
    gradients_variables,
    clip_norm=20.0
)
```



Defined in [`contrib/opt/python/training/multitask_optimizer_wrapper.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/opt/python/training/multitask_optimizer_wrapper.py).

<!-- Placeholder for "Used in" -->

Ignores all-zero tensors when computing the global norm.

#### Args:


* <b>`gradients_variables`</b>: a list of pairs (gradient, variable).
* <b>`clip_norm`</b>: a float Tensor, the global norm to clip on. Default is 20.0.


#### Returns:


* <b>`list`</b>: A list of pairs of the same type as gradients_variables,.
* <b>`fixed_global_norm`</b>: A 0-D (scalar) Tensor representing the global norm.