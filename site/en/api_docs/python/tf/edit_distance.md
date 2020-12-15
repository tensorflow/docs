description: Computes the Levenshtein distance between sequences.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.edit_distance" />
<meta itemprop="path" content="Stable" />
</div>

# tf.edit_distance

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L3620-L3722">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the Levenshtein distance between sequences.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.edit_distance`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.edit_distance(
    hypothesis, truth, normalize=(True), name='edit_distance'
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation takes variable-length sequences (`hypothesis` and `truth`),
each provided as a `SparseTensor`, and computes the Levenshtein distance.
You can normalize the edit distance by length of `truth` by setting
`normalize` to true.

#### For example:



Given the following input,
* `hypothesis` is a <a href="../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a> of shape `[2, 1, 1]`
* `truth` is a <a href="../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a> of shape `[2, 2, 2]`

```
>>> hypothesis = tf.SparseTensor(
...   [[0, 0, 0],
...    [1, 0, 0]],
...   ["a", "b"],
...   (2, 1, 1))
>>> truth = tf.SparseTensor(
...   [[0, 1, 0],
...    [1, 0, 0],
...    [1, 0, 1],
...    [1, 1, 0]],
...    ["a", "b", "c", "a"],
...    (2, 2, 2))
>>> tf.edit_distance(hypothesis, truth, normalize=True)
<tf.Tensor: shape=(2, 2), dtype=float32, numpy=
array([[inf, 1. ],
       [0.5, 1. ]], dtype=float32)>
```

The operaton returns a dense Tensor of shape `[2, 2]` with
edit distances normalized by `truth` lengths.

**Note**: It is possible to calculate edit distance between two
sparse tensors with variable-length values. However, attempting to create
them while eager execution is enabled will result in a `ValueError`.

For the following  inputs,

```python
# 'hypothesis' is a tensor of shape `[2, 1]` with variable-length values:
#   (0,0) = ["a"]
#   (1,0) = ["b"]
hypothesis = tf.sparse.SparseTensor(
    [[0, 0, 0],
     [1, 0, 0]],
    ["a", "b"],
    (2, 1, 1))

# 'truth' is a tensor of shape `[2, 2]` with variable-length values:
#   (0,0) = []
#   (0,1) = ["a"]
#   (1,0) = ["b", "c"]
#   (1,1) = ["a"]
truth = tf.sparse.SparseTensor(
    [[0, 1, 0],
     [1, 0, 0],
     [1, 0, 1],
     [1, 1, 0]],
    ["a", "b", "c", "a"],
    (2, 2, 2))

normalize = True

# The output would be a dense Tensor of shape `(2,)`, with edit distances
noramlized by 'truth' lengths.
# output => array([0., 0.5], dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`hypothesis`
</td>
<td>
A `SparseTensor` containing hypothesis sequences.
</td>
</tr><tr>
<td>
`truth`
</td>
<td>
A `SparseTensor` containing truth sequences.
</td>
</tr><tr>
<td>
`normalize`
</td>
<td>
A `bool`. If `True`, normalizes the Levenshtein distance by
length of `truth.`
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
A dense `Tensor` with rank `R - 1`, where R is the rank of the
`SparseTensor` inputs `hypothesis` and `truth`.
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
If either `hypothesis` or `truth` are not a `SparseTensor`.
</td>
</tr>
</table>

