page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tile


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/tile">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Constructs a tensor by tiling a given tensor.

### Aliases:

* <a href="/api_docs/python/tf/tile"><code>tf.compat.v1.manip.tile</code></a>
* <a href="/api_docs/python/tf/tile"><code>tf.compat.v1.tile</code></a>
* <a href="/api_docs/python/tf/tile"><code>tf.compat.v2.tile</code></a>
* <a href="/api_docs/python/tf/tile"><code>tf.manip.tile</code></a>


``` python
tf.tile(
    input,
    multiples,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation creates a new tensor by replicating `input` `multiples` times.
The output tensor's i'th dimension has `input.dims(i) * multiples[i]` elements,
and the values of `input` are replicated `multiples[i]` times along the 'i'th
dimension. For example, tiling `[a b c d]` by `[2]` produces
`[a b c d a b c d]`.

#### Args:


* <b>`input`</b>: A `Tensor`. 1-D or higher.
* <b>`multiples`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  1-D. Length must be the same as the number of dimensions in `input`
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
