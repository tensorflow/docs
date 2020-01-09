page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.PredictOutput


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/estimator/export/PredictOutput">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/model_utils/export_output.py#L202-L232">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `PredictOutput`

Represents the output of a generic prediction head.

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput)

### Aliases:

* Class <a href="/api_docs/python/tf/estimator/export/PredictOutput"><code>tf.compat.v1.estimator.export.PredictOutput</code></a>
* Class <a href="/api_docs/python/tf/estimator/export/PredictOutput"><code>tf.compat.v2.estimator.export.PredictOutput</code></a>


<!-- Placeholder for "Used in" -->

A generic prediction need not be either a classification or a regression.

Named outputs must be provided as a dict from string to `Tensor`,

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/model_utils/export_output.py#L211-L224">View source</a>

``` python
__init__(outputs)
```

Constructor for PredictOutput.


#### Args:


* <b>`outputs`</b>: A `Tensor` or a dict of string to `Tensor` representing the
  predictions.


#### Raises:


* <b>`ValueError`</b>: if the outputs is not dict, or any of its keys are not
    strings, or any of its values are not `Tensor`s.



## Properties

<h3 id="outputs"><code>outputs</code></h3>






## Methods

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/model_utils/export_output.py#L230-L232">View source</a>

``` python
as_signature_def(receiver_tensors)
```

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

#### Args:


* <b>`receiver_tensors`</b>: a `Tensor`, or a dict of string to `Tensor`, specifying
  input nodes that will be fed.
