page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.enable_tensor_equality


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L267-L276">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compare Tensors with element-wise comparison and thus be unhashable.

### Aliases:

* <a href="/api_docs/python/tf/enable_tensor_equality"><code>tf.compat.v1.enable_tensor_equality</code></a>


``` python
tf.enable_tensor_equality()
```



<!-- Placeholder for "Used in" -->

Comparing tensors with element-wise allows comparisons such as
tf.Variable(1.0) == 1.0. Element-wise equality implies that tensors are
unhashable. Thus tensors can no longer be directly used in sets or as a key in
a dictionary.
