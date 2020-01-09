page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.enable_control_flow_v2


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/control_flow_v2_toggles.py#L28-L45">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Use control flow v2.

### Aliases:

* <a href="/api_docs/python/tf/enable_control_flow_v2"><code>tf.compat.v1.enable_control_flow_v2</code></a>


``` python
tf.enable_control_flow_v2()
```



<!-- Placeholder for "Used in" -->

control flow v2 (cfv2) is an improved version of control flow in TensorFlow
with support for higher order derivatives. Enabling cfv2 will change the
graph/function representation of control flow, e.g., <a href="../tf/while_loop"><code>tf.while_loop</code></a> and
<a href="../tf/cond"><code>tf.cond</code></a> will generate functional `While` and `If` ops instead of low-level
`Switch`, `Merge` etc. ops. Note: Importing and running graphs exported
with old control flow will still be supported.

Calling tf.enable_control_flow_v2() lets you opt-in to this TensorFlow 2.0
feature.

Note: v2 control flow is always enabled inside of tf.function. Calling this
function is not required.
