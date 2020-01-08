page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.searchsorted

``` python
tf.searchsorted(
    sorted_sequence,
    values,
    side='left',
    out_type=tf.int32,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/array_ops.py).

Searches input tensor for values on the innermost dimension.

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