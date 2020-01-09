page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.RegressionOutput


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L170-L199">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RegressionOutput`

Represents the output of a regression head.

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput)

### Aliases:

* Class `tf.compat.v1.estimator.export.RegressionOutput`
* Class `tf.compat.v2.estimator.export.RegressionOutput`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L173-L185">View source</a>

``` python
__init__(value)
```

Constructor for `RegressionOutput`.


#### Args:


* <b>`value`</b>: a float `Tensor` giving the predicted values.  Required.


#### Raises:


* <b>`ValueError`</b>: if the value is not a `Tensor` with dtype tf.float32.



## Properties

<h3 id="value"><code>value</code></h3>






## Methods

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L191-L199">View source</a>

``` python
as_signature_def(receiver_tensors)
```

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

#### Args:


* <b>`receiver_tensors`</b>: a `Tensor`, or a dict of string to `Tensor`, specifying
  input nodes that will be fed.
