description: Reduce elems using fn to combine them from left to right.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.foldl" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.foldl

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L6097-L6111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reduce elems using fn to combine them from left to right.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.foldl`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.foldl(
    fn, elems, initializer=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`fn`
</td>
<td>
Callable that will be called upon each element in elems and an
accumulator, for instance `lambda acc, x: acc + x`
</td>
</tr><tr>
<td>
`elems`
</td>
<td>
tensor
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
The first value used (`elems[0]` in case of None)
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string name for the foldl node in the graph
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tensor with same type and shape as `initializer`.
</td>
</tr>

</table>

