page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.ExportOutput


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L32-L99">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ExportOutput`

Represents an output of a model that can be served.



### Aliases:

* Class `tf.compat.v1.estimator.export.ExportOutput`
* Class `tf.compat.v2.estimator.export.ExportOutput`


<!-- Placeholder for "Used in" -->

These typically correspond to model heads.

## Methods

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L42-L53">View source</a>

``` python
as_signature_def(receiver_tensors)
```

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

#### Args:


* <b>`receiver_tensors`</b>: a `Tensor`, or a dict of string to `Tensor`, specifying
  input nodes that will be fed.
