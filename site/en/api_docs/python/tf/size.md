page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.size

``` python
tf.size(
    input,
    name=None,
    out_type=tf.int32
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/array_ops.py).

Returns the size of a tensor.

Returns a 0-D `Tensor` representing the number of elements in `input`
of type `out_type`. Defaults to tf.int32.

For example:

```python
t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
tf.size(t)  # 12
```

#### Args:

* <b>`input`</b>: A `Tensor` or `SparseTensor`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`out_type`</b>: (Optional) The specified non-quantized numeric output type
    of the operation. Defaults to <a href="../tf#int32"><code>tf.int32</code></a>.


#### Returns:

A `Tensor` of type `out_type`. Defaults to <a href="../tf#int32"><code>tf.int32</code></a>.



#### Numpy Compatibility
Equivalent to np.size()

