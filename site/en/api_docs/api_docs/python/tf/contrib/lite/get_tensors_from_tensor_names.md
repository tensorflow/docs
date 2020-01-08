

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.get_tensors_from_tensor_names

``` python
tf.contrib.lite.get_tensors_from_tensor_names(
    graph,
    tensor_names
)
```



Defined in [`tensorflow/contrib/lite/python/convert_saved_model.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/lite/python/convert_saved_model.py).

Gets the Tensors associated with the `tensor_names` in the provided graph.

#### Args:

* <b>`graph`</b>: TensorFlow Graph.
* <b>`tensor_names`</b>: List of strings that represent names of tensors in the graph.


#### Returns:

A list of Tensor objects in the same order the names are provided.


#### Raises:

* <b>`ValueError`</b>:     tensor_names contains an invalid tensor name.