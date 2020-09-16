description: Computes the GRU cell back-propagation for 1 time step.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.GRUBlockCellGrad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.GRUBlockCellGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the GRU cell back-propagation for 1 time step.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.GRUBlockCellGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.GRUBlockCellGrad(
    x, h_prev, w_ru, w_c, b_ru, b_c, r, u, c, d_h, name=None
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
    r: Output of the reset gate.
    u: Output of the update gate.
    c: Output of the cell connection gate.
    d_h: Gradients of the h_new wrt to objective function.

Returns
    d_x: Gradients of the x wrt to objective function.
    d_h_prev: Gradients of the h wrt to objective function.
    d_c_bar Gradients of the c_bar wrt to objective function.
    d_r_bar_u_bar Gradients of the r_bar & u_bar wrt to objective function.

This kernel op implements the following mathematical equations:

Note on notation of the variables:

Concatenation of a and b is represented by a_b
Element-wise dot product of a and b is represented by ab
Element-wise dot product is represented by \circ
Matrix multiplication is represented by *

Additional notes for clarity:

`w_ru` can be segmented into 4 different matrices.
```
w_ru = [w_r_x w_u_x
        w_r_h_prev w_u_h_prev]
```
Similarly, `w_c` can be segmented into 2 different matrices.
```
w_c = [w_c_x w_c_h_prevr]
```
Same goes for biases.
```
b_ru = [b_ru_x b_ru_h]
b_c = [b_c_x b_c_h]
```
Another note on notation:
```
d_x = d_x_component_1 + d_x_component_2

where d_x_component_1 = d_r_bar * w_r_x^T + d_u_bar * w_r_x^T
and d_x_component_2 = d_c_bar * w_c_x^T

d_h_prev = d_h_prev_component_1 + d_h_prevr \circ r + d_h \circ u
where d_h_prev_componenet_1 = d_r_bar * w_r_h_prev^T + d_u_bar * w_r_h_prev^T
```

Mathematics behind the Gradients below:
```
d_c_bar = d_h \circ (1-u) \circ (1-c \circ c)
d_u_bar = d_h \circ (h-c) \circ u \circ (1-u)

d_r_bar_u_bar = [d_r_bar d_u_bar]

[d_x_component_1 d_h_prev_component_1] = d_r_bar_u_bar * w_ru^T

[d_x_component_2 d_h_prevr] = d_c_bar * w_c^T

d_x = d_x_component_1 + d_x_component_2

d_h_prev = d_h_prev_component_1 + d_h_prevr \circ r + u
```
Below calculation is performed in the python wrapper for the Gradients
(not in the gradient kernel.)
```
d_w_ru = x_h_prevr^T * d_c_bar

d_w_c = x_h_prev^T * d_r_bar_u_bar

d_b_ru = sum of d_r_bar_u_bar along axis = 0

d_b_c = sum of d_c_bar along axis = 0
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
`r`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
</td>
</tr><tr>
<td>
`u`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
</td>
</tr><tr>
<td>
`c`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
</td>
</tr><tr>
<td>
`d_h`
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
A tuple of `Tensor` objects (d_x, d_h_prev, d_c_bar, d_r_bar_u_bar).
</td>
</tr>
<tr>
<td>
`d_x`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`d_h_prev`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`d_c_bar`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr><tr>
<td>
`d_r_bar_u_bar`
</td>
<td>
A `Tensor`. Has the same type as `x`.
</td>
</tr>
</table>

