page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.get_structure


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/get_structure">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/dataset_ops.py#L2118-L2137">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the type specification of an element of a `Dataset` or `Iterator`.

### Aliases:

* <a href="/api_docs/python/tf/data/experimental/get_structure"><code>tf.compat.v1.data.experimental.get_structure</code></a>
* <a href="/api_docs/python/tf/data/experimental/get_structure"><code>tf.compat.v2.data.experimental.get_structure</code></a>


``` python
tf.data.experimental.get_structure(dataset_or_iterator)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dataset_or_iterator`</b>: A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> or <a href="../../../tf/data/Iterator"><code>tf.data.Iterator</code></a>.


#### Returns:

A nested structure of <a href="../../../tf/TypeSpec"><code>tf.TypeSpec</code></a> objects matching the structure of an
element of `dataset_or_iterator` and spacifying the type of individal
components.



#### Raises:


* <b>`TypeError`</b>: If `dataset_or_iterator` is not a `Dataset` or `Iterator` object.
