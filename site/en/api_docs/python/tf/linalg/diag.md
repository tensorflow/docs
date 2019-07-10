page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.diag

Returns a batched diagonal tensor with a given batched diagonal values.

### Aliases:

* `tf.compat.v1.linalg.diag`
* `tf.compat.v1.matrix_diag`
* `tf.compat.v2.linalg.diag`
* `tf.linalg.diag`
* `tf.matrix_diag`

``` python
tf.linalg.diag(
    diagonal,
    name=None
)
```



Defined in generated file: `python/ops/gen_array_ops.py`.

<!-- Placeholder for "Used in" -->

Given a `diagonal`, this operation returns a tensor with the `diagonal` and
everything else padded with zeros. The diagonal is computed as follows:

Assume `diagonal` has `k` dimensions `[I, J, K, ..., N]`, then the output is a
tensor of rank `k+1` with dimensions [I, J, K, ..., N, N]` where:

`output[i, j, k, ..., m, n] = 1{m=n} * diagonal[i, j, k, ..., n]`.

#### For example:



```
# 'diagonal' is [[1, 2, 3, 4], [5, 6, 7, 8]]

and diagonal.shape = (2, 4)

tf.matrix_diag(diagonal) ==> [[[1, 0, 0, 0]
                                     [0, 2, 0, 0]
                                     [0, 0, 3, 0]
                                     [0, 0, 0, 4]],
                                    [[5, 0, 0, 0]
                                     [0, 6, 0, 0]
                                     [0, 0, 7, 0]
                                     [0, 0, 0, 8]]]

which has shape (2, 4, 4)
```

#### Args:


* <b>`diagonal`</b>: A `Tensor`. Rank `k`, where `k >= 1`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `diagonal`.
