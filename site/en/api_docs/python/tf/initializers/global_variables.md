page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.global_variables

### Aliases:

* `tf.global_variables_initializer`
* `tf.initializers.global_variables`

``` python
tf.initializers.global_variables()
```



Defined in [`tensorflow/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/variables.py).

Returns an Op that initializes global variables.

This is just a shortcut for `variables_initializer(global_variables())`

#### Returns:

An Op that initializes global variables in the graph.