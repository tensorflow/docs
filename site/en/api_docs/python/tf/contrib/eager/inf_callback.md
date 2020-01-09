page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.inf_callback


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/execution_callbacks.py#L207-L222">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A specialization of `inf_nan_callback` that checks for `inf`s only.

``` python
tf.contrib.eager.inf_callback(
    op_type,
    inputs,
    attrs,
    outputs,
    op_name,
    action=tf.contrib.eager.ExecutionCallback.RAISE
)
```



<!-- Placeholder for "Used in" -->
