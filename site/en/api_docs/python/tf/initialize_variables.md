page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initialize_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L3221-L3226">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



See <a href="../tf/initializers/variables"><code>tf.compat.v1.variables_initializer</code></a>. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/initialize_variables"><code>tf.compat.v1.initialize_variables</code></a>


``` python
tf.initialize_variables(
    var_list,
    name='init'
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2017-03-02.
Instructions for updating:
Use <a href="../tf/initializers/variables"><code>tf.variables_initializer</code></a> instead.

  **NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.
