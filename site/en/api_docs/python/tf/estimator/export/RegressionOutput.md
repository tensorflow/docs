page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.RegressionOutput

## Class `RegressionOutput`

Represents the output of a regression head.

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput)

### Aliases:

* Class `tf.compat.v1.estimator.export.RegressionOutput`
* Class `tf.compat.v2.estimator.export.RegressionOutput`
* Class `tf.estimator.export.RegressionOutput`



Defined in [`python/saved_model/model_utils/export_output.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/saved_model/model_utils/export_output.py).

<!-- Placeholder for "Used in" -->


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






