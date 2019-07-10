page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.clip_by_value

Clips tensor values to a specified min and max.

### Aliases:

* `tf.clip_by_value`
* `tf.compat.v1.clip_by_value`
* `tf.compat.v2.clip_by_value`

``` python
tf.clip_by_value(
    t,
    clip_value_min,
    clip_value_max,
    name=None
)
```



Defined in [`python/ops/clip_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/clip_ops.py).

<!-- Placeholder for "Used in" -->

Given a tensor `t`, this operation returns a tensor of the same type and
shape as `t` with its values clipped to `clip_value_min` and `clip_value_max`.
Any values less than `clip_value_min` are set to `clip_value_min`. Any values
greater than `clip_value_max` are set to `clip_value_max`.

Note: `clip_value_min` needs to be smaller or equal to `clip_value_max` for
correct results.

#### Args:


* <b>`t`</b>: A `Tensor` or `IndexedSlices`.
* <b>`clip_value_min`</b>: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shape
  as `t`. The minimum value to clip by.
* <b>`clip_value_max`</b>: A 0-D (scalar) `Tensor`, or a `Tensor` with the same shape
  as `t`. The maximum value to clip by.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A clipped `Tensor` or `IndexedSlices`.



#### Raises:


* <b>`ValueError`</b>: If the clip tensors would trigger array broadcasting
  that would make the returned tensor larger than the input.