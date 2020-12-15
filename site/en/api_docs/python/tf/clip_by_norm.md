description: Clips tensor values to a maximum L2-norm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.clip_by_norm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.clip_by_norm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/clip_ops.py#L154-L235">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Clips tensor values to a maximum L2-norm.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.clip_by_norm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.clip_by_norm(
    t, clip_norm, axes=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a tensor `t`, and a maximum clip value `clip_norm`, this operation
normalizes `t` so that its L2-norm is less than or equal to `clip_norm`,
along the dimensions given in `axes`. Specifically, in the default case
where all dimensions are used for calculation, if the L2-norm of `t` is
already less than or equal to `clip_norm`, then `t` is not modified. If
the L2-norm is greater than `clip_norm`, then this operation returns a
tensor of the same type and shape as `t` with its values set to:

`t * clip_norm / l2norm(t)`

In this case, the L2-norm of the output tensor is `clip_norm`.

As another example, if `t` is a matrix and `axes == [1]`, then each row
of the output will have L2-norm less than or equal to `clip_norm`. If
`axes == [0]` instead, each column of the output will be clipped.

#### Code example:



```
>>> some_nums = tf.constant([[1, 2, 3, 4, 5]], dtype=tf.float32)
>>> tf.clip_by_norm(some_nums, 2.0).numpy()
array([[0.26967996, 0.5393599 , 0.80903983, 1.0787199 , 1.3483998 ]],
      dtype=float32)
```

This operation is typically used to clip gradients before applying them with
an optimizer.  Most gradient data is a collection of different shaped tensors
for different parts of the model.  Thus, this is a common usage:

```
# Get your gradients after training
loss_value, grads = grad(model, features, labels)

# Apply some clipping
grads = [tf.clip_by_norm(g, norm)
             for g in grads]

# Continue on with training
optimizer.apply_gradients(grads)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`t`
</td>
<td>
A `Tensor` or `IndexedSlices`.  This must be a floating point type.
</td>
</tr><tr>
<td>
`clip_norm`
</td>
<td>
A 0-D (scalar) `Tensor` > 0. A maximum clipping value, also
floating point
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
A 1-D (vector) `Tensor` of type int32 containing the dimensions
to use for computing the L2-norm. If `None` (the default), uses all
dimensions.
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
A clipped `Tensor` or `IndexedSlices`.
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
If the clip_norm tensor is not a 0-D scalar tensor.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If dtype of the input is not a floating point or
complex type.
</td>
</tr>
</table>

