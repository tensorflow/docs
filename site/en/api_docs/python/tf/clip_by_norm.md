page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.clip_by_norm


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/clip_by_norm">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/clip_ops.py#L125-L184">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Clips tensor values to a maximum L2-norm.

### Aliases:

* <a href="/api_docs/python/tf/clip_by_norm"><code>tf.compat.v1.clip_by_norm</code></a>
* <a href="/api_docs/python/tf/clip_by_norm"><code>tf.compat.v2.clip_by_norm</code></a>


``` python
tf.clip_by_norm(
    t,
    clip_norm,
    axes=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `t`, and a maximum clip value `clip_norm`, this operation
normalizes `t` so that its L2-norm is less than or equal to `clip_norm`,
along the dimensions given in `axes`. Specifically, in the default case
where all dimensions are used for calculation, if the L2-norm of `t` is
already less than or equal to `clip_norm`, then `t` is not modified. If
the L2-norm is greater than `clip_norm`, then this operation returns a
tensor of the same type and shape as `t` with its values set to:

`t * clip_norm / l2norm(t)`

In this case, the L2-norm of the output tensor is `clip_norm`.

As another example, if `t` is a matrix and `axes == [1]`, then each row
of the output will have L2-norm less than or equal to `clip_norm`. If
`axes == [0]` instead, each column of the output will be clipped.

This operation is typically used to clip gradients before applying them with
an optimizer.

#### Args:


* <b>`t`</b>: A `Tensor` or `IndexedSlices`.
* <b>`clip_norm`</b>: A 0-D (scalar) `Tensor` > 0. A maximum clipping value.
* <b>`axes`</b>: A 1-D (vector) `Tensor` of type int32 containing the dimensions
  to use for computing the L2-norm. If `None` (the default), uses all
  dimensions.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A clipped `Tensor` or `IndexedSlices`.



#### Raises:


* <b>`ValueError`</b>: If the clip_norm tensor is not a 0-D scalar tensor.
* <b>`TypeError`</b>: If dtype of the input is not a floating point or
  complex type.
