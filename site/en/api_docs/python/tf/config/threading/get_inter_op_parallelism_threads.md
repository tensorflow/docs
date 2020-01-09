page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.threading.get_inter_op_parallelism_threads


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/threading/get_inter_op_parallelism_threads">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L53-L63">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get number of threads used for parallelism between independent operations.

### Aliases:

* <a href="/api_docs/python/tf/config/threading/get_inter_op_parallelism_threads"><code>tf.compat.v1.config.threading.get_inter_op_parallelism_threads</code></a>
* <a href="/api_docs/python/tf/config/threading/get_inter_op_parallelism_threads"><code>tf.compat.v2.config.threading.get_inter_op_parallelism_threads</code></a>


``` python
tf.config.threading.get_inter_op_parallelism_threads()
```



<!-- Placeholder for "Used in" -->

Determines the number of threads used by independent non-blocking operations.
0 means the system picks an appropriate number.

#### Returns:

Number of parallel threads
