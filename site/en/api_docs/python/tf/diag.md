page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.diag

### Aliases:

* `tf.diag`
* `tf.linalg.tensor_diag`

``` python
tf.diag(
    diagonal,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_array_ops.py`.

See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Returns a diagonal tensor with a given diagonal values.

Given a `diagonal`, this operation returns a tensor with the `diagonal` and
everything else padded with zeros. The diagonal is computed as follows:

Assume `diagonal` has dimensions [D1,..., Dk], then the output is a tensor of
rank 2k with dimensions [D1,..., Dk, D1,..., Dk] where:

`output[i1,..., ik, i1,..., ik] = diagonal[i1, ..., ik]` and 0 everywhere else.

For example:

```
# 'diagonal' is [1, 2, 3, 4]
tf.diag(diagonal) ==> [[1, 0, 0, 0]
                       [0, 2, 0, 0]
                       [0, 0, 3, 0]
                       [0, 0, 0, 4]]
```

#### Args:

* <b>`diagonal`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
    Rank k tensor where k is at most 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `diagonal`.