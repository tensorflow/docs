page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.convert_to_tensor_or_indexed_slices


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/indexed_slices.py#L249-L271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts the given object to a `Tensor` or an `IndexedSlices`.

### Aliases:

* <a href="/api_docs/python/tf/convert_to_tensor_or_indexed_slices"><code>tf.compat.v1.convert_to_tensor_or_indexed_slices</code></a>


``` python
tf.convert_to_tensor_or_indexed_slices(
    value,
    dtype=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If `value` is an `IndexedSlices` or `SparseTensor` it is returned
unmodified. Otherwise, it is converted to a `Tensor` using
`convert_to_tensor()`.

#### Args:


* <b>`value`</b>: An `IndexedSlices`, `SparseTensor`, or an object that can be consumed
  by `convert_to_tensor()`.
* <b>`dtype`</b>: (Optional.) The required `DType` of the returned `Tensor` or
  `IndexedSlices`.
* <b>`name`</b>: (Optional.) A name to use if a new `Tensor` is created.


#### Returns:

A `Tensor`, `IndexedSlices`, or `SparseTensor` based on `value`.



#### Raises:


* <b>`ValueError`</b>: If `dtype` does not match the element type of `value`.
