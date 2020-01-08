

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.quantize.experimental_create_training_graph

``` python
tf.contrib.quantize.experimental_create_training_graph(
    input_graph=None,
    weight_bits=8,
    activation_bits=8,
    quant_delay=0,
    freeze_bn_delay=None,
    scope=None
)
```



Defined in [`tensorflow/contrib/quantize/python/quantize_graph.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/quantize/python/quantize_graph.py).

Rewrites a training input_graph in place for simulated quantization.

Variables added by the rewrite get added to the global variables collection.

This function has additional experimental options not (yet) available to
create_training_graph. The resulting behavior may be undefined.

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

* <b>`input_graph`</b>: The tf.Graph to be transformed, if None then defaults to the
    default graph.
* <b>`weight_bits`</b>: Number of bits to use for quantizing weights.
* <b>`activation_bits`</b>: Number of bits to use for quantizing activations.
* <b>`quant_delay`</b>: Number of steps after which weights and activations are
    quantized during training.
* <b>`freeze_bn_delay`</b>: Number of steps after which moving mean and variance are
    frozen and used instead of batch statistics during training.
    freeze_bn_delay should be greater than quant_delay and should correspond
    to when training has almost converged
* <b>`scope`</b>: The scope to be transformed. If it's not None, only the ops which
    are in this scope will be transformed.


#### Raises:

* <b>`ValueError`</b>: If elements contains an element that isn't a tf.Tensor or
      tf.Operation.