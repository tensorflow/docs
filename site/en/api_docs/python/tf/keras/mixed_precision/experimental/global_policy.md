page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.mixed_precision.experimental.global_policy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/mixed_precision/experimental/global_policy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/mixed_precision/experimental/policy.py#L350-L370">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the global Policy.

### Aliases:

* <a href="/api_docs/python/tf/keras/mixed_precision/experimental/global_policy"><code>tf.compat.v1.keras.mixed_precision.experimental.global_policy</code></a>
* <a href="/api_docs/python/tf/keras/mixed_precision/experimental/global_policy"><code>tf.compat.v2.keras.mixed_precision.experimental.global_policy</code></a>


``` python
tf.keras.mixed_precision.experimental.global_policy()
```



<!-- Placeholder for "Used in" -->

The global policy is the default policy used for layers, if no policy is
passed to the layer constructor. If no policy has been set with
<a href="../../../../tf/keras/mixed_precision/experimental/set_policy"><code>keras.mixed_precision.experimental.set_policy</code></a>, this will return a policy
constructed from <a href="../../../../tf/keras/backend/floatx"><code>tf.keras.backend.floatx()</code></a> in TensorFlow 2, or an "infer"
policy in TensorFlow 1.

See <a href="../../../../tf/keras/mixed_precision/experimental/Policy"><code>keras.mixed_precision.experimental.Policy</code></a> for more information.

#### Returns:

The global Policy.
