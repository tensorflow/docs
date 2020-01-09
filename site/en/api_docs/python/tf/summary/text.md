page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.text


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/summary/text">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/summary/summary.py#L233-L271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Summarizes textual data.

### Aliases:

* <a href="/api_docs/python/tf/summary/text"><code>tf.compat.v1.summary.text</code></a>


``` python
tf.summary.text(
    name,
    tensor,
    collections=None
)
```



<!-- Placeholder for "Used in" -->

Text data summarized via this plugin will be visible in the Text Dashboard
in TensorBoard. The standard TensorBoard Text Dashboard will render markdown
in the strings, and will automatically organize 1d and 2d tensors into tables.
If a tensor with more than 2 dimensions is provided, a 2d subarray will be
displayed along with a warning message. (Note that this behavior is not
intrinsic to the text summary api, but rather to the default TensorBoard text
plugin.)

#### Args:


* <b>`name`</b>: A name for the generated node. Will also serve as a series name in
  TensorBoard.
* <b>`tensor`</b>: a string-type Tensor to summarize.
* <b>`collections`</b>: Optional list of ops.GraphKeys.  The collections to add the
  summary to.  Defaults to [_ops.GraphKeys.SUMMARIES]


#### Returns:

A TensorSummary op that is configured so that TensorBoard will recognize
that it contains textual data. The TensorSummary is a scalar `Tensor` of
type `string` which contains `Summary` protobufs.



#### Raises:


* <b>`ValueError`</b>: If tensor has the wrong type.
