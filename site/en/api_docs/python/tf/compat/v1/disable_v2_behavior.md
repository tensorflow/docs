page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.disable_v2_behavior


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/compat/v2_compat.py#L51-L68">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Disables TensorFlow 2.x behaviors.

``` python
tf.compat.v1.disable_v2_behavior()
```



<!-- Placeholder for "Used in" -->

This function can be called at the beginning of the program (before `Tensors`,
`Graphs` or other structures have been created, and before devices have been
initialized. It switches all global behaviors that are different between
TensorFlow 1.x and 2.x to behave as intended for 1.x.

User can call this function to disable 2.x behavior during complex migrations.
