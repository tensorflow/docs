description: Returns a one-hot tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.OneHot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.OneHot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns a one-hot tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.OneHot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.OneHot(
    indices, depth, on_value, off_value, axis=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The locations represented by indices in `indices` take value `on_value`,
while all other locations take value `off_value`.

If the input `indices` is rank `N`, the output will have rank `N+1`,
The new axis is created at dimension `axis` (default: the new axis is
appended at the end).

If `indices` is a scalar the output shape will be a vector of length `depth`.

If `indices` is a vector of length `features`, the output shape will be:
```
  features x depth if axis == -1
  depth x features if axis == 0
```

If `indices` is a matrix (batch) with shape `[batch, features]`,
the output shape will be:
```
  batch x features x depth if axis == -1
  batch x depth x features if axis == 1
  depth x batch x features if axis == 0
```


Examples
=========

Suppose that
```
  indices = [0, 2, -1, 1]
  depth = 3
  on_value = 5.0
  off_value = 0.0
  axis = -1
```

Then output is `[4 x 3]`:
```
output =
  [5.0 0.0 0.0]  // one_hot(0)
  [0.0 0.0 5.0]  // one_hot(2)
  [0.0 0.0 0.0]  // one_hot(-1)
  [0.0 5.0 0.0]  // one_hot(1)
```

Suppose that
```
  indices = [0, 2, -1, 1]
  depth = 3
  on_value = 0.0
  off_value = 3.0
  axis = 0
```

Then output is `[3 x 4]`:
```
output =
  [0.0 3.0 3.0 3.0]
  [3.0 3.0 3.0 0.0]
  [3.0 3.0 3.0 3.0]
  [3.0 0.0 3.0 3.0]
//  ^                one_hot(0)
//      ^            one_hot(2)
//          ^        one_hot(-1)
//              ^    one_hot(1)
```

Suppose that
```
  indices = [[0, 2], [1, -1]]
  depth = 3
  on_value = 1.0
  off_value = 0.0
  axis = -1
```

Then output is `[2 x 2 x 3]`:
```
output =
  [
    [1.0, 0.0, 0.0]  // one_hot(0)
    [0.0, 0.0, 1.0]  // one_hot(2)
  ][
    [0.0, 1.0, 0.0]  // one_hot(1)
    [0.0, 0.0, 0.0]  // one_hot(-1)
  ]
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
A `Tensor`. Must be one of the following types: `uint8`, `int32`, `int64`.
A tensor of indices.
</td>
</tr><tr>
<td>
`depth`
</td>
<td>
A `Tensor` of type `int32`.
A scalar defining the depth of the one hot dimension.
</td>
</tr><tr>
<td>
`on_value`
</td>
<td>
A `Tensor`.
A scalar defining the value to fill in output when `indices[j] = i`.
</td>
</tr><tr>
<td>
`off_value`
</td>
<td>
A `Tensor`. Must have the same type as `on_value`.
A scalar defining the value to fill in output when `indices[j] != i`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An optional `int`. Defaults to `-1`.
The axis to fill (default: -1, a new inner-most axis).
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
A `Tensor`. Has the same type as `on_value`.
</td>
</tr>

</table>

