page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.build_parsing_serving_input_receiver_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/estimator/export/build_parsing_serving_input_receiver_fn">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/export/export.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Build a serving_input_receiver_fn expecting fed tf.Examples.

### Aliases:

* <a href="/api_docs/python/tf/estimator/export/build_parsing_serving_input_receiver_fn"><code>tf.compat.v1.estimator.export.build_parsing_serving_input_receiver_fn</code></a>
* <a href="/api_docs/python/tf/estimator/export/build_parsing_serving_input_receiver_fn"><code>tf.compat.v2.estimator.export.build_parsing_serving_input_receiver_fn</code></a>


``` python
tf.estimator.export.build_parsing_serving_input_receiver_fn(
    feature_spec,
    default_batch_size=None
)
```



<!-- Placeholder for "Used in" -->

Creates a serving_input_receiver_fn that expects a serialized tf.Example fed
into a string placeholder.  The function parses the tf.Example according to
the provided feature_spec, and returns all parsed Tensors as features.

#### Args:


* <b>`feature_spec`</b>: a dict of string to `VarLenFeature`/`FixedLenFeature`.
* <b>`default_batch_size`</b>: the number of query examples expected per batch.
    Leave unset for variable batch size (recommended).


#### Returns:

A serving_input_receiver_fn suitable for use in serving.
