page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.get_tensor_from_tensor_info


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/utils_impl.py#L136-L183">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/saved_model/get_tensor_from_tensor_info"><code>tf.compat.v1.saved_model.get_tensor_from_tensor_info</code></a>
* <a href="/api_docs/python/tf/saved_model/get_tensor_from_tensor_info"><code>tf.compat.v1.saved_model.utils.get_tensor_from_tensor_info</code></a>
* <a href="/api_docs/python/tf/saved_model/get_tensor_from_tensor_info"><code>tf.saved_model.utils.get_tensor_from_tensor_info</code></a>


``` python
tf.saved_model.get_tensor_from_tensor_info(
    tensor_info,
    graph=None,
    import_scope=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.utils.get_tensor_from_tensor_info or tf.compat.v1.saved_model.get_tensor_from_tensor_info.

#### Args:


* <b>`tensor_info`</b>: A TensorInfo proto describing a Tensor or SparseTensor or
  CompositeTensor.
* <b>`graph`</b>: The tf.Graph in which tensors are looked up. If None, the
    current default graph is used.
* <b>`import_scope`</b>: If not None, names in `tensor_info` are prefixed with this
    string before lookup.


#### Returns:

The Tensor or SparseTensor or CompositeTensor in `graph` described by
`tensor_info`.



#### Raises:


* <b>`KeyError`</b>: If `tensor_info` does not correspond to a tensor in `graph`.
* <b>`ValueError`</b>: If `tensor_info` is malformed.
