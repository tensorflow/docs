page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.local_variables

Returns an Op that initializes all local variables.

### Aliases:

* `tf.compat.v1.initializers.local_variables`
* `tf.compat.v1.local_variables_initializer`
* `tf.initializers.local_variables`
* `tf.local_variables_initializer`

``` python
tf.initializers.local_variables()
```



Defined in [`python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

This is just a shortcut for `variables_initializer(local_variables())`

#### Returns:

An Op that initializes all local variables in the graph.
