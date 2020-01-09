page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.mixed_precision.experimental.set_policy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/mixed_precision/experimental/policy.py#L416-L441">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the global Policy.

### Aliases:

* `tf.compat.v1.keras.mixed_precision.experimental.set_policy`
* `tf.compat.v2.keras.mixed_precision.experimental.set_policy`


``` python
tf.keras.mixed_precision.experimental.set_policy(policy)
```



<!-- Placeholder for "Used in" -->

The global policy is the default policy used for layers, if no policy is
passed to the layer constructor. If no global policy is set, layers will
instead default to a Policy constructed from <a href="../../../../tf/keras/backend/floatx"><code>tf.keras.backend.floatx()</code></a> in
TensorFlow 2. In TensorFlow 1, layers default to an "infer" policy.

See <a href="../../../../tf/keras/mixed_precision/experimental/Policy"><code>keras.mixed_precision.experimental.Policy</code></a> for more information.

#### Args:


* <b>`policy`</b>: A Policy, or a string that will be converted to a Policy..
