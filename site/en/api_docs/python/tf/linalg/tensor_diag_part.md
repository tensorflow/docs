description: Returns the diagonal part of the tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.tensor_diag_part" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.tensor_diag_part

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L2617-L2659">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the diagonal part of the tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.diag_part`, `tf.compat.v1.linalg.tensor_diag_part`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.tensor_diag_part(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation returns a tensor with the `diagonal` part
of the `input`. The `diagonal` part is computed as follows:

Assume `input` has dimensions `[D1,..., Dk, D1,..., Dk]`, then the output is a
tensor of rank `k` with dimensions `[D1,..., Dk]` where:

`diagonal[i1,..., ik] = input[i1, ..., ik, i1,..., ik]`.

For a rank 2 tensor, <a href="../../tf/linalg/diag_part.md"><code>linalg.diag_part</code></a> and <a href="../../tf/linalg/tensor_diag_part.md"><code>linalg.tensor_diag_part</code></a>
produce the same result. For rank 3 and higher, linalg.diag_part extracts
the diagonal of each inner-most matrix in the tensor. An example where
they differ is given below.

```
>>> x = [[[[1111,1112],[1121,1122]],
...       [[1211,1212],[1221,1222]]],
...      [[[2111, 2112], [2121, 2122]],
...       [[2211, 2212], [2221, 2222]]]
...      ]
>>> tf.linalg.tensor_diag_part(x)
<tf.Tensor: shape=(2, 2), dtype=int32, numpy=
array([[1111, 1212],
       [2121, 2222]], dtype=int32)>
>>> tf.linalg.diag_part(x).shape
TensorShape([2, 2, 2])
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
A `Tensor` with rank `2k`.
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
A Tensor containing diagonals of `input`. Has the same type as `input`, and
rank `k`.
</td>
</tr>

</table>

