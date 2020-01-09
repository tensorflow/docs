page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.experimental.get_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/summary_ops_v2.py#L146-L154">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the default summary step for the current thread.

### Aliases:

* `tf.compat.v2.summary.experimental.get_step`


``` python
tf.summary.experimental.get_step()
```



<!-- Placeholder for "Used in" -->


#### Returns:

The step set by <a href="../../../tf/summary/experimental/set_step"><code>tf.summary.experimental.set_step()</code></a> if one has been set,
otherwise None.
