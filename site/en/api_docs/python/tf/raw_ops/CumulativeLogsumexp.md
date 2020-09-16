description: Compute the cumulative product of the tensor x along axis.

robots: noindex

# tf.raw_ops.CumulativeLogsumexp

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Compute the cumulative product of the tensor `x` along `axis`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CumulativeLogsumexp`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CumulativeLogsumexp(
    x, axis, exclusive=(False), reverse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

By default, this op performs an inclusive cumulative log-sum-exp,
which means that the first
element of the input is identical to the first element of the output:
```python
tf.math.cumulative_logsumexp([a, b, c])  # => [a, log(exp(a) + exp(b)), log(exp(a) + exp(b) + exp(c))]
```

By setting the `exclusive` kwarg to `True`, an exclusive cumulative log-sum-exp is
performed instead:
```python
tf.cumulative_logsumexp([a, b, c], exclusive=True)  # => [-inf, a, log(exp(a) * exp(b))]
```
Note that the neutral element of the log-sum-exp operation is `-inf`,
however, for performance reasons, the minimal value representable by the
floating point type is used instead.

By setting the `reverse` kwarg to `True`, the cumulative log-sum-exp is performed in the
opposite direction.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
A `Tensor`. Must be one of the following types: `float16`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A `Tensor` of type `int32` (default: 0). Must be in the range
`[-rank(x), rank(x))`.
</td>
</tr><tr>
<td>
`exclusive`
</td>
<td>
An optional `bool`. Defaults to `False`.
If `True`, perform exclusive cumulative log-sum-exp.
</td>
</tr><tr>
<td>
`reverse`
</td>
<td>
An optional `bool`. Defaults to `False`.
A `bool` (default: False).
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
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>

