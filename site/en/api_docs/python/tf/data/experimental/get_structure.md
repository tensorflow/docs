page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.get_structure


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/dataset_ops.py#L2109-L2128">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the type specification of an element of a `Dataset` or `Iterator`.

### Aliases:

* `tf.compat.v1.data.experimental.get_structure`
* `tf.compat.v2.data.experimental.get_structure`


``` python
tf.data.experimental.get_structure(dataset_or_iterator)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dataset_or_iterator`</b>: A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> or `tf.data.Iterator`.


#### Returns:

A nested structure of <a href="../../../tf/TypeSpec"><code>tf.TypeSpec</code></a> objects matching the structure of an
element of `dataset_or_iterator` and spacifying the type of individal
components.



#### Raises:


* <b>`TypeError`</b>: If `dataset_or_iterator` is not a `Dataset` or `Iterator` object.
