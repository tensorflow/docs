page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.shutdown_system


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu.py#L138-L150">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Shuts down a running a distributed TPU system.

### Aliases:

* <a href="/api_docs/python/tf/tpu/shutdown_system"><code>tf.compat.v1.tpu.shutdown_system</code></a>
* <a href="/api_docs/python/tf/tpu/shutdown_system"><code>tf.contrib.tpu.shutdown_system</code></a>


``` python
tf.tpu.shutdown_system(job=None)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`job`</b>: The job (the XXX in TensorFlow device specification /job:XXX) that
  contains the TPU devices that will be shutdown. If job=None it is
  assumed there is only one job in the TensorFlow flock, and an error will
  be returned if this assumption does not hold.
