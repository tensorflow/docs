description: Creates a sequence of numbers.

robots: noindex

# tf.raw_ops.Range

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a sequence of numbers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Range`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Range(
    start, limit, delta, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation creates a sequence of numbers that begins at `start` and
extends by increments of `delta` up to but not including `limit`.

#### For example:



```
# 'start' is 3
# 'limit' is 18
# 'delta' is 3
tf.range(start, limit, delta) ==> [3, 6, 9, 12, 15]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`start`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`.
0-D (scalar). First entry in the sequence.
</td>
</tr><tr>
<td>
`limit`
</td>
<td>
A `Tensor`. Must have the same type as `start`.
0-D (scalar). Upper limit of sequence, exclusive.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
A `Tensor`. Must have the same type as `start`.
0-D (scalar). Optional. Default is 1. Number that increments `start`.
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
A `Tensor`. Has the same type as `start`.
</td>
</tr>

</table>

