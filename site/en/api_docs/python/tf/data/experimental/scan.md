page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.scan


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/scan">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/scan_ops.py#L143-L167">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A transformation that scans a function across an input dataset.

### Aliases:

* <a href="/api_docs/python/tf/data/experimental/scan"><code>tf.compat.v1.data.experimental.scan</code></a>
* <a href="/api_docs/python/tf/data/experimental/scan"><code>tf.compat.v2.data.experimental.scan</code></a>


``` python
tf.data.experimental.scan(
    initial_state,
    scan_func
)
```



<!-- Placeholder for "Used in" -->

This transformation is a stateful relative of <a href="../../../tf/data/Dataset#map"><code>tf.data.Dataset.map</code></a>.
In addition to mapping `scan_func` across the elements of the input dataset,
`scan()` accumulates one or more state tensors, whose initial values are
`initial_state`.

#### Args:


* <b>`initial_state`</b>: A nested structure of tensors, representing the initial state
  of the accumulator.
* <b>`scan_func`</b>: A function that maps `(old_state, input_element)` to
  `(new_state, output_element). It must take two arguments and return a
  pair of nested structures of tensors. The `new_state` must match the
  structure of `initial_state`.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
