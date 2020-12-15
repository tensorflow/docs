description: Increments 'ref' until it reaches 'limit'. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.count_up_to" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.count_up_to

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/state_ops.py#L231-L252">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Increments 'ref' until it reaches 'limit'. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.count_up_to(
    ref, limit, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Prefer Dataset.range instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
A Variable. Must be one of the following types: `int32`, `int64`.
Should be from a scalar `Variable` node.
</td>
</tr><tr>
<td>
`limit`
</td>
<td>
An `int`.
If incrementing ref would bring it above limit, instead generates an
'OutOfRange' error.
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
A `Tensor`. Has the same type as `ref`.
A copy of the input before increment. If nothing else modifies the
input, the values produced will all be distinct.
</td>
</tr>

</table>

