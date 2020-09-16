description: Invokes a python function to compute func(input)->output.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.PyFunc" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.PyFunc

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Invokes a python function to compute func(input)->output.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.PyFunc`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.PyFunc(
    input, token, Tout, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation is considered stateful. For a stateless version, see
PyFuncStateless.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A list of `Tensor` objects.
List of Tensors that will provide input to the Op.
</td>
</tr><tr>
<td>
`token`
</td>
<td>
A `string`.
A token representing a registered python function in this address space.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes`. Data types of the outputs from the op.
The length of the list specifies the number of outputs.
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

