description: Pads a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.pad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.pad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/array_ops.py#L3144-L3199">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Pads a tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.pad(
    tensor, paddings, mode='CONSTANT', constant_values=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation pads a `tensor` according to the `paddings` you specify.
`paddings` is an integer tensor with shape `[n, 2]`, where n is the rank of
`tensor`. For each dimension D of `input`, `paddings[D, 0]` indicates how
many values to add before the contents of `tensor` in that dimension, and
`paddings[D, 1]` indicates how many values to add after the contents of
`tensor` in that dimension. If `mode` is "REFLECT" then both `paddings[D, 0]`
and `paddings[D, 1]` must be no greater than `tensor.dim_size(D) - 1`. If
`mode` is "SYMMETRIC" then both `paddings[D, 0]` and `paddings[D, 1]` must be
no greater than `tensor.dim_size(D)`.

The padded size of each dimension D of the output is:

`paddings[D, 0] + tensor.dim_size(D) + paddings[D, 1]`

#### For example:



```python
t = tf.constant([[1, 2, 3], [4, 5, 6]])
paddings = tf.constant([[1, 1,], [2, 2]])
# 'constant_values' is 0.
# rank of 't' is 2.
tf.pad(t, paddings, "CONSTANT")  # [[0, 0, 0, 0, 0, 0, 0],
                                 #  [0, 0, 1, 2, 3, 0, 0],
                                 #  [0, 0, 4, 5, 6, 0, 0],
                                 #  [0, 0, 0, 0, 0, 0, 0]]

tf.pad(t, paddings, "REFLECT")  # [[6, 5, 4, 5, 6, 5, 4],
                                #  [3, 2, 1, 2, 3, 2, 1],
                                #  [6, 5, 4, 5, 6, 5, 4],
                                #  [3, 2, 1, 2, 3, 2, 1]]

tf.pad(t, paddings, "SYMMETRIC")  # [[2, 1, 1, 2, 3, 3, 2],
                                  #  [2, 1, 1, 2, 3, 3, 2],
                                  #  [5, 4, 4, 5, 6, 6, 5],
                                  #  [5, 4, 4, 5, 6, 6, 5]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`paddings`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
One of "CONSTANT", "REFLECT", or "SYMMETRIC" (case-insensitive)
</td>
</tr><tr>
<td>
`constant_values`
</td>
<td>
In "CONSTANT" mode, the scalar pad value to use. Must be
same type as `tensor`.
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
A `Tensor`. Has the same type as `tensor`.
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
When mode is not one of "CONSTANT", "REFLECT", or "SYMMETRIC".
</td>
</tr>
</table>

