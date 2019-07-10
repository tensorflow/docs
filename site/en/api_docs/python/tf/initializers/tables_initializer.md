page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.tables_initializer

Returns an Op that initializes all tables of the default graph.

### Aliases:

* `tf.compat.v1.initializers.tables_initializer`
* `tf.compat.v1.tables_initializer`
* `tf.initializers.tables_initializer`
* `tf.tables_initializer`

``` python
tf.initializers.tables_initializer(name='init_all_tables')
```



Defined in [`python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/lookup_ops.py).

<!-- Placeholder for "Used in" -->

See the [Low Level
Intro](https://www.tensorflow.org/guide/low_level_intro#feature_columns)
guide, for an example of usage.

#### Args:


* <b>`name`</b>: Optional name for the initialization op.


#### Returns:

An Op that initializes all tables.  Note that if there are
not tables the returned Op is a NoOp.
