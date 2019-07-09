page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.dnn_logit_fn_builder

``` python
tf.contrib.estimator.dnn_logit_fn_builder(
    units,
    hidden_units,
    feature_columns,
    activation_fn,
    dropout,
    input_layer_partitioner,
    batch_norm
)
```



Defined in [`tensorflow/python/estimator/canned/dnn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/estimator/canned/dnn.py).

Function builder for a dnn logit_fn.

#### Args:

* <b>`units`</b>: An int indicating the dimension of the logit layer.  In the
    MultiHead case, this should be the sum of all component Heads' logit
    dimensions.
* <b>`hidden_units`</b>: Iterable of integer number of hidden units per layer.
* <b>`feature_columns`</b>: Iterable of `feature_column._FeatureColumn` model inputs.
* <b>`activation_fn`</b>: Activation function applied to each layer.
* <b>`dropout`</b>: When not `None`, the probability we will drop out a given
    coordinate.
* <b>`input_layer_partitioner`</b>: Partitioner for input layer.
* <b>`batch_norm`</b>: Whether to use batch normalization after each hidden layer.


#### Returns:

A logit_fn (see below).


#### Raises:

* <b>`ValueError`</b>: If units is not an int.