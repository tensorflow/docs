page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_variable_full_name


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L597-L614">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the full name of a variable.

``` python
tf.contrib.framework.get_variable_full_name(var)
```



<!-- Placeholder for "Used in" -->

For normal Variables, this is the same as the var.op.name.  For
sliced or PartitionedVariables, this name is the same for all the
slices/partitions. In both cases, this is normally the name used in
a checkpoint file.

#### Args:


* <b>`var`</b>: A `Variable` object.


#### Returns:

A string that is the full name.
