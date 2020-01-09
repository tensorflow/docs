page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.core


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu.py#L153-L163">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the device name for a core in a replicated TPU computation.

### Aliases:

* <a href="/api_docs/python/tf/tpu/core"><code>tf.compat.v1.tpu.core</code></a>
* <a href="/api_docs/python/tf/tpu/core"><code>tf.contrib.tpu.core</code></a>


``` python
tf.tpu.core(num)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`num`</b>: the virtual core number within each replica to which operators should
be assigned.

#### Returns:

A device name, suitable for passing to <a href="../../tf/device"><code>tf.device()</code></a>.
