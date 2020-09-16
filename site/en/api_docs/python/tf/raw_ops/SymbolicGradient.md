description: Computes the gradient function for function f via backpropagation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SymbolicGradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SymbolicGradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradient function for function f via backpropagation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SymbolicGradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SymbolicGradient(
    input, Tout, f, name=None
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
A list of `Tensor` objects. a list of input tensors of size N + M;
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
the type list for the input list.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun.
The function we want to compute the gradient for.

The function 'f' must be a numerical function which takes N inputs and
produces M outputs. Its gradient function 'g', which is computed by
this SymbolicGradient op is a function taking N + M inputs and
produces N outputs.

I.e. if we have
(y1, y2, ..., y_M) = f(x1, x2, ..., x_N),
then, g is
(dL/dx1, dL/dx2, ..., dL/dx_N) = g(x1, x2, ..., x_N,
dL/dy1, dL/dy2, ..., dL/dy_M),

where L is a scalar-value function of (x1, x2, ..., xN) (e.g., the
loss function). dL/dx_i is the partial derivative of L with respect
to x_i.

(Needs some math expert to say the comment above better.)
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

