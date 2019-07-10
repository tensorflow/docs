page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.tensor_list

``` python
tf.contrib.autograph.tensor_list(
    elements,
    element_dtype=None,
    element_shape=None,
    use_tensor_array=False
)
```



Defined in [`tensorflow/python/autograph/lang/special_functions.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/autograph/lang/special_functions.py).

Creates an tensor list and populates it with the given elements.

This function provides a more uniform access to tensor lists and tensor
arrays, and allows optional initialization.

Note: this function is a simplified wrapper. If you need greater control,
it is recommended to use the underlying implementation directly.

#### Args:

* <b>`elements`</b>: Iterable[tf.Tensor, ...], the elements to initially fill the list
      with
* <b>`element_dtype`</b>: Optional[tf.DType], data type for the elements in the list;
      required if the list is empty
* <b>`element_shape`</b>: Optional[tf.TensorShape], shape for the elements in the list;
      required if the list is empty
* <b>`use_tensor_array`</b>: bool, whether to use the more compatible but restrictive
      tf.TensorArray implementation

#### Returns:

Union[tf.Tensor, tf.TensorArray], the new list.

#### Raises:

* <b>`ValueError`</b>: for invalid arguments