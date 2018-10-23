

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.placeholder_with_default

``` python
tf.placeholder_with_default(
    input,
    shape,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_array_ops.py`.

See the guide: [Inputs and Readers > Placeholders](../../../api_guides/python/io_ops#Placeholders)

A placeholder op that passes through `input` when its output is not fed.

#### Args:

* <b>`input`</b>: A `Tensor`. The default value to produce when `output` is not fed.
* <b>`shape`</b>: A `tf.TensorShape` or list of `ints`.
    The (possibly partial) shape of the tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.