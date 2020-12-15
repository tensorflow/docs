description: Assert x has rank in ranks.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.assert_rank_in" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.assert_rank_in

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/check_ops.py#L1389-L1451">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Assert `x` has rank in `ranks`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.assert_rank_in`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.assert_rank_in(
    x, ranks, data=None, summarize=None, message=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_rank_in(x, (2, 4))]):
  output = tf.reduce_sum(x)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Numeric `Tensor`.
</td>
</tr><tr>
<td>
`ranks`
</td>
<td>
Iterable of scalar `Tensor` objects.
</td>
</tr><tr>
<td>
`data`
</td>
<td>
The tensors to print out if the condition is False.  Defaults to
error message and first few entries of `x`.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
Print this many entries of each tensor.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
A string to prefix to the default message.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
Defaults to "assert_rank_in".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Op raising `InvalidArgumentError` unless rank of `x` is in `ranks`.
If static checks determine `x` has matching rank, a `no_op` is returned.
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
If static checks determine `x` has mismatched rank.
</td>
</tr>
</table>

