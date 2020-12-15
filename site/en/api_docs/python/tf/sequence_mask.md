description: Returns a mask tensor representing the first N positions of each cell.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sequence_mask" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sequence_mask

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L4141-L4204">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a mask tensor representing the first N positions of each cell.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sequence_mask`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sequence_mask(
    lengths, maxlen=None, dtype=tf.dtypes.bool, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `lengths` has shape `[d_1, d_2, ..., d_n]` the resulting tensor `mask` has
dtype `dtype` and shape `[d_1, d_2, ..., d_n, maxlen]`, with

```
mask[i_1, i_2, ..., i_n, j] = (j < lengths[i_1, i_2, ..., i_n])
```

#### Examples:



```python
tf.sequence_mask([1, 3, 2], 5)  # [[True, False, False, False, False],
                                #  [True, True, True, False, False],
                                #  [True, True, False, False, False]]

tf.sequence_mask([[1, 3],[2,0]])  # [[[True, False, False],
                                  #   [True, True, True]],
                                  #  [[True, True, False],
                                  #   [False, False, False]]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`lengths`
</td>
<td>
integer tensor, all its values <= maxlen.
</td>
</tr><tr>
<td>
`maxlen`
</td>
<td>
scalar integer tensor, size of last dimension of returned tensor.
Default is the maximum value in `lengths`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
output type of the resulting tensor.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
name of the op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A mask tensor of shape `lengths.shape + (maxlen,)`, cast to specified dtype.
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
if `maxlen` is not a scalar.
</td>
</tr>
</table>

