description: Slice a SparseTensor based on the start and size.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseSlice" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseSlice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Slice a `SparseTensor` based on the `start` and `size`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseSlice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseSlice(
    indices, values, shape, start, size, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, if the input is

    input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

    sparse_slice([0, 0], [2, 4]) = shape = [2, 4]
    [    a  ]
    [b c    ]

    sparse_slice([0, 4], [2, 3]) = shape = [2, 3]
    [ d e  ]
    [      ]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
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
</td>
</tr><tr>
<td>
`start`
</td>
<td>
A `Tensor` of type `int64`.
1-D. tensor represents the start of the slice.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A `Tensor` of type `int64`.
1-D. tensor represents the size of the slice.
output indices: A list of 1-D tensors represents the indices of the output
sparse tensors.
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
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`output_values`
</td>
<td>
A `Tensor`. Has the same type as `values`.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

