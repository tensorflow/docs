page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.data.get_output_types


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/dataset_ops.py#L2171-L2188">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the output shapes of a `Dataset` or `Iterator` elements.

``` python
tf.compat.v1.data.get_output_types(dataset_or_iterator)
```



<!-- Placeholder for "Used in" -->

This utility method replaces the deprecated-in-V2
`tf.compat.v1.Dataset.output_types` property.

#### Args:


* <b>`dataset_or_iterator`</b>: A <a href="../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> or `tf.data.Iterator`.


#### Returns:

A nested structure of <a href="../../../../tf/dtypes/DType"><code>tf.DType</code></a> objects objects matching the structure of
dataset / iterator elements and specifying the shape of the individual
components.
