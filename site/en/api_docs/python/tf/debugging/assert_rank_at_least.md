description: Assert that x has rank of at least rank.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.assert_rank_at_least" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.assert_rank_at_least

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/check_ops.py#L1189-L1220">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Assert that `x` has rank of at least `rank`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.debugging.assert_rank_at_least(
    x, rank, message=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This Op checks that the rank of `x` is greater or equal to `rank`.

If `x` has a rank lower than `rank`, `message`, as well as the shape of `x`
are printed, and `InvalidArgumentError` is raised.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor`.
</td>
</tr><tr>
<td>
`rank`
</td>
<td>
Scalar integer `Tensor`.
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
A name for this operation (optional).  Defaults to
"assert_rank_at_least".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Op raising `InvalidArgumentError` unless `x` has specified rank or higher.
If static checks determine `x` has correct rank, a `no_op` is returned.
This can be used with <a href="../../tf/control_dependencies.md"><code>tf.control_dependencies</code></a> inside of <a href="../../tf/function.md"><code>tf.function</code></a>s
to block followup computation until the check has executed.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
`x` does not have rank at least `rank`, but the rank
cannot be statically determined.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If static checks determine `x` has mismatched rank.
</td>
</tr>
</table>



#### Eager Compatibility
returns None

