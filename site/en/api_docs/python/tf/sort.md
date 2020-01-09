page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sort


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sort_ops.py#L36-L66">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sorts a tensor.

### Aliases:

* `tf.compat.v1.sort`
* `tf.compat.v2.sort`


``` python
tf.sort(
    values,
    axis=-1,
    direction='ASCENDING',
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Usage:



```python
import tensorflow as tf
a = [1, 10, 26.9, 2.8, 166.32, 62.3]
b = tf.sort(a,axis=-1,direction='ASCENDING',name=None)
c = tf.keras.backend.eval(b)
# Here, c = [  1.     2.8   10.    26.9   62.3  166.32]
```

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
