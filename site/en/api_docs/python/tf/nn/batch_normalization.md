description: Batch normalization.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.batch_normalization" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.batch_normalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/nn_impl.py#L1474-L1542">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batch normalization.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.batch_normalization`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.batch_normalization(
    x, mean, variance, offset, scale, variance_epsilon, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Normalizes a tensor by `mean` and `variance`, and applies (optionally) a
`scale` \\(\gamma\\) to it, as well as an `offset` \\(\beta\\):

\\(\frac{\gamma(x-\mu)}{\sigma}+\beta\\)

`mean`, `variance`, `offset` and `scale` are all expected to be of one of two
shapes:

  * In all generality, they can have the same number of dimensions as the
    input `x`, with identical sizes as `x` for the dimensions that are not
    normalized over (the 'depth' dimension(s)), and dimension 1 for the
    others which are being normalized over.
    `mean` and `variance` in this case would typically be the outputs of
    <a href="../../tf/nn/moments.md"><code>tf.nn.moments(..., keepdims=True)</code></a> during training, or running averages
    thereof during inference.
  * In the common case where the 'depth' dimension is the last dimension in
    the input tensor `x`, they may be one dimensional tensors of the same
    size as the 'depth' dimension.
    This is the case for example for the common `[batch, depth]` layout of
    fully-connected layers, and `[batch, height, width, depth]` for
    convolutions.
    `mean` and `variance` in this case would typically be the outputs of
    <a href="../../tf/nn/moments.md"><code>tf.nn.moments(..., keepdims=False)</code></a> during training, or running averages
    thereof during inference.

See equation 11 in Algorithm 2 of source:
[Batch Normalization: Accelerating Deep Network Training by
Reducing Internal Covariate Shift; S. Ioffe, C. Szegedy]
(http://arxiv.org/abs/1502.03167).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Input `Tensor` of arbitrary dimensionality.
</td>
</tr><tr>
<td>
`mean`
</td>
<td>
A mean `Tensor`.
</td>
</tr><tr>
<td>
`variance`
</td>
<td>
A variance `Tensor`.
</td>
</tr><tr>
<td>
`offset`
</td>
<td>
An offset `Tensor`, often denoted \\(\beta\\) in equations, or
None. If present, will be added to the normalized tensor.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
A scale `Tensor`, often denoted \\(\gamma\\) in equations, or
`None`. If present, the scale is applied to the normalized tensor.
</td>
</tr><tr>
<td>
`variance_epsilon`
</td>
<td>
A small float number to avoid dividing by 0.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
the normalized, scaled, offset tensor.
</td>
</tr>

</table>



#### References:

Batch Normalization - Accelerating Deep Network Training by Reducing
Internal Covariate Shift:
  [Ioffe et al., 2015](http://arxiv.org/abs/1502.03167)
  ([pdf](http://proceedings.mlr.press/v37/ioffe15.pdf))
