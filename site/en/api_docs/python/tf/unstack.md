page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.unstack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/unstack">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L1278-L1323">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Unpacks the given dimension of a rank-`R` tensor into rank-`(R-1)` tensors.

### Aliases:

* <a href="/api_docs/python/tf/unstack"><code>tf.compat.v1.unstack</code></a>
* <a href="/api_docs/python/tf/unstack"><code>tf.compat.v2.unstack</code></a>


``` python
tf.unstack(
    value,
    num=None,
    axis=0,
    name='unstack'
)
```



<!-- Placeholder for "Used in" -->

Unpacks `num` tensors from `value` by chipping it along the `axis` dimension.
If `num` is not specified (the default), it is inferred from `value`'s shape.
If `value.shape[axis]` is not known, `ValueError` is raised.

For example, given a tensor of shape `(A, B, C, D)`;

If `axis == 0` then the i'th tensor in `output` is the slice
  `value[i, :, :, :]` and each tensor in `output` will have shape `(B, C, D)`.
  (Note that the dimension unpacked along is gone, unlike `split`).

If `axis == 1` then the i'th tensor in `output` is the slice
  `value[:, i, :, :]` and each tensor in `output` will have shape `(A, C, D)`.
Etc.

This is the opposite of stack.

#### Args:


* <b>`value`</b>: A rank `R > 0` `Tensor` to be unstacked.
* <b>`num`</b>: An `int`. The length of the dimension `axis`. Automatically inferred if
  `None` (the default).
* <b>`axis`</b>: An `int`. The axis to unstack along. Defaults to the first dimension.
  Negative values wrap around, so the valid range is `[-R, R)`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The list of `Tensor` objects unstacked from `value`.



#### Raises:


* <b>`ValueError`</b>: If `num` is unspecified and cannot be inferred.
* <b>`ValueError`</b>: If `axis` is out of the range [-R, R).
