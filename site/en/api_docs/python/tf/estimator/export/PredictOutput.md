page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.PredictOutput

## Class `PredictOutput`

Represents the output of a generic prediction head.

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput)

### Aliases:

* Class `tf.compat.v1.estimator.export.PredictOutput`
* Class `tf.compat.v2.estimator.export.PredictOutput`
* Class `tf.estimator.export.PredictOutput`



Defined in [`python/saved_model/model_utils/export_output.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/saved_model/model_utils/export_output.py).

<!-- Placeholder for "Used in" -->

A generic prediction need not be either a classification or a regression.

Named outputs must be provided as a dict from string to `Tensor`,

<h2 id="__init__"><code>__init__</code></h2>

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

``` python
as_signature_def(receiver_tensors)
```






