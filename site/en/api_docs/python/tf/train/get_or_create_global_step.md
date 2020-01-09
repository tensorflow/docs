page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.get_or_create_global_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/training_util.py#L147-L162">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns and create (if necessary) the global step tensor.

### Aliases:

* <a href="/api_docs/python/tf/train/get_or_create_global_step"><code>tf.compat.v1.train.get_or_create_global_step</code></a>


``` python
tf.train.get_or_create_global_step(graph=None)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`graph`</b>: The graph in which to create the global step tensor. If missing, use
  default graph.


#### Returns:

The global step tensor.
