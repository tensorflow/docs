page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linspace


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Generates values in an interval.

### Aliases:

* `tf.compat.v1.lin_space`
* `tf.compat.v1.linspace`
* `tf.compat.v2.linspace`


``` python
tf.linspace(
    start,
    stop,
    num,
    name=None
)
```



<!-- Placeholder for "Used in" -->

A sequence of `num` evenly-spaced values are generated beginning at `start`.
If `num > 1`, the values in the sequence increase by `stop - start / num - 1`,
so that the last one is exactly `stop`.

#### For example:



```
tf.linspace(10.0, 12.0, 3, name="linspace") => [ 10.0  11.0  12.0]
```

#### Args:


* <b>`start`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `float64`.
  0-D tensor. First entry in the range.
* <b>`stop`</b>: A `Tensor`. Must have the same type as `start`.
  0-D tensor. Last entry in the range.
* <b>`num`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  0-D tensor. Number of values to generate.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `start`.
