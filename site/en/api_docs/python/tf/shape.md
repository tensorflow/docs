page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.shape

Returns the shape of a tensor.

### Aliases:

* `tf.compat.v1.shape`
* `tf.shape`

``` python
tf.shape(
    input,
    name=None,
    out_type=tf.dtypes.int32
)
```



Defined in [`python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/array_ops.py).

<!-- Placeholder for "Used in" -->

This operation returns a 1-D integer tensor representing the shape of `input`.

#### For example:



```python
t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
tf.shape(t)  # [2, 2, 3]
```

#### Args:


* <b>`input`</b>: A `Tensor` or `SparseTensor`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`out_type`</b>: (Optional) The specified output type of the operation (`int32` or
  `int64`). Defaults to <a href="../tf#int32"><code>tf.int32</code></a>.


#### Returns:

A `Tensor` of type `out_type`.
