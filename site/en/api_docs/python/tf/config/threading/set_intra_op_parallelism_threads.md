page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.threading.set_intra_op_parallelism_threads


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/threading/set_intra_op_parallelism_threads">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L39-L50">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Set number of threads used within an individual op for parallelism.

### Aliases:

* <a href="/api_docs/python/tf/config/threading/set_intra_op_parallelism_threads"><code>tf.compat.v1.config.threading.set_intra_op_parallelism_threads</code></a>
* <a href="/api_docs/python/tf/config/threading/set_intra_op_parallelism_threads"><code>tf.compat.v2.config.threading.set_intra_op_parallelism_threads</code></a>


``` python
tf.config.threading.set_intra_op_parallelism_threads(num_threads)
```



<!-- Placeholder for "Used in" -->

Certain operations like matrix multiplication and reductions can utilize
parallel threads for speed ups. A value of 0 means the system picks an
appropriate number.

#### Args:


* <b>`num_threads`</b>: Number of parallel threads
