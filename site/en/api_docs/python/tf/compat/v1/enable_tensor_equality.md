description: Compare Tensors with element-wise comparison and thus be unhashable.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.enable_tensor_equality" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.enable_tensor_equality

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L235-L245">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compare Tensors with element-wise comparison and thus be unhashable.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.enable_tensor_equality()
</code></pre>



<!-- Placeholder for "Used in" -->

Comparing tensors with element-wise allows comparisons such as
tf.Variable(1.0) == 1.0. Element-wise equality implies that tensors are
unhashable. Thus tensors can no longer be directly used in sets or as a key in
a dictionary.