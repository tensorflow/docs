page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.fill


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L136-L173">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a tensor filled with a scalar value.

### Aliases:

* `tf.compat.v1.fill`
* `tf.compat.v2.fill`


``` python
tf.fill(
    dims,
    value,
    name=None
)
```



### Used in the guide:

* [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)
* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Unicode strings](https://www.tensorflow.org/tutorials/load_data/unicode)



This operation creates a tensor of shape `dims` and fills it with `value`.

#### For example:



```
# Output tensor has shape [2, 3].
fill([2, 3], 9) ==> [[9, 9, 9]
                     [9, 9, 9]]
```

<a href="../tf/fill"><code>tf.fill</code></a> differs from <a href="../tf/constant"><code>tf.constant</code></a> in a few ways:

*   <a href="../tf/fill"><code>tf.fill</code></a> only supports scalar contents, whereas <a href="../tf/constant"><code>tf.constant</code></a> supports
    Tensor values.
*   <a href="../tf/fill"><code>tf.fill</code></a> creates an Op in the computation graph that constructs the
actual
    Tensor value at runtime. This is in contrast to <a href="../tf/constant"><code>tf.constant</code></a> which embeds
    the entire Tensor into the graph with a `Const` node.
*   Because <a href="../tf/fill"><code>tf.fill</code></a> evaluates at graph runtime, it supports dynamic shapes
    based on other runtime Tensors, unlike <a href="../tf/constant"><code>tf.constant</code></a>.

#### Args:


* <b>`dims`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D.
  Represents the shape of the output tensor.
* <b>`value`</b>: A `Tensor`. 0-D (scalar). Value to fill the returned tensor.
  @compatibility(numpy) Equivalent to np.full @end_compatibility
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `value`.
