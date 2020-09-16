description: Computes the GRU cell forward propagation for 1 time step.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.GRUBlockCell" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.GRUBlockCell

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the GRU cell forward propagation for 1 time step.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.GRUBlockCell`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.GRUBlockCell(
    x, h_prev, w_ru, w_c, b_ru, b_c, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Args
    x: Input to the GRU cell.
    h_prev: State input from the previous GRU cell.
    w_ru: Weight matrix for the reset and update gate.
    w_c: Weight matrix for the cell connection gate.
    b_ru: Bias vector for the reset and update gate.
    b_c: Bias vector for the cell connection gate.

Returns
    r: Output of the reset gate.
    u: Output of the update gate.
    c: Output of the cell connection gate.
    h: Current state of the GRU cell.

Note on notation of the variables:

Concatenation of a and b is represented by a_b
Element-wise dot product of a and b is represented by ab
Element-wise dot product is represented by \circ
Matrix multiplication is represented by *

Biases are initialized with :
`b_ru` - constant_initializer(1.0)
`b_c` - constant_initializer(0.0)

This kernel op implements the following mathematical equations:

```
x_h_prev = [x, h_prev]

[r_bar u_bar] = x_h_prev * w_ru + b_ru

r = sigmoid(r_bar)
u = sigmoid(u_bar)

h_prevr = h_prev \circ r

x_h_prevr = [x h_prevr]

c_bar = x_h_prevr * w_c + b_c
c = tanh(c_bar)

h = (1-u) \circ c + u \circ h_prev
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`.
</td>
</tr><tr>
<td>
`h_prev`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
</td>
</tr><tr>
<td>
`w_ru`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
</td>
</tr><tr>
<td>
`w_c`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
</td>
</tr><tr>
<td>
`b_ru`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
</td>
</tr><tr>
<td>
`b_c`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
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
A tuple of `Tensor` objects (r, u, c, h).
</td>
</tr>
<tr>
<td>
`r`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`u`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`c`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`h`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr>
</table>

