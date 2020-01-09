page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.convert_to_tensor_or_sparse_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/sparse_tensor.py#L388-L414">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts value to a `SparseTensor` or `Tensor`.

### Aliases:

* <a href="/api_docs/python/tf/convert_to_tensor_or_sparse_tensor"><code>tf.compat.v1.convert_to_tensor_or_sparse_tensor</code></a>
* <a href="/api_docs/python/tf/convert_to_tensor_or_sparse_tensor"><code>tf.contrib.framework.convert_to_tensor_or_sparse_tensor</code></a>


``` python
tf.convert_to_tensor_or_sparse_tensor(
    value,
    dtype=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`value`</b>: A `SparseTensor`, `SparseTensorValue`, or an object whose type has a
  registered `Tensor` conversion function.
* <b>`dtype`</b>: Optional element type for the returned tensor. If missing, the type
  is inferred from the type of `value`.
* <b>`name`</b>: Optional name to use if a new `Tensor` is created.


#### Returns:

A `SparseTensor` or `Tensor` based on `value`.



#### Raises:


* <b>`RuntimeError`</b>: If result type is incompatible with `dtype`.
