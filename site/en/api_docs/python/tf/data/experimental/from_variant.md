page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.from_variant


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/dataset_ops.py#L2432-L2444">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Constructs a dataset from the given variant and structure.

### Aliases:

* `tf.compat.v1.data.experimental.from_variant`
* `tf.compat.v2.data.experimental.from_variant`


``` python
tf.data.experimental.from_variant(
    variant,
    structure
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`variant`</b>: A scalar <a href="../../../tf#variant"><code>tf.variant</code></a> tensor representing a dataset.
* <b>`structure`</b>: A `tf.data.experimental.Structure` object representing the
  structure of each element in the dataset.


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> instance.
