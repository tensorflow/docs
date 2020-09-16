description: Finds values and indices of the k largest entries for the last dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.top_k" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.top_k

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/nn_ops.py#L5067-L5095">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Finds values and indices of the `k` largest entries for the last dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.nn.top_k`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.top_k`, `tf.compat.v1.nn.top_k`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.top_k(
    input, k=1, sorted=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If the input is a vector (rank=1), finds the `k` largest entries in the vector
and outputs their values and indices as vectors.  Thus `values[j]` is the
`j`-th largest entry in `input`, and its index is `indices[j]`.

For matrices (resp. higher rank input), computes the top `k` entries in each
row (resp. vector along the last dimension).  Thus,

    values.shape = indices.shape = input.shape[:-1] + [k]

If two elements are equal, the lower-index element appears first.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
1-D or higher `Tensor` with last dimension at least `k`.
</td>
</tr><tr>
<td>
`k`
</td>
<td>
0-D `int32` `Tensor`.  Number of top elements to look for along the last
dimension (along each row for matrices).
</td>
</tr><tr>
<td>
`sorted`
</td>
<td>
If true the resulting `k` elements will be sorted by the values in
descending order.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
The `k` largest elements along each last dimensional slice.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
The indices of `values` within the last dimension of `input`.
</td>
</tr>
</table>

