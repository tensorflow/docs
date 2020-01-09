page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.tables_initializer

### Aliases:

* `tf.initializers.tables_initializer`
* `tf.tables_initializer`

``` python
tf.initializers.tables_initializer(name='init_all_tables')
```



Defined in [`tensorflow/python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/lookup_ops.py).

Returns an Op that initializes all tables of the default graph.

#### Args:

* <b>`name`</b>: Optional name for the initialization op.


#### Returns:

An Op that initializes all tables.  Note that if there are
not tables the returned Op is a NoOp.