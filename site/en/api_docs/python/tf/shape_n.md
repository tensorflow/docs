page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.shape_n


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L489-L505">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns shape of tensors.

### Aliases:

* `tf.compat.v1.shape_n`
* `tf.compat.v2.shape_n`


``` python
tf.shape_n(
    input,
    out_type=tf.dtypes.int32,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: A list of at least 1 `Tensor` object with the same type.
* <b>`out_type`</b>: The specified output type of the operation (`int32` or `int64`).
  Defaults to <a href="../tf#int32"><code>tf.int32</code></a>(optional).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list with the same length as `input` of `Tensor` objects with
  type `out_type`.
