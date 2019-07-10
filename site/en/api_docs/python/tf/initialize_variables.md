page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initialize_variables

See <a href="../tf/initializers/variables"><code>tf.compat.v1.variables_initializer</code></a>. (deprecated)

### Aliases:

* `tf.compat.v1.initialize_variables`
* `tf.initialize_variables`

``` python
tf.initialize_variables(
    var_list,
    name='init'
)
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2017-03-02.
Instructions for updating:
Use <a href="../tf/initializers/variables"><code>tf.variables_initializer</code></a> instead.

  **NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.