

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.trace

### `tf.trace`

``` python
trace(
    x,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Compute the trace of a tensor `x`.

`trace(x)` returns the sum along the main diagonal of each inner-most matrix
in x. If x is of rank `k` with shape `[I, J, K, ..., L, M, N]`, then output
is a tensor of rank `k-2` with dimensions `[I, J, K, ..., L]` where

`output[i, j, k, ..., l] = trace(x[i, j, i, ..., l, :, :])`

For example:

```python
# 'x' is [[1, 2],
#         [3, 4]]
tf.trace(x) ==> 5

# 'x' is [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
tf.trace(x) ==> 15

# 'x' is [[[1,2,3],
#          [4,5,6],
#          [7,8,9]],
#         [[-1,-2,-3],
#          [-4,-5,-6],
#          [-7,-8,-9]]]
tf.trace(x) ==> [15,-15]
```

#### Args:

* <b>`x`</b>: tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  The trace of input tensor.