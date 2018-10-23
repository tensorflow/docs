

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.quantize.create_eval_graph

``` python
tf.contrib.quantize.create_eval_graph(input_graph=None)
```



Defined in [`tensorflow/contrib/quantize/python/quantize_graph.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/quantize/python/quantize_graph.py).

Rewrites an eval input_graph in place for simulated quantization.

The graph has fake quantization ops inserted to simulate the error
introduced by quantization. Since the graph is transformed in place,
the expected behavior of previously held references to nodes and tensors may
change.

#### Args:

* <b>`input_graph`</b>: The tf.Graph to be transformed, if None then defaults to the
    default graph.


#### Raises:

* <b>`ValueError`</b>: If elements contains an element that isn't a tf.Tensor or
    tf.Operation.