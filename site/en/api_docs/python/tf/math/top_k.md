page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.top_k


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L4320-L4347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Finds values and indices of the `k` largest entries for the last dimension.

### Aliases:

* `tf.compat.v1.math.top_k`
* `tf.compat.v1.nn.top_k`
* `tf.compat.v2.math.top_k`
* `tf.compat.v2.nn.top_k`
* `tf.nn.top_k`


``` python
tf.math.top_k(
    input,
    k=1,
    sorted=True,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If the input is a vector (rank=1), finds the `k` largest entries in the vector
and outputs their values and indices as vectors.  Thus `values[j]` is the
`j`-th largest entry in `input`, and its index is `indices[j]`.

For matrices (resp. higher rank input), computes the top `k` entries in each
row (resp. vector along the last dimension).  Thus,

    values.shape = indices.shape = input.shape[:-1] + [k]

If two elements are equal, the lower-index element appears first.

#### Args:


* <b>`input`</b>: 1-D or higher `Tensor` with last dimension at least `k`.
* <b>`k`</b>: 0-D `int32` `Tensor`.  Number of top elements to look for along the last
  dimension (along each row for matrices).
* <b>`sorted`</b>: If true the resulting `k` elements will be sorted by the values in
  descending order.
* <b>`name`</b>: Optional name for the operation.


#### Returns:


* <b>`values`</b>: The `k` largest elements along each last dimensional slice.
* <b>`indices`</b>: The indices of `values` within the last dimension of `input`.
