description: Split a SparseTensor into num_split tensors along axis. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse_split" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.sparse_split

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/sparse_ops.py#L951-L1022">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Split a `SparseTensor` into `num_split` tensors along `axis`. (deprecated arguments)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.split`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.sparse_split(
    keyword_required=KeywordRequired(), sp_input=None, num_split=None, axis=None,
    name=None, split_dim=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(split_dim)`. They will be removed in a future version.
Instructions for updating:
split_dim is deprecated, use axis instead

If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split`
each slice starting from 0:`shape[axis] % num_split` gets extra one
dimension. For example, if `axis = 1` and `num_split = 2` and the
input is:

    input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

    output_tensor[0] =
    [    a   ]
    [b c     ]

    output_tensor[1] =
    [ d e  ]
    [      ]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`keyword_required`
</td>
<td>
Python 2 standin for * (temporary for argument reorder)
</td>
</tr><tr>
<td>
`sp_input`
</td>
<td>
The `SparseTensor` to split.
</td>
</tr><tr>
<td>
`num_split`
</td>
<td>
A Python integer. The number of ways to split.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A 0-D `int32` `Tensor`. The dimension along which to split.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`split_dim`
</td>
<td>
Deprecated old name for axis.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
`num_split` `SparseTensor` objects resulting from splitting `value`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `sp_input` is not a `SparseTensor`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the deprecated `split_dim` and `axis` are both non None.
</td>
</tr>
</table>

