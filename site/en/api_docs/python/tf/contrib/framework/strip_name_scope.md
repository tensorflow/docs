page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.strip_name_scope

Removes name scope from a name.

``` python
tf.contrib.framework.strip_name_scope(
    name,
    export_scope
)
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: A `string` name.
* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

Name with name scope removed, or the original name if export_scope
is None.
