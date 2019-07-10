page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sort

### Aliases:

* `tf.contrib.framework.sort`
* `tf.sort`

``` python
tf.sort(
    values,
    axis=-1,
    direction='ASCENDING',
    name=None
)
```



Defined in [`tensorflow/python/ops/sort_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/sort_ops.py).

Sorts a tensor.

#### Args:

* <b>`values`</b>: 1-D or higher numeric `Tensor`.
* <b>`axis`</b>: The axis along which to sort. The default is -1, which sorts the last
    axis.
* <b>`direction`</b>: The direction in which to sort the values (`'ASCENDING'` or
    `'DESCENDING'`).
* <b>`name`</b>: Optional name for the operation.


#### Returns:

A `Tensor` with the same dtype and shape as `values`, with the elements
    sorted along the given `axis`.


#### Raises:

* <b>`ValueError`</b>: If axis is not a constant scalar, or the direction is invalid.