description: Concatenates a list of SparseTensor along the specified dimension. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse_concat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.sparse_concat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L271-L384">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Concatenates a list of `SparseTensor` along the specified dimension. (deprecated arguments)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.concat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.sparse_concat(
    axis, sp_inputs, name=None, expand_nonconcat_dim=(False), concat_dim=None,
    expand_nonconcat_dims=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(concat_dim)`. They will be removed in a future version.
Instructions for updating:
concat_dim is deprecated, use axis instead

Concatenation is with respect to the dense versions of each sparse input.
It is assumed that each inputs is a `SparseTensor` whose elements are ordered
along increasing dimension number.

If expand_nonconcat_dim is False, all inputs' shapes must match, except for
the concat dimension. If expand_nonconcat_dim is True, then inputs' shapes are
allowed to vary among all inputs.

The `indices`, `values`, and `shapes` lists must have the same length.

If expand_nonconcat_dim is False, then the output shape is identical to the
inputs', except along the concat dimension, where it is the sum of the inputs'
sizes along that dimension.

If expand_nonconcat_dim is True, then the output shape along the non-concat
dimensions will be expand to be the largest among all inputs, and it is the
sum of the inputs sizes along the concat dimension.

The output elements will be resorted to preserve the sort order along
increasing dimension number.

This op runs in `O(M log M)` time, where `M` is the total number of non-empty
values across all inputs. This is due to the need for an internal sort in
order to concatenate efficiently across an arbitrary dimension.

For example, if `axis = 1` and the inputs are

    sp_inputs[0]: shape = [2, 3]
    [0, 2]: "a"
    [1, 0]: "b"
    [1, 1]: "c"

    sp_inputs[1]: shape = [2, 4]
    [0, 1]: "d"
    [0, 2]: "e"

then the output will be

    shape = [2, 7]
    [0, 2]: "a"
    [0, 4]: "d"
    [0, 5]: "e"
    [1, 0]: "b"
    [1, 1]: "c"

Graphically this is equivalent to doing

    [    a] concat [  d e  ] = [    a   d e  ]
    [b c  ]        [       ]   [b c          ]

Another example, if 'axis = 1' and the inputs are

    sp_inputs[0]: shape = [3, 3]
    [0, 2]: "a"
    [1, 0]: "b"
    [2, 1]: "c"

    sp_inputs[1]: shape = [2, 4]
    [0, 1]: "d"
    [0, 2]: "e"

if expand_nonconcat_dim = False, this will result in an error. But if
expand_nonconcat_dim = True, this will result in:

    shape = [3, 7]
    [0, 2]: "a"
    [0, 4]: "d"
    [0, 5]: "e"
    [1, 0]: "b"
    [2, 1]: "c"

Graphically this is equivalent to doing

    [    a] concat [  d e  ] = [    a   d e  ]
    [b    ]        [       ]   [b            ]
    [  c  ]                    [  c          ]


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Dimension to concatenate along. Must be in range [-rank, rank),
where rank is the number of dimensions in each input `SparseTensor`.
</td>
</tr><tr>
<td>
`sp_inputs`
</td>
<td>
List of `SparseTensor` to concatenate.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional).
</td>
</tr><tr>
<td>
`expand_nonconcat_dim`
</td>
<td>
Whether to allow the expansion in the non-concat
dimensions. Defaulted to False.
</td>
</tr><tr>
<td>
`concat_dim`
</td>
<td>
The old (deprecated) name for axis.
</td>
</tr><tr>
<td>
`expand_nonconcat_dims`
</td>
<td>
alias for expand_nonconcat_dim
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` with the concatenated output.
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
If `sp_inputs` is not a list of `SparseTensor`.
</td>
</tr>
</table>

