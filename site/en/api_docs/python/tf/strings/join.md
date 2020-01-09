page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.join


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_string_ops.py`



Joins the strings in the given list of string tensors into one tensor;

### Aliases:

* `tf.compat.v1.string_join`
* `tf.compat.v1.strings.join`
* `tf.compat.v2.strings.join`


``` python
tf.strings.join(
    inputs,
    separator='',
    name=None
)
```



### Used in the guide:

* [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)



with the given separator (default is an empty separator).

#### Args:


* <b>`inputs`</b>: A list of at least 1 `Tensor` objects with type `string`.
  A list of string tensors.  The tensors must all have the same shape,
  or be scalars.  Scalars may be mixed in; these will be broadcast to the shape
  of non-scalar inputs.
* <b>`separator`</b>: An optional `string`. Defaults to `""`.
  string, an optional join separator.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
