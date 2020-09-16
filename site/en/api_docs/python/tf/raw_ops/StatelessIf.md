description: output = cond ? then_branch(input) : else_branch(input)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.StatelessIf" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.StatelessIf

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



output = cond ? then_branch(input) : else_branch(input)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatelessIf`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessIf(
    cond, input, Tout, then_branch, else_branch, output_shapes=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cond`
</td>
<td>
A `Tensor`.
A Tensor. If the tensor is a scalar of non-boolean type, the
scalar is converted to a boolean according to the
following rule: if the scalar is a numerical value, non-zero means
`True` and zero means False; if the scalar is a string, non-empty
means `True` and empty means `False`. If the tensor is not a scalar,
being empty means False and being non-empty means True.

This should only be used when the if then/else body functions do not
have stateful ops.
</td>
</tr><tr>
<td>
`input`
</td>
<td>
A list of `Tensor` objects. A list of input tensors.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes`. A list of output types.
</td>
</tr><tr>
<td>
`then_branch`
</td>
<td>
A function decorated with @Defun.
A function that takes 'inputs' and returns a list of tensors, whose
types are the same as what else_branch returns.
</td>
</tr><tr>
<td>
`else_branch`
</td>
<td>
A function decorated with @Defun.
A function that takes 'inputs' and returns a list of tensors, whose
types are the same as what then_branch returns.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
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

