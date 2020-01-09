page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.as_dtype


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/dtypes/as_dtype">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/dtypes.py#L690-L721">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts the given `type_value` to a `DType`.

### Aliases:

* <a href="/api_docs/python/tf/dtypes/as_dtype"><code>tf.as_dtype</code></a>
* <a href="/api_docs/python/tf/dtypes/as_dtype"><code>tf.compat.v1.as_dtype</code></a>
* <a href="/api_docs/python/tf/dtypes/as_dtype"><code>tf.compat.v1.dtypes.as_dtype</code></a>
* <a href="/api_docs/python/tf/dtypes/as_dtype"><code>tf.compat.v2.as_dtype</code></a>
* <a href="/api_docs/python/tf/dtypes/as_dtype"><code>tf.compat.v2.dtypes.as_dtype</code></a>


``` python
tf.dtypes.as_dtype(type_value)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`type_value`</b>: A value that can be converted to a <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> object. This may
  currently be a <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> object, a [`DataType`
  enum](https://www.tensorflow.org/code/tensorflow/core/framework/types.proto),
    a string type name, or a `numpy.dtype`.


#### Returns:

A `DType` corresponding to `type_value`.



#### Raises:


* <b>`TypeError`</b>: If `type_value` cannot be converted to a `DType`.
