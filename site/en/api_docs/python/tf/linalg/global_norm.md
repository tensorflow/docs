page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.global_norm

### Aliases:

* `tf.global_norm`
* `tf.linalg.global_norm`

``` python
tf.linalg.global_norm(
    t_list,
    name=None
)
```



Defined in [`tensorflow/python/ops/clip_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/clip_ops.py).

Computes the global norm of multiple tensors.

Given a tuple or list of tensors `t_list`, this operation returns the
global norm of the elements in all tensors in `t_list`. The global norm is
computed as:

`global_norm = sqrt(sum([l2norm(t)**2 for t in t_list]))`

Any entries in `t_list` that are of type None are ignored.

#### Args:

* <b>`t_list`</b>: A tuple or list of mixed `Tensors`, `IndexedSlices`, or None.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A 0-D (scalar) `Tensor` of type `float`.


#### Raises:

* <b>`TypeError`</b>: If `t_list` is not a sequence.