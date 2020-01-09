page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.local_variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L3251-L3262">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an Op that initializes all local variables.

### Aliases:

* <a href="/api_docs/python/tf/initializers/local_variables"><code>tf.compat.v1.initializers.local_variables</code></a>
* <a href="/api_docs/python/tf/initializers/local_variables"><code>tf.compat.v1.local_variables_initializer</code></a>
* <a href="/api_docs/python/tf/initializers/local_variables"><code>tf.local_variables_initializer</code></a>


``` python
tf.initializers.local_variables()
```



<!-- Placeholder for "Used in" -->

This is just a shortcut for `variables_initializer(local_variables())`

#### Returns:

An Op that initializes all local variables in the graph.
