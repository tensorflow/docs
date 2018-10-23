

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.estimator.export.RegressionOutput

### `class tf.estimator.export.RegressionOutput`



Defined in [`tensorflow/python/estimator/export/export_output.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/estimator/export/export_output.py).

Represents the output of a regression head.

## Properties

<h3 id="value"><code>value</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(value)
```

Constructor for `RegressionOutput`.

#### Args:

* <b>`value`</b>: a float `Tensor` giving the predicted values.  Required.


#### Raises:

* <b>`ValueError`</b>: if the value is not a `Tensor` with dtype tf.float32.

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

``` python
as_signature_def(receiver_tensors)
```





