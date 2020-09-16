description: Split a SparseTensor into num_split tensors along one dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseSplit" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseSplit

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Split a `SparseTensor` into `num_split` tensors along one dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseSplit`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseSplit(
    split_dim, indices, values, shape, num_split, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If the `shape[split_dim]` is not an integer multiple of `num_split`. Slices
`[0 : shape[split_dim] % num_split]` gets one extra dimension.
For example, if `split_dim = 1` and `num_split = 2` and the input is

    input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

    output_tensor[0] = shape = [2, 4]
    [    a  ]
    [b c    ]

    output_tensor[1] = shape = [2, 3]
    [ d e  ]
    [      ]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`split_dim`
</td>
<td>
A `Tensor` of type `int64`.
0-D.  The dimension along which to split.  Must be in the range
`[0, rank(shape))`.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D tensor represents the indices of the sparse tensor.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor`. 1-D tensor represents the values of the sparse tensor.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D. tensor represents the shape of the sparse tensor.
output indices: A list of 1-D tensors represents the indices of the output
sparse tensors.
</td>
</tr><tr>
<td>
`num_split`
</td>
<td>
An `int` that is `>= 1`. The number of ways to split.
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
A tuple of `Tensor` objects (output_indices, output_values, output_shape).
</td>
</tr>
<tr>
<td>
`output_indices`
</td>
<td>
A list of `num_split` `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`output_values`
</td>
<td>
A list of `num_split` `Tensor` objects with the same type as `values`.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A list of `num_split` `Tensor` objects with type `int64`.
</td>
</tr>
</table>

