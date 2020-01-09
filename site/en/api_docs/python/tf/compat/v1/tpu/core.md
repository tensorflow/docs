page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.tpu.core


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/tpu/tpu.py#L151-L161">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the device name for a core in a replicated TPU computation.

``` python
tf.compat.v1.tpu.core(num)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`num`</b>: the virtual core number within each replica to which operators should
be assigned.

#### Returns:

A device name, suitable for passing to <a href="../../../../tf/device"><code>tf.device()</code></a>.
