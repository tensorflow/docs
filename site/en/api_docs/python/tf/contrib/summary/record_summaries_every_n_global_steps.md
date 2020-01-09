page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.record_summaries_every_n_global_steps


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L125-L133">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the should_record_summaries Tensor to true if global_step % n == 0.

``` python
tf.contrib.summary.record_summaries_every_n_global_steps(
    n,
    global_step=None
)
```



<!-- Placeholder for "Used in" -->
