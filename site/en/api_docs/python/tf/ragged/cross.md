description: Generates feature cross from a list of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.cross" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.cross

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/ragged_array_ops.py#L704-L728">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates feature cross from a list of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.cross`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.cross(
    inputs, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input tensors must have `rank=2`, and must all have the same number of
rows.  The result is a `RaggedTensor` with the same number of rows as the
inputs, where `result[row]` contains a list of all combinations of values
formed by taking a single value from each input's corresponding row
(`inputs[i][row]`).  Values are combined by joining their strings with '_X_'.
E.g.:

```
>>> tf.ragged.cross([tf.ragged.constant([['a'], ['b', 'c']]),
...                  tf.ragged.constant([['d'], ['e']]),
...                  tf.ragged.constant([['f'], ['g']])])
<tf.RaggedTensor [[b'a_X_d_X_f'], [b'b_X_e_X_g', b'c_X_e_X_g']]>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of `RaggedTensor` or `Tensor` or `SparseTensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 2D `RaggedTensor` of type `string`.
</td>
</tr>

</table>

