page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.band_part


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Copy a tensor setting everything outside a central band in each innermost matrix

### Aliases:

* `tf.compat.v1.linalg.band_part`
* `tf.compat.v1.matrix_band_part`
* `tf.compat.v2.linalg.band_part`


``` python
tf.linalg.band_part(
    input,
    num_lower,
    num_upper,
    name=None
)
```



### Used in the tutorials:

* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



to zero.

The `band` part is computed as follows:
Assume `input` has `k` dimensions `[I, J, K, ..., M, N]`, then the output is a
tensor with the same shape where

`band[i, j, k, ..., m, n] = in_band(m, n) * input[i, j, k, ..., m, n]`.

The indicator function

`in_band(m, n) = (num_lower < 0 || (m-n) <= num_lower)) &&
                 (num_upper < 0 || (n-m) <= num_upper)`.

#### For example:



```
# if 'input' is [[ 0,  1,  2, 3]
                 [-1,  0,  1, 2]
                 [-2, -1,  0, 1]
                 [-3, -2, -1, 0]],

tf.matrix_band_part(input, 1, -1) ==> [[ 0,  1,  2, 3]
                                       [-1,  0,  1, 2]
                                       [ 0, -1,  0, 1]
                                       [ 0,  0, -1, 0]],

tf.matrix_band_part(input, 2, 1) ==> [[ 0,  1,  0, 0]
                                      [-1,  0,  1, 0]
                                      [-2, -1,  0, 1]
                                      [ 0, -2, -1, 0]]
```

#### Useful special cases:



```
 tf.matrix_band_part(input, 0, -1) ==> Upper triangular part.
 tf.matrix_band_part(input, -1, 0) ==> Lower triangular part.
 tf.matrix_band_part(input, 0, 0) ==> Diagonal.
```

#### Args:


* <b>`input`</b>: A `Tensor`. Rank `k` tensor.
* <b>`num_lower`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  0-D tensor. Number of subdiagonals to keep. If negative, keep entire
  lower triangle.
* <b>`num_upper`</b>: A `Tensor`. Must have the same type as `num_lower`.
  0-D tensor. Number of superdiagonals to keep. If negative, keep
  entire upper triangle.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
