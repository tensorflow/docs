description: Clips values of multiple tensors by the ratio of the sum of their norms.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.clip_by_global_norm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.clip_by_global_norm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/clip_ops.py#L289-L379">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Clips values of multiple tensors by the ratio of the sum of their norms.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.clip_by_global_norm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.clip_by_global_norm(
    t_list, clip_norm, use_norm=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a tuple or list of tensors `t_list`, and a clipping ratio `clip_norm`,
this operation returns a list of clipped tensors `list_clipped`
and the global norm (`global_norm`) of all tensors in `t_list`. Optionally,
if you've already computed the global norm for `t_list`, you can specify
the global norm with `use_norm`.

To perform the clipping, the values `t_list[i]` are set to:

    t_list[i] * clip_norm / max(global_norm, clip_norm)

where:

    global_norm = sqrt(sum([l2norm(t)**2 for t in t_list]))

If `clip_norm > global_norm` then the entries in `t_list` remain as they are,
otherwise they're all shrunk by the global ratio.

If `global_norm == infinity` then the entries in `t_list` are all set to `NaN`
to signal that an error occurred.

Any of the entries of `t_list` that are of type `None` are ignored.

This is the correct way to perform gradient clipping (Pascanu et al., 2012).

However, it is slower than `clip_by_norm()` because all the parameters must be
ready before the clipping operation can be performed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`t_list`
</td>
<td>
A tuple or list of mixed `Tensors`, `IndexedSlices`, or None.
</td>
</tr><tr>
<td>
`clip_norm`
</td>
<td>
A 0-D (scalar) `Tensor` > 0. The clipping ratio.
</td>
</tr><tr>
<td>
`use_norm`
</td>
<td>
A 0-D (scalar) `Tensor` of type `float` (optional). The global
norm to use. If not provided, `global_norm()` is used to compute the norm.
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
`list_clipped`
</td>
<td>
A list of `Tensors` of the same type as `list_t`.
</td>
</tr><tr>
<td>
`global_norm`
</td>
<td>
A 0-D (scalar) `Tensor` representing the global norm.
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
If `t_list` is not a sequence.
</td>
</tr>
</table>



#### References:

On the difficulty of training Recurrent Neural Networks:
  [Pascanu et al., 2012](http://proceedings.mlr.press/v28/pascanu13.html)
  ([pdf](http://proceedings.mlr.press/v28/pascanu13.pdf))
