

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.initialize_all_tables

### `tf.initialize_all_tables`

``` python
initialize_all_tables(
    *args,
    **kwargs
)
```



Defined in [`tensorflow/python/util/deprecation.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/util/deprecation.py).

See the guide: [Variables > Sparse Variable Updates](../../../api_guides/python/state_ops#Sparse_Variable_Updates)

Returns an Op that initializes all tables of the default graph. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2017-03-02.
Instructions for updating:
Use `tf.tables_initializer` instead.

#### Args:

* <b>`name`</b>: Optional name for the initialization op.


#### Returns:

  An Op that initializes all tables.  Note that if there are
  not tables the returned Op is a NoOp.