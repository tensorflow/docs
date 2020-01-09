page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.build_raw_serving_input_receiver_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/estimator/export/build_raw_serving_input_receiver_fn">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/export/export.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Build a serving_input_receiver_fn expecting feature Tensors.

### Aliases:

* <a href="/api_docs/python/tf/estimator/export/build_raw_serving_input_receiver_fn"><code>tf.compat.v1.estimator.export.build_raw_serving_input_receiver_fn</code></a>
* <a href="/api_docs/python/tf/estimator/export/build_raw_serving_input_receiver_fn"><code>tf.compat.v2.estimator.export.build_raw_serving_input_receiver_fn</code></a>


``` python
tf.estimator.export.build_raw_serving_input_receiver_fn(
    features,
    default_batch_size=None
)
```



<!-- Placeholder for "Used in" -->

Creates an serving_input_receiver_fn that expects all features to be fed
directly.

#### Args:


* <b>`features`</b>: a dict of string to `Tensor`.
* <b>`default_batch_size`</b>: the number of query examples expected per batch.
    Leave unset for variable batch size (recommended).


#### Returns:

A serving_input_receiver_fn.
