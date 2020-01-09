page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.disable_control_flow_v2


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/control_flow_v2_toggles.py#L48-L58">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Opts out of control flow v2.

``` python
tf.compat.v1.disable_control_flow_v2()
```



<!-- Placeholder for "Used in" -->

Note: v2 control flow is always enabled inside of tf.function. Calling this
function has no effect in that case.

If your code needs tf.disable_control_flow_v2() to be called to work
properly please file a bug.
