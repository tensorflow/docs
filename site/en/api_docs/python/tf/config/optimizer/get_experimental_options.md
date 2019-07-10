page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.optimizer.get_experimental_options

Get experimental optimizer options.

### Aliases:

* `tf.compat.v1.config.optimizer.get_experimental_options`
* `tf.compat.v2.config.optimizer.get_experimental_options`
* `tf.config.optimizer.get_experimental_options`

``` python
tf.config.optimizer.get_experimental_options()
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

Refer to tf.config.optimizer.set_experimental_options for a list of current
options.

Note that optimizations are only applied in graph mode, (within tf.function).
In addition, as these are experimental options, the list is subject to change.

#### Returns:

Dictionary of configured experimental optimizer options
