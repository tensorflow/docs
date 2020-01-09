page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.invert_permutation


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Computes the inverse permutation of a tensor.

### Aliases:

* `tf.compat.v1.invert_permutation`
* `tf.compat.v1.math.invert_permutation`
* `tf.compat.v2.math.invert_permutation`


``` python
tf.math.invert_permutation(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation computes the inverse of an index permutation. It takes a 1-D
integer tensor `x`, which represents the indices of a zero-based array, and
swaps each value with its index position. In other words, for an output tensor
`y` and an input tensor `x`, this operation computes the following:

`y[x[i]] = i for i in [0, 1, ..., len(x) - 1]`

The values must include 0. There can be no duplicate values or negative values.

#### For example:



```
# tensor `x` is [3, 4, 0, 2, 1]
invert_permutation(x) ==> [2, 4, 3, 0, 1]
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
