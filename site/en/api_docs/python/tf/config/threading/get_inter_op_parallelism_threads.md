page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.threading.get_inter_op_parallelism_threads

Get number of threads used for parallelism between independent operations.

### Aliases:

* `tf.compat.v1.config.threading.get_inter_op_parallelism_threads`
* `tf.compat.v2.config.threading.get_inter_op_parallelism_threads`
* `tf.config.threading.get_inter_op_parallelism_threads`

``` python
tf.config.threading.get_inter_op_parallelism_threads()
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

Determines the number of threads used by independent non-blocking operations.
0 means the system picks an appropriate number.

#### Returns:

Number of parallel threads
