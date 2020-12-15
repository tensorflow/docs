description: Generates hashed feature cross from a list of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.cross_hashed" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.cross_hashed

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ragged/ragged_array_ops.py#L731-L765">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates hashed feature cross from a list of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.cross_hashed`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.cross_hashed(
    inputs, num_buckets=0, hash_key=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input tensors must have `rank=2`, and must all have the same number of
rows.  The result is a `RaggedTensor` with the same number of rows as the
inputs, where `result[row]` contains a list of all combinations of values
formed by taking a single value from each input's corresponding row
(`inputs[i][row]`).  Values are combined by hashing together their
fingerprints. E.g.:

```
>>> tf.ragged.cross_hashed([tf.ragged.constant([['a'], ['b', 'c']]),
...                         tf.ragged.constant([['d'], ['e']]),
...                         tf.ragged.constant([['f'], ['g']])],
...                        num_buckets=100)
<tf.RaggedTensor [[78], [66, 74]]>
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
`num_buckets`
</td>
<td>
A non-negative `int` that used to bucket the hashed values. If
`num_buckets != 0`, then `output = hashed_value % num_buckets`.
</td>
</tr><tr>
<td>
`hash_key`
</td>
<td>
Integer hash_key that will be used by the `FingerprintCat64`
function. If not given, a default key is used.
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
A 2D `RaggedTensor` of type `int64`.
</td>
</tr>

</table>

