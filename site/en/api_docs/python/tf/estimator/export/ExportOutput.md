

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.ExportOutput

## Class `ExportOutput`





Defined in [`tensorflow/python/estimator/export/export_output.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/estimator/export/export_output.py).

Represents an output of a model that can be served.

These typically correspond to model heads.

## Methods

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

``` python
as_signature_def(receiver_tensors)
```

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

#### Args:

* <b>`receiver_tensors`</b>: a `Tensor`, or a dict of string to `Tensor`, specifying
    input nodes that will be fed.



