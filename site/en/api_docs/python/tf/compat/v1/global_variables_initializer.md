page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.global_variables_initializer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/variables.py#L3229-L3240">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an Op that initializes global variables.

### Aliases:

* `tf.compat.v1.initializers.global_variables`


``` python
tf.compat.v1.global_variables_initializer()
```



<!-- Placeholder for "Used in" -->

This is just a shortcut for `variables_initializer(global_variables())`

#### Returns:

An Op that initializes global variables in the graph.
