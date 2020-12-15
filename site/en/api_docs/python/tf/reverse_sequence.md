description: Reverses variable length slices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.reverse_sequence" />
<meta itemprop="path" content="Stable" />
</div>

# tf.reverse_sequence

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L4670-L4721">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reverses variable length slices.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.reverse_sequence(
    input, seq_lengths, seq_axis=None, batch_axis=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op first slices `input` along the dimension `batch_axis`, and for
each slice `i`, reverses the first `seq_lengths[i]` elements along the
dimension `seq_axis`.

The elements of `seq_lengths` must obey `seq_lengths[i] <=
input.dims[seq_axis]`, and `seq_lengths` must be a vector of length
`input.dims[batch_axis]`.

The output slice `i` along dimension `batch_axis` is then given by
input slice `i`, with the first `seq_lengths[i]` slices along
dimension `seq_axis` reversed.

#### Example usage:



```
>>> seq_lengths = [7, 2, 3, 5]
>>> input = [[1, 2, 3, 4, 5, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0],
...          [1, 2, 3, 4, 0, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8]]
>>> output = tf.reverse_sequence(input, seq_lengths, seq_axis=1, batch_axis=0)
>>> output
<tf.Tensor: shape=(4, 8), dtype=int32, numpy=
array([[0, 0, 5, 4, 3, 2, 1, 0],
       [2, 1, 0, 0, 0, 0, 0, 0],
       [3, 2, 1, 4, 0, 0, 0, 0],
       [5, 4, 3, 2, 1, 6, 7, 8]], dtype=int32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. The input to reverse.
</td>
</tr><tr>
<td>
`seq_lengths`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`,
`int64`. 1-D with length `input.dims(batch_axis)` and `max(seq_lengths) <=
input.dims(seq_axis)`
</td>
</tr><tr>
<td>
`seq_axis`
</td>
<td>
An `int`. The dimension which is partially reversed.
</td>
</tr><tr>
<td>
`batch_axis`
</td>
<td>
An optional `int`. Defaults to `0`. The dimension along which
reversal is performed.
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
A Tensor. Has the same type as input.
</td>
</tr>

</table>

