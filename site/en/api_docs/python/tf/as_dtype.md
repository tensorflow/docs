page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.as_dtype

``` python
tf.as_dtype(type_value)
```



Defined in [`tensorflow/python/framework/dtypes.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/framework/dtypes.py).

See the guide: [Building Graphs > Tensor types](../../../api_guides/python/framework#Tensor_types)

Converts the given `type_value` to a `DType`.

#### Args:

* <b>`type_value`</b>: A value that can be converted to a <a href="../tf/DType"><code>tf.DType</code></a> object. This may
    currently be a <a href="../tf/DType"><code>tf.DType</code></a> object, a [`DataType`
    enum](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/core/framework/types.proto),
    a string type name, or a `numpy.dtype`.


#### Returns:

A `DType` corresponding to `type_value`.


#### Raises:

* <b>`TypeError`</b>: If `type_value` cannot be converted to a `DType`.