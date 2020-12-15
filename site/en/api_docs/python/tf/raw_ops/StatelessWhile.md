description: output = input; While (Cond(output)) { output = Body(output) }

robots: noindex

# tf.raw_ops.StatelessWhile

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



output = input; While (Cond(output)) { output = Body(output) }

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatelessWhile`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessWhile(
    input, cond, body, output_shapes=[], parallel_iterations=10, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
A list of input tensors whose types are T.
</td>
</tr><tr>
<td>
`cond`
</td>
<td>
A function decorated with @Defun.
A function takes 'input' and returns a tensor.  If the tensor is
a scalar of non-boolean, the scalar is converted to a boolean
according to the following rule: if the scalar is a numerical
value, non-zero means True and zero means False; if the scalar is
a string, non-empty means True and empty means False. If the
tensor is not a scalar, non-emptiness means True and False
otherwise.

This should only be used when the while condition and body functions
do not have stateful ops.
</td>
</tr><tr>
<td>
`body`
</td>
<td>
A function decorated with @Defun.
A function that takes a list of tensors and returns another
list of tensors. Both lists have the same types as specified
by T.
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
`parallel_iterations`
</td>
<td>
An optional `int`. Defaults to `10`.
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
A list of `Tensor` objects. Has the same type as `input`.
</td>
</tr>

</table>

