page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.threading.get_intra_op_parallelism_threads

Get number of threads used within an individual op for parallelism.

### Aliases:

* `tf.compat.v1.config.threading.get_intra_op_parallelism_threads`
* `tf.compat.v2.config.threading.get_intra_op_parallelism_threads`
* `tf.config.threading.get_intra_op_parallelism_threads`

``` python
tf.config.threading.get_intra_op_parallelism_threads()
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

Certain operations like matrix multiplication and reductions can utilize
parallel threads for speed ups. A value of 0 means the system picks an
appropriate number.

#### Returns:

Number of parallel threads
