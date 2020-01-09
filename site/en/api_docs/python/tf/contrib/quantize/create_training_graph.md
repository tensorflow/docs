page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.quantize.create_training_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/quantize/python/quantize_graph.py#L84-L122">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Rewrites a training input_graph in place for simulated quantization.

``` python
tf.contrib.quantize.create_training_graph(
    input_graph=None,
    quant_delay=0
)
```



<!-- Placeholder for "Used in" -->

Variables added by the rewrite get added to the global variables collection.

This function must be invoked prior to insertion of gradient ops in a graph
as quantization should be modeled in both forward and backward passes.

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
