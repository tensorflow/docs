page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.global_variables_initializer

### Aliases:

* `tf.contrib.lite.global_variables_initializer`
* `tf.global_variables_initializer`
* `tf.initializers.global_variables`

``` python
tf.global_variables_initializer()
```



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/variables.py).

See the guide: [Variables > Variable helper functions](../../../api_guides/python/state_ops#Variable_helper_functions)

Returns an Op that initializes global variables.

This is just a shortcut for `variables_initializer(global_variables())`

#### Returns:

An Op that initializes global variables in the graph.