description: Computes log Poisson loss given log_input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.log_poisson_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.log_poisson_loss

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_impl.py#L47-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes log Poisson loss given `log_input`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.log_poisson_loss`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.log_poisson_loss(
    targets, log_input, compute_full_loss=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Gives the log-likelihood loss between the prediction and the target under the
assumption that the target has a Poisson distribution.
Caveat: By default, this is not the exact loss, but the loss minus a
  constant term [log(z!)]. That has no effect for optimization, but
  does not play well with relative loss comparisons. To compute an
  approximation of the log factorial term, specify
  compute_full_loss=True to enable Stirling's Approximation.

For brevity, let `c = log(x) = log_input`, `z = targets`.  The log Poisson
loss is

      -log(exp(-x) * (x^z) / z!)
    = -log(exp(-x) * (x^z)) + log(z!)
    ~ -log(exp(-x)) - log(x^z) [+ z * log(z) - z + 0.5 * log(2 * pi * z)]
        [ Note the second term is the Stirling's Approximation for log(z!).
          It is invariant to x and does not affect optimization, though
          important for correct relative loss comparisons. It is only
          computed when compute_full_loss == True. ]
    = x - z * log(x) [+ z * log(z) - z + 0.5 * log(2 * pi * z)]
    = exp(c) - z * c [+ z * log(z) - z + 0.5 * log(2 * pi * z)]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`targets`
</td>
<td>
A `Tensor` of the same type and shape as `log_input`.
</td>
</tr><tr>
<td>
`log_input`
</td>
<td>
A `Tensor` of type `float32` or `float64`.
</td>
</tr><tr>
<td>
`compute_full_loss`
</td>
<td>
whether to compute the full loss. If false, a constant
term is dropped in favor of more efficient optimization.
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
A `Tensor` of the same shape as `log_input` with the componentwise
logistic losses.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `log_input` and `targets` do not have the same shape.
</td>
</tr>
</table>

