page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.ExportOutput

## Class `ExportOutput`

Represents an output of a model that can be served.



### Aliases:

* Class `tf.compat.v1.estimator.export.ExportOutput`
* Class `tf.compat.v2.estimator.export.ExportOutput`
* Class `tf.estimator.export.ExportOutput`



Defined in [`python/saved_model/model_utils/export_output.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/saved_model/model_utils/export_output.py).

<!-- Placeholder for "Used in" -->

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



