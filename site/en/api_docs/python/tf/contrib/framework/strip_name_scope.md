page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.strip_name_scope

``` python
tf.contrib.framework.strip_name_scope(
    name,
    export_scope
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/framework/ops.py).

Removes name scope from a name.

#### Args:

* <b>`name`</b>: A `string` name.
* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

Name with name scope removed, or the original name if export_scope
is None.