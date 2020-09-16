description: Returns the dlpack capsule representing the tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.dlpack.to_dlpack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.experimental.dlpack.to_dlpack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/dlpack/dlpack.py#L26-L45">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the dlpack capsule representing the tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.dlpack.to_dlpack(
    tf_tensor
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation ensures the underlying data memory is ready when returns.

  ```python
  a = tf.tensor([1, 10])
  dlcapsule = tf.experimental.dlpack.to_dlpack(a)
  # dlcapsule represents the dlpack data structure
  ```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tf_tensor`
</td>
<td>
Tensorflow eager tensor, to be converted to dlpack capsule.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A PyCapsule named as dltensor, which shares the underlying memory to other
framework. This PyCapsule can be consumed only once.
</td>
</tr>

</table>

