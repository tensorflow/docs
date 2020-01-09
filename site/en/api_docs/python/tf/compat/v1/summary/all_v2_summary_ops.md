page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.all_v2_summary_ops


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/summary_ops_v2.py#L513-L526">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns all V2-style summary ops defined in the current default graph.

``` python
tf.compat.v1.summary.all_v2_summary_ops()
```



<!-- Placeholder for "Used in" -->

This includes ops from TF 2.0 tf.summary and TF 1.x tf.contrib.summary (except
for `tf.contrib.summary.graph` and `tf.contrib.summary.import_event`), but
does *not* include TF 1.x tf.summary ops.

#### Returns:

List of summary ops, or None if called under eager execution.
