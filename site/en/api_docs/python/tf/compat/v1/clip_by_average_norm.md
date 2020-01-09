page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.clip_by_average_norm


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/clip_ops.py#L328-L372">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Clips tensor values to a maximum average L2-norm. (deprecated)

``` python
tf.compat.v1.clip_by_average_norm(
    t,
    clip_norm,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
clip_by_average_norm is deprecated in TensorFlow 2.0. Please use clip_by_norm(t, clip_norm * tf.cast(tf.size(t), tf.float32), name) instead.

Given a tensor `t`, and a maximum clip value `clip_norm`, this operation
normalizes `t` so that its average L2-norm is less than or equal to
`clip_norm`. Specifically, if the average L2-norm is already less than or
equal to `clip_norm`, then `t` is not modified. If the average L2-norm is
greater than `clip_norm`, then this operation returns a tensor of the same
type and shape as `t` with its values set to:

`t * clip_norm / l2norm_avg(t)`

In this case, the average L2-norm of the output tensor is `clip_norm`.

This operation is typically used to clip gradients before applying them with
an optimizer.

#### Args:


* <b>`t`</b>: A `Tensor`.
* <b>`clip_norm`</b>: A 0-D (scalar) `Tensor` > 0. A maximum clipping value.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A clipped `Tensor`.
