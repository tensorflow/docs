description: Counts the number of occurrences of each value in an integer array.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.bincount" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.bincount

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/math_ops.py#L3467-L3497">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Counts the number of occurrences of each value in an integer array.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.bincount`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.bincount(
    arr, weights=None, minlength=None, maxlength=None, dtype=tf.dtypes.int32
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `minlength` and `maxlength` are not given, returns a vector with length
`tf.reduce_max(arr) + 1` if `arr` is non-empty, and length 0 otherwise.
If `weights` are non-None, then index `i` of the output stores the sum of the
value in `weights` at each index where the corresponding value in `arr` is
`i`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`arr`
</td>
<td>
An int32 tensor of non-negative values.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
If non-None, must be the same shape as arr. For each value in
`arr`, the bin will be incremented by the corresponding weight instead of
1.
</td>
</tr><tr>
<td>
`minlength`
</td>
<td>
If given, ensures the output has length at least `minlength`,
padding with zeros at the end if necessary.
</td>
</tr><tr>
<td>
`maxlength`
</td>
<td>
If given, skips values in `arr` that are equal or greater than
`maxlength`, ensuring that the output has length at most `maxlength`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
If `weights` is None, determines the type of the output bins.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A vector with the same dtype as `weights` or the given `dtype`. The bin
values.
</td>
</tr>

</table>

