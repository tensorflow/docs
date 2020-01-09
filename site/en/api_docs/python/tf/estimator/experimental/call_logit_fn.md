page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.experimental.call_logit_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/estimator/experimental/call_logit_fn">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/model_fn.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Calls logit_fn (experimental).

### Aliases:

* <a href="/api_docs/python/tf/estimator/experimental/call_logit_fn"><code>tf.compat.v1.estimator.experimental.call_logit_fn</code></a>
* <a href="/api_docs/python/tf/estimator/experimental/call_logit_fn"><code>tf.compat.v2.estimator.experimental.call_logit_fn</code></a>


``` python
tf.estimator.experimental.call_logit_fn(
    logit_fn,
    features,
    mode,
    params,
    config
)
```



<!-- Placeholder for "Used in" -->

THIS FUNCTION IS EXPERIMENTAL. Keras layers/models are the recommended APIs
for logit and model composition.

A utility function that calls the provided logit_fn with the relevant subset
of provided arguments. Similar to tf.estimator._call_model_fn().

#### Args:


* <b>`logit_fn`</b>: A logit_fn as defined above.
* <b>`features`</b>: The features dict.
* <b>`mode`</b>: TRAIN / EVAL / PREDICT ModeKeys.
* <b>`params`</b>: The hyperparameter dict.
* <b>`config`</b>: The configuration object.


#### Returns:

A logit Tensor, the output of logit_fn.



#### Raises:


* <b>`ValueError`</b>: if logit_fn does not return a Tensor or a dictionary mapping
  strings to Tensors.
