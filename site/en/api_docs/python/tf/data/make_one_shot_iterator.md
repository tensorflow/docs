page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.make_one_shot_iterator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/dataset_ops.py#L2063-L2081">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a <a href="../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> for enumerating the elements of a dataset.

### Aliases:

* <a href="/api_docs/python/tf/data/make_one_shot_iterator"><code>tf.compat.v1.data.make_one_shot_iterator</code></a>


``` python
tf.data.make_one_shot_iterator(dataset)
```



<!-- Placeholder for "Used in" -->

Note: The returned iterator will be initialized automatically.
A "one-shot" iterator does not support re-initialization.

#### Args:


* <b>`dataset`</b>: A <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a>.


#### Returns:

A <a href="../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> over the elements of this dataset.
