description: Gather slices from params axis axis according to indices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.gather" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.gather

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/array_ops.py#L4435-L4524">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Gather slices from params axis `axis` according to indices.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.gather(
    params, indices, validate_indices=None, name=None, axis=None, batch_dims=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

Gather slices from params axis `axis` according to `indices`.  `indices` must
be an integer tensor of any dimension (usually 0-D or 1-D).

For 0-D (scalar) `indices`:

$$\begin{align*}
output[p_0, ..., p_{axis-1}, &&          &&& p_{axis + 1}, ..., p_{N-1}] = \\
params[p_0, ..., p_{axis-1}, && indices, &&& p_{axis + 1}, ..., p_{N-1}]
\end{align*}$$

Where *N* = `ndims(params)`.

For 1-D (vector) `indices` with `batch_dims=0`:

$$\begin{align*}
output[p_0, ..., p_{axis-1}, &&         &i,  &&p_{axis + 1}, ..., p_{N-1}] =\\
params[p_0, ..., p_{axis-1}, && indices[&i], &&p_{axis + 1}, ..., p_{N-1}]
\end{align*}$$

In the general case, produces an output tensor where:

$$\begin{align*}
output[p_0,             &..., p_{axis-1},                       &
       &i_{B},           ..., i_{M-1},                          &
       p_{axis + 1},    &..., p_{N-1}]                          = \\
params[p_0,             &..., p_{axis-1},                       &
       indices[p_0, ..., p_{B-1}, &i_{B}, ..., i_{M-1}],        &
       p_{axis + 1},    &..., p_{N-1}]
\end{align*}$$

Where *N* = `ndims(params)`, *M* = `ndims(indices)`, and *B* = `batch_dims`.
Note that `params.shape[:batch_dims]` must be identical to
`indices.shape[:batch_dims]`.

The shape of the output tensor is:

> `output.shape = params.shape[:axis] + indices.shape[batch_dims:] +
> params.shape[axis + 1:]`.

Note that on CPU, if an out of bound index is found, an error is returned.
On GPU, if an out of bound index is found, a 0 is stored in the corresponding
output value.

See also <a href="../../../tf/gather_nd.md"><code>tf.gather_nd</code></a>.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/Gather.png"
alt>
</div>

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`params`
</td>
<td>
The `Tensor` from which to gather values. Must be at least rank
`axis + 1`.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
The index `Tensor`.  Must be one of the following types: `int32`,
`int64`. Must be in range `[0, params.shape[axis])`.
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
Deprecated, does nothing.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`. The
`axis` in `params` to gather `indices` from. Must be greater than or equal
to `batch_dims`.  Defaults to the first non-batch dimension. Supports
negative indexes.
</td>
</tr><tr>
<td>
`batch_dims`
</td>
<td>
An `integer`.  The number of batch dimensions.  Must be less
than or equal to `rank(indices)`.
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
A `Tensor`. Has the same type as `params`.
</td>
</tr>

</table>

