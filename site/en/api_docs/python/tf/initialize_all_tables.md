page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initialize_all_tables

``` python
tf.initialize_all_tables(name='init_all_tables')
```



Defined in [`tensorflow/python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/lookup_ops.py).

Returns an Op that initializes all tables of the default graph. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../tf/initializers/tables_initializer"><code>tf.tables_initializer</code></a> instead.

#### Args:

* <b>`name`</b>: Optional name for the initialization op.


#### Returns:

An Op that initializes all tables.  Note that if there are
not tables the returned Op is a NoOp.