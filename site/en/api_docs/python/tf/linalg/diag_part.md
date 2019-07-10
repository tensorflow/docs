page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.diag_part

Returns the batched diagonal part of a batched tensor.

### Aliases:

* `tf.compat.v1.linalg.diag_part`
* `tf.compat.v1.matrix_diag_part`
* `tf.compat.v2.linalg.diag_part`
* `tf.linalg.diag_part`
* `tf.matrix_diag_part`

``` python
tf.linalg.diag_part(
    input,
    name=None
)
```



Defined in generated file: `python/ops/gen_array_ops.py`.

<!-- Placeholder for "Used in" -->

This operation returns a tensor with the `diagonal` part
of the batched `input`. The `diagonal` part is computed as follows:

Assume `input` has `k` dimensions `[I, J, K, ..., M, N]`, then the output is a
tensor of rank `k - 1` with dimensions `[I, J, K, ..., min(M, N)]` where:

`diagonal[i, j, k, ..., n] = input[i, j, k, ..., n, n]`.

The input must be at least a matrix.

#### For example:



```
# 'input' is [[[1, 0, 0, 0]
               [0, 2, 0, 0]
               [0, 0, 3, 0]
               [0, 0, 0, 4]],
              [[5, 0, 0, 0]
               [0, 6, 0, 0]
               [0, 0, 7, 0]
               [0, 0, 0, 8]]]

and input.shape = (2, 4, 4)

tf.matrix_diag_part(input) ==> [[1, 2, 3, 4], [5, 6, 7, 8]]

which has shape (2, 4)
```

#### Args:


* <b>`input`</b>: A `Tensor`. Rank `k` tensor where `k >= 2`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
