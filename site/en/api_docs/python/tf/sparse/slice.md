description: Slice a SparseTensor based on the start and size.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.slice" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.slice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L1096-L1143">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Slice a `SparseTensor` based on the `start` and `size.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.slice`, `tf.compat.v1.sparse_slice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.slice(
    sp_input, start, size, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, if the input is

    input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

    sparse.slice([0, 0], [2, 4]) = shape = [2, 4]
    [    a  ]
    [b c    ]

    sparse.slice([0, 4], [2, 3]) = shape = [2, 3]
    [ d e  ]
    [      ]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
The `SparseTensor` to split.
</td>
</tr><tr>
<td>
`start`
</td>
<td>
1-D. tensor represents the start of the slice.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
1-D. tensor represents the size of the slice.
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
A `SparseTensor` objects resulting from splicing.
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
</tr>
</table>

