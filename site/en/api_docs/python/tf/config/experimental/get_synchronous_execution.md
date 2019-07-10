page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_synchronous_execution

Gets whether operations are executed synchronously or asynchronously.

### Aliases:

* `tf.compat.v1.config.experimental.get_synchronous_execution`
* `tf.compat.v2.config.experimental.get_synchronous_execution`
* `tf.config.experimental.get_synchronous_execution`

``` python
tf.config.experimental.get_synchronous_execution()
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

TensorFlow can execute operations synchronously or asynchronously. If
asynchronous execution is enabled, operations may return "non-ready" handles.

#### Returns:

Current thread execution mode
