description: Adds all input tensors element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.add_n" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.add_n

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L3518-L3572">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adds all input tensors element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.add_n`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.add_n`, `tf.compat.v1.math.add_n`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.add_n(
    inputs, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

<a href="../../tf/math/add_n.md"><code>tf.math.add_n</code></a> performs the same operation as <a href="../../tf/math/accumulate_n.md"><code>tf.math.accumulate_n</code></a>, but it
waits for all of its inputs to be ready before beginning to sum.
This buffering can result in higher memory consumption when inputs are ready
at different times, since the minimum temporary storage required is
proportional to the input size rather than the output size.

This op does not [broadcast](
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)
its inputs. If you need broadcasting, use <a href="../../tf/math/add.md"><code>tf.math.add</code></a> (or the `+` operator)
instead.

#### For example:



```
>>> a = tf.constant([[3, 5], [4, 8]])
>>> b = tf.constant([[1, 6], [2, 9]])
>>> tf.math.add_n([a, b, a])
<tf.Tensor: shape=(2, 2), dtype=int32, numpy=
array([[ 7, 16],
       [10, 25]], dtype=int32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a> objects, each with the
same shape and type. <a href="../../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a> objects will be converted into
dense tensors prior to adding.
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
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of the same shape and type as the elements of `inputs`.
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
If `inputs` don't all have same shape and dtype or the shape
cannot be inferred.
</td>
</tr>
</table>

