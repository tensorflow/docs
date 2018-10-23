

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.strip_name_scope

``` python
strip_name_scope(
    name,
    export_scope
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/framework/ops.py).

Removes name scope from a name.

#### Args:

* <b>`name`</b>: A `string` name.
* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

  Name with name scope removed, or the original name if export_scope
  is None.