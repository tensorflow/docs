page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.local_variables

### Aliases:

* `tf.initializers.local_variables`
* `tf.local_variables_initializer`

``` python
tf.initializers.local_variables()
```



Defined in [`tensorflow/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/variables.py).

Returns an Op that initializes all local variables.

This is just a shortcut for `variables_initializer(local_variables())`

#### Returns:

An Op that initializes all local variables in the graph.