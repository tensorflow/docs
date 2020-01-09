page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.experimental.set_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L157-L173">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the default summary step for the current thread.

``` python
tf.compat.v2.summary.experimental.set_step(step)
```



<!-- Placeholder for "Used in" -->

For convenience, this function sets a default value for the `step` parameter
used in summary-writing functions elsewhere in the API so that it need not
be explicitly passed in every such invocation. The value can be a constant
or a variable, and can be retrieved via `tf.summary.experimental.get_step()`.

Note: when using this with @tf.functions, the step value will be captured at
the time the function is traced, so changes to the step outside the function
will not be reflected inside the function unless using a <a href="../../../../../tf/Variable"><code>tf.Variable</code></a> step.

#### Args:


* <b>`step`</b>: An `int64`-castable default step value, or None to unset.
