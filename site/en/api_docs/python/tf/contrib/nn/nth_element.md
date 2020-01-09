page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.nn.nth_element


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L4350-L4377">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Finds values of the `n`-th smallest value for the last dimension.

``` python
tf.contrib.nn.nth_element(
    input,
    n,
    reverse=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Note that n is zero-indexed.

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
