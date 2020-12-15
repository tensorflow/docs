description: Returns a one-hot tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.one_hot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.one_hot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L3963-L4123">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a one-hot tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.one_hot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.one_hot(
    indices, depth, on_value=None, off_value=None, axis=None, dtype=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/fill.md"><code>tf.fill</code></a>, <a href="../tf/eye.md"><code>tf.eye</code></a>.

The locations represented by indices in `indices` take value `on_value`,
while all other locations take value `off_value`.

`on_value` and `off_value` must have matching data types. If `dtype` is also
provided, they must be the same data type as specified by `dtype`.

If `on_value` is not provided, it will default to the value `1` with type
`dtype`

If `off_value` is not provided, it will default to the value `0` with type
`dtype`

If the input `indices` is rank `N`, the output will have rank `N+1`. The
new axis is created at dimension `axis` (default: the new axis is appended
at the end).

If `indices` is a scalar the output shape will be a vector of length `depth`

If `indices` is a vector of length `features`, the output shape will be:

```
  features x depth if axis == -1
  depth x features if axis == 0
```

If `indices` is a matrix (batch) with shape `[batch, features]`, the output
shape will be:

```
  batch x features x depth if axis == -1
  batch x depth x features if axis == 1
  depth x batch x features if axis == 0
```

If `indices` is a RaggedTensor, the 'axis' argument must be positive and refer
to a non-ragged axis. The output will be equivalent to applying 'one_hot' on
the values of the RaggedTensor, and creating a new RaggedTensor from the
result.

If `dtype` is not provided, it will attempt to assume the data type of
`on_value` or `off_value`, if one or both are passed in. If none of
`on_value`, `off_value`, or `dtype` are provided, `dtype` will default to the
value <a href="../tf.md#float32"><code>tf.float32</code></a>.

Note: If a non-numeric data type output is desired (<a href="../tf.md#string"><code>tf.string</code></a>, <a href="../tf.md#bool"><code>tf.bool</code></a>,
etc.), both `on_value` and `off_value` _must_ be provided to `one_hot`.

#### For example:



```python
indices = [0, 1, 2]
depth = 3
tf.one_hot(indices, depth)  # output: [3 x 3]
# [[1., 0., 0.],
#  [0., 1., 0.],
#  [0., 0., 1.]]

indices = [0, 2, -1, 1]
depth = 3
tf.one_hot(indices, depth,
           on_value=5.0, off_value=0.0,
           axis=-1)  # output: [4 x 3]
# [[5.0, 0.0, 0.0],  # one_hot(0)
#  [0.0, 0.0, 5.0],  # one_hot(2)
#  [0.0, 0.0, 0.0],  # one_hot(-1)
#  [0.0, 5.0, 0.0]]  # one_hot(1)

indices = [[0, 2], [1, -1]]
depth = 3
tf.one_hot(indices, depth,
           on_value=1.0, off_value=0.0,
           axis=-1)  # output: [2 x 2 x 3]
# [[[1.0, 0.0, 0.0],   # one_hot(0)
#   [0.0, 0.0, 1.0]],  # one_hot(2)
#  [[0.0, 1.0, 0.0],   # one_hot(1)
#   [0.0, 0.0, 0.0]]]  # one_hot(-1)

indices = tf.ragged.constant([[0, 1], [2]])
depth = 3
tf.one_hot(indices, depth)  # output: [2 x None x 3]
# [[[1., 0., 0.],
#   [0., 1., 0.]],
#  [[0., 0., 1.]]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`
</td>
<td>
A `Tensor` of indices.
</td>
</tr><tr>
<td>
`depth`
</td>
<td>
A scalar defining the depth of the one hot dimension.
</td>
</tr><tr>
<td>
`on_value`
</td>
<td>
A scalar defining the value to fill in output when `indices[j]
= i`. (default: 1)
</td>
</tr><tr>
<td>
`off_value`
</td>
<td>
A scalar defining the value to fill in output when `indices[j]
!= i`. (default: 0)
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The axis to fill (default: -1, a new inner-most axis).
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The data type of the output tensor.
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

<tr>
<td>
`output`
</td>
<td>
The one-hot tensor.
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
If dtype of either `on_value` or `off_value` don't match `dtype`
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If dtype of `on_value` and `off_value` don't match one another
</td>
</tr>
</table>

