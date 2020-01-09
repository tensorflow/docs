page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.disable_eager_execution


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L5722-L5734">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Disables eager execution.

### Aliases:

* <a href="/api_docs/python/tf/disable_eager_execution"><code>tf.compat.v1.disable_eager_execution</code></a>


``` python
tf.disable_eager_execution()
```



<!-- Placeholder for "Used in" -->

This function can only be called before any Graphs, Ops, or Tensors have been
created. It can be used at the beginning of the program for complex migration
projects from TensorFlow 1.x to 2.x.
