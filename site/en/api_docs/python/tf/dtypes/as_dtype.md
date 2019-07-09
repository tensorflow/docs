page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.as_dtype

### Aliases:

* `tf.as_dtype`
* `tf.dtypes.as_dtype`

``` python
tf.dtypes.as_dtype(type_value)
```



Defined in [`tensorflow/python/framework/dtypes.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/dtypes.py).

Converts the given `type_value` to a `DType`.

#### Args:

* <b>`type_value`</b>: A value that can be converted to a <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> object. This may
    currently be a <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> object, a [`DataType`
    enum](https://www.github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/core/framework/types.proto),
    a string type name, or a `numpy.dtype`.


#### Returns:

A `DType` corresponding to `type_value`.


#### Raises:

* <b>`TypeError`</b>: If `type_value` cannot be converted to a `DType`.