page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.searchsorted


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L4481-L4539">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Searches input tensor for values on the innermost dimension.

### Aliases:

* `tf.compat.v1.searchsorted`
* `tf.compat.v2.searchsorted`


``` python
tf.searchsorted(
    sorted_sequence,
    values,
    side='left',
    out_type=tf.dtypes.int32,
    name=None
)
```



<!-- Placeholder for "Used in" -->

A 2-D example:

```
  sorted_sequence = [[0, 3, 9, 9, 10],
                     [1, 2, 3, 4, 5]]
  values = [[2, 4, 9],
            [0, 2, 6]]

  result = searchsorted(sorted_sequence, values, side="left")

  result == [[1, 2, 2],
             [0, 1, 5]]

  result = searchsorted(sorted_sequence, values, side="right")

  result == [[1, 2, 4],
             [0, 2, 5]]
```

#### Args:


* <b>`sorted_sequence`</b>: N-D `Tensor` containing a sorted sequence.
* <b>`values`</b>: N-D `Tensor` containing the search values.
* <b>`side`</b>: 'left' or 'right'; 'left' corresponds to lower_bound and 'right' to
  upper_bound.
* <b>`out_type`</b>: The output type (`int32` or `int64`).  Default is <a href="../tf#int32"><code>tf.int32</code></a>.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

An N-D `Tensor` the size of values containing the result of applying either
lower_bound or upper_bound (depending on side) to each value.  The result
is not a global index to the entire `Tensor`, but the index in the last
dimension.



#### Raises:


* <b>`ValueError`</b>: If the last dimension of `sorted_sequence >= 2^31-1` elements.
            If the total size of values exceeds `2^31 - 1` elements.
            If the first `N-1` dimensions of the two tensors don't match.
