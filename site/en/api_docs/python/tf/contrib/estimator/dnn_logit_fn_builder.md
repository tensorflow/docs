page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.dnn_logit_fn_builder


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/dnn.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Function builder for a dnn logit_fn.

### Aliases:

* <a href="/api_docs/python/tf/contrib/estimator/dnn_logit_fn_builder"><code>tf.compat.v1.estimator.experimental.dnn_logit_fn_builder</code></a>
* <a href="/api_docs/python/tf/contrib/estimator/dnn_logit_fn_builder"><code>tf.estimator.experimental.dnn_logit_fn_builder</code></a>


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



<!-- Placeholder for "Used in" -->


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
