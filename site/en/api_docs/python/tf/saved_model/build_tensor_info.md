page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.build_tensor_info


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/utils_impl.py#L44-L67">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Utility function to build TensorInfo proto from a Tensor. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/saved_model/build_tensor_info"><code>tf.compat.v1.saved_model.build_tensor_info</code></a>
* <a href="/api_docs/python/tf/saved_model/build_tensor_info"><code>tf.compat.v1.saved_model.utils.build_tensor_info</code></a>
* <a href="/api_docs/python/tf/saved_model/build_tensor_info"><code>tf.saved_model.utils.build_tensor_info</code></a>


``` python
tf.saved_model.build_tensor_info(tensor)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.utils.build_tensor_info or tf.compat.v1.saved_model.build_tensor_info.

#### Args:


* <b>`tensor`</b>: Tensor or SparseTensor whose name, dtype and shape are used to
    build the TensorInfo. For SparseTensors, the names of the three
    constituent Tensors are used.


#### Returns:

A TensorInfo protocol buffer constructed based on the supplied argument.



#### Raises:


* <b>`RuntimeError`</b>: If eager execution is enabled.
