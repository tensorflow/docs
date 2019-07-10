page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.global_variables

Returns an Op that initializes global variables.

### Aliases:

* `tf.compat.v1.global_variables_initializer`
* `tf.compat.v1.initializers.global_variables`
* `tf.global_variables_initializer`
* `tf.initializers.global_variables`

``` python
tf.initializers.global_variables()
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

This is just a shortcut for `variables_initializer(global_variables())`

#### Returns:

An Op that initializes global variables in the graph.
