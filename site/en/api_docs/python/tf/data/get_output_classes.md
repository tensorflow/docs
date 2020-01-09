page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.get_output_classes


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/dataset_ops.py#L2140-L2157">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the output classes of a `Dataset` or `Iterator` elements.

### Aliases:

* <a href="/api_docs/python/tf/data/get_output_classes"><code>tf.compat.v1.data.get_output_classes</code></a>


``` python
tf.data.get_output_classes(dataset_or_iterator)
```



<!-- Placeholder for "Used in" -->

This utility method replaces the deprecated-in-V2
`tf.compat.v1.Dataset.output_classes` property.

#### Args:


* <b>`dataset_or_iterator`</b>: A <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a> or `tf.data.IteratorV2`.


#### Returns:

A nested structure of Python `type` objects matching the structure of the
dataset / iterator elements and specifying the class of the individual
components.
