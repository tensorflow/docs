page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.take_while


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/take_while">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/take_while_ops.py#L55-L72">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A transformation that stops dataset iteration based on a `predicate`.

### Aliases:

* <a href="/api_docs/python/tf/data/experimental/take_while"><code>tf.compat.v1.data.experimental.take_while</code></a>
* <a href="/api_docs/python/tf/data/experimental/take_while"><code>tf.compat.v2.data.experimental.take_while</code></a>


``` python
tf.data.experimental.take_while(predicate)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`predicate`</b>: A function that maps a nested structure of tensors (having shapes
  and types defined by `self.output_shapes` and `self.output_types`) to a
  scalar <a href="../../../tf#bool"><code>tf.bool</code></a> tensor.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
