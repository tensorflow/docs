page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.global_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L3229-L3240">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an Op that initializes global variables.

### Aliases:

* <a href="/api_docs/python/tf/initializers/global_variables"><code>tf.compat.v1.global_variables_initializer</code></a>
* <a href="/api_docs/python/tf/initializers/global_variables"><code>tf.compat.v1.initializers.global_variables</code></a>
* <a href="/api_docs/python/tf/initializers/global_variables"><code>tf.global_variables_initializer</code></a>


``` python
tf.initializers.global_variables()
```



<!-- Placeholder for "Used in" -->

This is just a shortcut for `variables_initializer(global_variables())`

#### Returns:

An Op that initializes global variables in the graph.
