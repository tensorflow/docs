page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental_run_functions_eagerly


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/def_function.py#L254-L271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Enables / disables eager execution of <a href="../../tf/function"><code>tf.function</code></a>s.

### Aliases:

* `tf.compat.v1.config.experimental_run_functions_eagerly`
* `tf.compat.v2.config.experimental_run_functions_eagerly`


``` python
tf.config.experimental_run_functions_eagerly(run_eagerly)
```



### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)



After calling <a href="../../tf/config/experimental_run_functions_eagerly"><code>tf.config.experimental_run_functions_eagerly(True)</code></a> all
invocations of tf.function will run eagerly instead of running through a graph
function.

This can be useful for debugging or profiling.

Similarly, calling <a href="../../tf/config/experimental_run_functions_eagerly"><code>tf.config.experimental_run_functions_eagerly(False)</code></a> will
revert the behavior of all functions to graph functions.

#### Args:


* <b>`run_eagerly`</b>: Boolean. Whether to run functions eagerly.
