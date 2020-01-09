page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.enable_v2_behavior


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/compat/v2_compat.py#L30-L51">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Enables TensorFlow 2.x behaviors.

### Aliases:

* <a href="/api_docs/python/tf/enable_v2_behavior"><code>tf.compat.v1.enable_v2_behavior</code></a>
* <a href="/api_docs/python/tf/enable_v2_behavior"><code>tf.compat.v2.enable_v2_behavior</code></a>


``` python
tf.enable_v2_behavior()
```



<!-- Placeholder for "Used in" -->

This function can be called at the beginning of the program (before `Tensors`,
`Graphs` or other structures have been created, and before devices have been
initialized. It switches all global behaviors that are different between
TensorFlow 1.x and 2.x to behave as intended for 2.x.

This function is called in the main TensorFlow `__init__.py` file, user should
not need to call it, except during complex migrations.
