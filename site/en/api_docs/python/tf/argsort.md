page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.argsort

Returns the indices of a tensor that give its sorted order along an axis.

### Aliases:

* `tf.argsort`
* `tf.compat.v1.argsort`
* `tf.compat.v2.argsort`
* `tf.contrib.framework.argsort`

``` python
tf.argsort(
    values,
    axis=-1,
    direction='ASCENDING',
    stable=False,
    name=None
)
```



Defined in [`python/ops/sort_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/sort_ops.py).

<!-- Placeholder for "Used in" -->

For a 1D tensor, `tf.gather(values, tf.argsort(values))` is equivalent to
<a href="../tf/sort"><code>tf.sort(values)</code></a>. For higher dimensions, the output has the same shape as
`values`, but along the given axis, values represent the index of the sorted
element in that slice of the tensor at the given position.

#### Usage:



```python
import tensorflow as tf
a = [1, 10, 26.9, 2.8, 166.32, 62.3]
b = tf.argsort(a,axis=-1,direction='ASCENDING',stable=False,name=None)
c = tf.keras.backend.eval(b)
# Here, c = [0 3 1 2 5 4]
```

#### Args:


* <b>`values`</b>: 1-D or higher numeric `Tensor`.
* <b>`axis`</b>: The axis along which to sort. The default is -1, which sorts the last
  axis.
* <b>`direction`</b>: The direction in which to sort the values (`'ASCENDING'` or
  `'DESCENDING'`).
* <b>`stable`</b>: If True, equal elements in the original tensor will not be
  re-ordered in the returned order. Unstable sort is not yet implemented,
  but will eventually be the default for performance reasons. If you require
  a stable order, pass `stable=True` for forwards compatibility.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

An int32 `Tensor` with the same shape as `values`. The indices that would
    sort each slice of the given `values` along the given `axis`.



#### Raises:


* <b>`ValueError`</b>: If axis is not a constant scalar, or the direction is invalid.