page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.row_splits_to_segment_ids


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/ragged/row_splits_to_segment_ids">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/segment_id_ops.py#L33-L73">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Generates the segmentation corresponding to a RaggedTensor `row_splits`.

### Aliases:

* <a href="/api_docs/python/tf/ragged/row_splits_to_segment_ids"><code>tf.compat.v1.ragged.row_splits_to_segment_ids</code></a>
* <a href="/api_docs/python/tf/ragged/row_splits_to_segment_ids"><code>tf.compat.v2.ragged.row_splits_to_segment_ids</code></a>


``` python
tf.ragged.row_splits_to_segment_ids(
    splits,
    name=None,
    out_type=None
)
```



<!-- Placeholder for "Used in" -->

Returns an integer vector `segment_ids`, where `segment_ids[i] == j` if
`splits[j] <= i < splits[j+1]`.  Example:

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}ragged.row_splits_to_segment_ids([0, 3, 3, 5, 6, 9]).eval(){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}[ 0 0 0 2 2 3 4 4 4 ]{% endhtmlescape %}</code>
</pre>

#### Args:


* <b>`splits`</b>: A sorted 1-D integer Tensor.  `splits[0]` must be zero.
* <b>`name`</b>: A name prefix for the returned tensor (optional).
* <b>`out_type`</b>: The dtype for the return value.  Defaults to `splits.dtype`,
  or <a href="../../tf#int64"><code>tf.int64</code></a> if `splits` does not have a dtype.


#### Returns:

A sorted 1-D integer Tensor, with `shape=[splits[-1]]`



#### Raises:


* <b>`ValueError`</b>: If `splits` is invalid.
