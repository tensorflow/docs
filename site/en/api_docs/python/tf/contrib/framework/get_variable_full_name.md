page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_variable_full_name

Returns the full name of a variable.

``` python
tf.contrib.framework.get_variable_full_name(var)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

For normal Variables, this is the same as the var.op.name.  For
sliced or PartitionedVariables, this name is the same for all the
slices/partitions. In both cases, this is normally the name used in
a checkpoint file.

#### Args:


* <b>`var`</b>: A `Variable` object.


#### Returns:

A string that is the full name.
