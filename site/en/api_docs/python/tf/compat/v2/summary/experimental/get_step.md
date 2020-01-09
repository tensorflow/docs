page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.experimental.get_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L146-L154">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the default summary step for the current thread.

``` python
tf.compat.v2.summary.experimental.get_step()
```



<!-- Placeholder for "Used in" -->


#### Returns:

The step set by `tf.summary.experimental.set_step()` if one has been set,
otherwise None.
