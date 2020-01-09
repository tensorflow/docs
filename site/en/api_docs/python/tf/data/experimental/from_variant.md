page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.from_variant


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/from_variant">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/dataset_ops.py#L2450-L2462">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Constructs a dataset from the given variant and structure.

### Aliases:

* <a href="/api_docs/python/tf/data/experimental/from_variant"><code>tf.compat.v1.data.experimental.from_variant</code></a>
* <a href="/api_docs/python/tf/data/experimental/from_variant"><code>tf.compat.v2.data.experimental.from_variant</code></a>


``` python
tf.data.experimental.from_variant(
    variant,
    structure
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`variant`</b>: A scalar <a href="../../../tf#variant"><code>tf.variant</code></a> tensor representing a dataset.
* <b>`structure`</b>: A <a href="../../../tf/TypeSpec"><code>tf.data.experimental.Structure</code></a> object representing the
  structure of each element in the dataset.


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> instance.
