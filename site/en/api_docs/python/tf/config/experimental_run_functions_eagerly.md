page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental_run_functions_eagerly


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental_run_functions_eagerly">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/def_function.py#L218-L235">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Enables / disables eager execution of <a href="../../tf/function"><code>tf.function</code></a>s.

### Aliases:

* <a href="/api_docs/python/tf/config/experimental_run_functions_eagerly"><code>tf.compat.v1.config.experimental_run_functions_eagerly</code></a>
* <a href="/api_docs/python/tf/config/experimental_run_functions_eagerly"><code>tf.compat.v2.config.experimental_run_functions_eagerly</code></a>


``` python
tf.config.experimental_run_functions_eagerly(run_eagerly)
```



<!-- Placeholder for "Used in" -->

After calling <a href="../../tf/config/experimental_run_functions_eagerly"><code>tf.config.experimental_run_functions_eagerly(True)</code></a> all
invocations of tf.function will run eagerly instead of running through a graph
function.

This can be useful for debugging or profiling.

Similarly, calling <a href="../../tf/config/experimental_run_functions_eagerly"><code>tf.config.experimental_run_functions_eagerly(False)</code></a> will
revert the behavior of all functions to graph functions.

#### Args:


* <b>`run_eagerly`</b>: Boolean. Whether to run functions eagerly.
