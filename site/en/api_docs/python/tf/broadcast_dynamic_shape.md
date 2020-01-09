page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.broadcast_dynamic_shape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/broadcast_dynamic_shape">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L346-L368">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the shape of a broadcast given symbolic shapes.

### Aliases:

* <a href="/api_docs/python/tf/broadcast_dynamic_shape"><code>tf.compat.v1.broadcast_dynamic_shape</code></a>
* <a href="/api_docs/python/tf/broadcast_dynamic_shape"><code>tf.compat.v2.broadcast_dynamic_shape</code></a>


``` python
tf.broadcast_dynamic_shape(
    shape_x,
    shape_y
)
```



<!-- Placeholder for "Used in" -->

When shape_x and shape_y are Tensors representing shapes (i.e. the result of
calling tf.shape on another Tensor) this computes a Tensor which is the shape
of the result of a broadcasting op applied in tensors of shapes shape_x and
shape_y.

For example, if shape_x is [1, 2, 3] and shape_y is [5, 1, 3], the result is a
Tensor whose value is [5, 2, 3].

This is useful when validating the result of a broadcasting operation when the
tensors do not have statically known shapes.

#### Args:


* <b>`shape_x`</b>: A rank 1 integer `Tensor`, representing the shape of x.
* <b>`shape_y`</b>: A rank 1 integer `Tensor`, representing the shape of y.


#### Returns:

A rank 1 integer `Tensor` representing the broadcasted shape.
