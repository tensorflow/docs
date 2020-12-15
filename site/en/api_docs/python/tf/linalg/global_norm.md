description: Computes the global norm of multiple tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.global_norm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.global_norm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/clip_ops.py#L238-L286">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the global norm of multiple tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.global_norm`, `tf.compat.v1.linalg.global_norm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.global_norm(
    t_list, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a tuple or list of tensors `t_list`, this operation returns the
global norm of the elements in all tensors in `t_list`. The global norm is
computed as:

`global_norm = sqrt(sum([l2norm(t)**2 for t in t_list]))`

Any entries in `t_list` that are of type None are ignored.

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
A 0-D (scalar) `Tensor` of type `float`.
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

