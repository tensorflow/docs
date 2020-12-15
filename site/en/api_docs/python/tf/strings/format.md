description: Formats a string template using a list of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.format" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.format

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/string_ops.py#L115-L175">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Formats a string template using a list of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.strings.format`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.format(
    template, inputs, placeholder='{}', summarize=3, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Formats a string template using a list of tensors, abbreviating tensors by
only printing the first and last `summarize` elements of each dimension
(recursively). If formatting only one tensor into a template, the tensor does
not have to be wrapped in a list.

#### Example:

Formatting a single-tensor template:

```
>>> tensor = tf.range(5)
>>> tf.strings.format("tensor: {}, suffix", tensor)
<tf.Tensor: shape=(), dtype=string, numpy=b'tensor: [0 1 2 3 4], suffix'>
```

Formatting a multi-tensor template:

```
>>> tensor_a = tf.range(2)
>>> tensor_b = tf.range(1, 4, 2)
>>> tf.strings.format("a: {}, b: {}, suffix", (tensor_a, tensor_b))
<tf.Tensor: shape=(), dtype=string, numpy=b'a: [0 1], b: [1 3], suffix'>
```




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`template`
</td>
<td>
A string template to format tensor values into.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A list of `Tensor` objects, or a single Tensor.
The list of tensors to format into the template string. If a solitary
tensor is passed in, the input tensor will automatically be wrapped as a
list.
</td>
</tr><tr>
<td>
`placeholder`
</td>
<td>
An optional `string`. Defaults to `{}`.
At each placeholder occurring in the template, a subsequent tensor
will be inserted.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
An optional `int`. Defaults to `3`.
When formatting the tensors, show the first and last `summarize`
entries of each tensor dimension (recursively). If set to -1, all
elements of the tensor will be shown.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` of type `string`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the number of placeholders does not match the number of
inputs.
</td>
</tr>
</table>

