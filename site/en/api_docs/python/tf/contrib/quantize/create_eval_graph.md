

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.quantize.create_eval_graph

``` python
tf.contrib.quantize.create_eval_graph(
    input_graph,
    elements=None,
    device_name_or_function=None
)
```



Defined in [`tensorflow/contrib/quantize/python/quantize_graph.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/quantize/python/quantize_graph.py).

Returns a transformed eval input_graph for simulated quantization.

The forward pass has fake quantization ops inserted to simulate the error
introduced by quantization.

#### Args:

* <b>`input_graph`</b>: The tf.Graph to be transformed.
* <b>`elements`</b>: (Optional) List of Tensors and Operations in input_graph whose
      corresponding elements in the new graph will be returned.
* <b>`device_name_or_function`</b>: (Optional) The device name or function to use.


#### Returns:

g is new tf.Graph that is rewritten for simulated quantization.
l is a list of Tensors/Operations in g corresponding to the provided input
    elements, if elements is not None.


#### Raises:

* <b>`ValueError`</b>: If elements contains an element that isn't a tf.Tensor or
      tf.Operation.