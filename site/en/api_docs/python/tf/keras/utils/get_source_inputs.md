page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.get_source_inputs

``` python
tf.keras.utils.get_source_inputs(
    tensor,
    layer=None,
    node_index=None
)
```



Defined in [`tensorflow/python/keras/utils/layer_utils.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/utils/layer_utils.py).

Returns the list of input tensors necessary to compute `tensor`.

Output will always be a list of tensors
(potentially with 1 element).

#### Arguments:

* <b>`tensor`</b>: The tensor to start from.
* <b>`layer`</b>: Origin layer of the tensor. Will be
        determined via tensor._keras_history if not provided.
* <b>`node_index`</b>: Origin node index of the tensor.


#### Returns:

List of input tensors.