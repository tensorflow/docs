page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.get_next_as_optional


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/get_next_as_optional">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/iterator_ops.py#L800-L820">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an `Optional` that contains the next value from the iterator.

### Aliases:

* <a href="/api_docs/python/tf/data/experimental/get_next_as_optional"><code>tf.compat.v1.data.experimental.get_next_as_optional</code></a>
* <a href="/api_docs/python/tf/data/experimental/get_next_as_optional"><code>tf.compat.v2.data.experimental.get_next_as_optional</code></a>
* <a href="/api_docs/python/tf/data/experimental/get_next_as_optional"><code>tf.contrib.data.get_next_as_optional</code></a>


``` python
tf.data.experimental.get_next_as_optional(iterator)
```



<!-- Placeholder for "Used in" -->

If `iterator` has reached the end of the sequence, the returned `Optional`
will have no value.

#### Args:


* <b>`iterator`</b>: A <a href="../../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> object.


#### Returns:

An `Optional` object representing the next value from the iterator (if it
has one) or no value.
