page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.saturate_cast


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L710-L740">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Performs a safe saturating cast of `value` to `dtype`.

### Aliases:

* `tf.compat.v1.dtypes.saturate_cast`
* `tf.compat.v1.saturate_cast`
* `tf.compat.v2.dtypes.saturate_cast`
* `tf.compat.v2.saturate_cast`
* `tf.saturate_cast`


``` python
tf.dtypes.saturate_cast(
    value,
    dtype,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This function casts the input to `dtype` without applying any scaling.  If
there is a danger that values would over or underflow in the cast, this op
applies the appropriate clamping before the cast.

#### Args:


* <b>`value`</b>: A `Tensor`.
* <b>`dtype`</b>: The desired output `DType`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`value` safely cast to `dtype`.
