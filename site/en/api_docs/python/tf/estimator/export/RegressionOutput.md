page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.RegressionOutput

## Class `RegressionOutput`

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput)

Represents the output of a regression head.

<h2 id="__init__"><code>__init__</code></h2>

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

``` python
as_signature_def(receiver_tensors)
```

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

#### Args:

* <b>`receiver_tensors`</b>: a `Tensor`, or a dict of string to `Tensor`, specifying
    input nodes that will be fed.



