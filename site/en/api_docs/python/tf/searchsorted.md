description: Searches input tensor for values on the innermost dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.searchsorted" />
<meta itemprop="path" content="Stable" />
</div>

# tf.searchsorted

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L5284-L5343">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Searches input tensor for values on the innermost dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.searchsorted`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.searchsorted(
    sorted_sequence, values, side='left', out_type=tf.dtypes.int32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A 2-D example:

```
  sorted_sequence = [[0, 3, 9, 9, 10],
                     [1, 2, 3, 4, 5]]
  values = [[2, 4, 9],
            [0, 2, 6]]

  result = searchsorted(sorted_sequence, values, side="left")

  result == [[1, 2, 2],
             [0, 1, 5]]

  result = searchsorted(sorted_sequence, values, side="right")

  result == [[1, 2, 4],
             [0, 2, 5]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sorted_sequence`
</td>
<td>
N-D `Tensor` containing a sorted sequence.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
N-D `Tensor` containing the search values.
</td>
</tr><tr>
<td>
`side`
</td>
<td>
'left' or 'right'; 'left' corresponds to lower_bound and 'right' to
upper_bound.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
The output type (`int32` or `int64`).  Default is <a href="../tf.md#int32"><code>tf.int32</code></a>.
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
<tr class="alt">
<td colspan="2">
An N-D `Tensor` the size of values containing the result of applying either
lower_bound or upper_bound (depending on side) to each value.  The result
is not a global index to the entire `Tensor`, but the index in the last
dimension.
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
If the last dimension of `sorted_sequence >= 2^31-1` elements.
If the total size of values exceeds `2^31 - 1` elements.
If the first `N-1` dimensions of the two tensors don't match.
</td>
</tr>
</table>

