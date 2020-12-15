description: Stacks a list of rank-R tensors into one rank-(R+1) tensor in parallel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.parallel_stack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.parallel_stack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L1299-L1348">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor in parallel.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.parallel_stack`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.parallel_stack(
    values, name='parallel_stack'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Requires that the shape of inputs be known at graph construction time.

Packs the list of tensors in `values` into a tensor with rank one higher than
each tensor in `values`, by packing them along the first dimension.
Given a list of length `N` of tensors of shape `(A, B, C)`; the `output`
tensor will have the shape `(N, A, B, C)`.

#### For example:



```python
x = tf.constant([1, 4])
y = tf.constant([2, 5])
z = tf.constant([3, 6])
tf.parallel_stack([x, y, z])  # [[1, 4], [2, 5], [3, 6]]
```

The difference between `stack` and `parallel_stack` is that `stack` requires
all the inputs be computed before the operation will begin but doesn't require
that the input shapes be known during graph construction.

`parallel_stack` will copy pieces of the input into the output as they become
available, in some situations this can provide a performance benefit.

Unlike `stack`, `parallel_stack` does NOT support backpropagation.

This is the opposite of unstack.  The numpy equivalent is

    tf.parallel_stack([x, y, z]) = np.asarray([x, y, z])

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A list of `Tensor` objects with the same shape and type.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
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
A stacked `Tensor` with the same type as `values`.
</td>
</tr>
</table>

