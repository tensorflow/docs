description: Runs function f on a remote device indicated by target.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RemoteCall" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RemoteCall

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Runs function `f` on a remote device indicated by `target`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RemoteCall`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RemoteCall(
    target, args, Tout, f, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`target`
</td>
<td>
A `Tensor` of type `string`.
A fully specified device name where we want to run the function.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
A list of `Tensor` objects. A list of arguments for the function.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
The type list for the return values.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun. The function to run remotely.
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
A list of `Tensor` objects of type `Tout`.
</td>
</tr>

</table>

