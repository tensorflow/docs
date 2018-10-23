

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.tables_initializer

### `tf.tables_initializer`

``` python
tables_initializer(name='init_all_tables')
```



Defined in [`tensorflow/python/ops/data_flow_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/data_flow_ops.py).

See the guide: [Variables > Sparse Variable Updates](../../../api_guides/python/state_ops#Sparse_Variable_Updates)

Returns an Op that initializes all tables of the default graph.

#### Args:

* <b>`name`</b>: Optional name for the initialization op.


#### Returns:

  An Op that initializes all tables.  Note that if there are
  not tables the returned Op is a NoOp.