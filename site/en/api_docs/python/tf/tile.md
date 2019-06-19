page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tile

``` python
tf.tile(
    input,
    multiples,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_array_ops.py`.

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Constructs a tensor by tiling a given tensor.

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