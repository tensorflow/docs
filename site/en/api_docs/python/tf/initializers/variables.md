page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.variables


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L3195-L3218">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an Op that initializes a list of variables.

### Aliases:

* <a href="/api_docs/python/tf/initializers/variables"><code>tf.compat.v1.initializers.variables</code></a>
* <a href="/api_docs/python/tf/initializers/variables"><code>tf.compat.v1.variables_initializer</code></a>
* <a href="/api_docs/python/tf/initializers/variables"><code>tf.variables_initializer</code></a>


``` python
tf.initializers.variables(
    var_list,
    name='init'
)
```



<!-- Placeholder for "Used in" -->

After you launch the graph in a session, you can run the returned Op to
initialize all the variables in `var_list`. This Op runs all the
initializers of the variables in `var_list` in parallel.

Calling `initialize_variables()` is equivalent to passing the list of
initializers to `Group()`.

If `var_list` is empty, however, the function still returns an Op that can
be run. That Op just has no effect.

#### Args:


* <b>`var_list`</b>: List of `Variable` objects to initialize.
* <b>`name`</b>: Optional name for the returned operation.


#### Returns:

An Op that run the initializers of all the specified variables.
