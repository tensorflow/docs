

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.nn.nth_element

``` python
nth_element(
    input,
    n,
    reverse=False,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/nn_ops.py).

Finds values of the `n`-th order statistic for the last dmension.

If the input is a vector (rank-1), finds the entries which is the nth-smallest
value in the vector and outputs their values as scalar tensor.

For matrices (resp. higher rank input), computes the entries which is the
nth-smallest value in each row (resp. vector along the last dimension). Thus,

    values.shape = input.shape[:-1]

#### Args:

* <b>`input`</b>: 1-D or higher `Tensor` with last dimension at least `n+1`.
* <b>`n`</b>: A `Tensor` of type `int32`.
    0-D. Position of sorted vector to select along the last dimension (along
    each row for matrices). Valid range of n is `[0, input.shape[:-1])`
* <b>`reverse`</b>: An optional `bool`. Defaults to `False`.
    When set to True, find the nth-largest value in the vector and vice
    versa.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
The `n`-th order statistic along each last dimensional slice.