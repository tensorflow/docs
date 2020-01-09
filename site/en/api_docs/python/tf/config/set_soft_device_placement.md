page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.set_soft_device_placement


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/set_soft_device_placement">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L174-L186">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Set if soft device placement is enabled.

### Aliases:

* <a href="/api_docs/python/tf/config/set_soft_device_placement"><code>tf.compat.v1.config.set_soft_device_placement</code></a>
* <a href="/api_docs/python/tf/config/set_soft_device_placement"><code>tf.compat.v2.config.set_soft_device_placement</code></a>


``` python
tf.config.set_soft_device_placement(enabled)
```



<!-- Placeholder for "Used in" -->

If enabled, an op will be placed on CPU if any of the following are true
  1. there's no GPU implementation for the OP
  2. no GPU devices are known or registered
  3. need to co-locate with reftype input(s) which are from CPU

#### Args:


* <b>`enabled`</b>: Whether to enable soft placement.
