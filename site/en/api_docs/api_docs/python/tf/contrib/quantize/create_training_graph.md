

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.quantize.create_training_graph

``` python
tf.contrib.quantize.create_training_graph(
    input_graph=None,
    quant_delay=0
)
```



Defined in [`tensorflow/contrib/quantize/python/quantize_graph.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/quantize/python/quantize_graph.py).

Rewrites a training input_graph in place for simulated quantization.

Variables added by the rewrite get added to the global variables collection.

The graph has fake quantization ops inserted to simulate the error
introduced by quantization. Since the graph is transformed in place,
the expected behavior of previously held references to nodes and tensors may
change.

The default value of quant_delay is suitable for finetuning an already trained
floating point model (recommended).
If one wants to train a quantized model from scratch, quant_delay should be
set to the number of steps it take the floating point model to converge.
Quantization will be activated at this point and effectively finetune the
model. If quant_delay is not provided when training from scratch, training can
often fail.

#### Args:

* <b>`input_graph`</b>: The tf.Graph to be transformed.
* <b>`quant_delay`</b>: Number of steps after which weights and activations are
    quantized during training.


#### Raises:

* <b>`ValueError`</b>: If elements contains an element that isn't a tf.Tensor or
    tf.Operation.