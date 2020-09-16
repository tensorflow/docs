description: Batch normalization.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.batch_norm_with_global_normalization" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.batch_norm_with_global_normalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_impl.py#L1602-L1648">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batch normalization.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.batch_norm_with_global_normalization(
    input, mean, variance, beta, gamma, variance_epsilon, scale_after_normalization,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op is deprecated. See <a href="../../tf/nn/batch_normalization.md"><code>tf.nn.batch_normalization</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A 4D input Tensor.
</td>
</tr><tr>
<td>
`mean`
</td>
<td>
A 1D mean Tensor with size matching the last dimension of t.
This is the first output from tf.nn.moments,
or a saved moving average thereof.
</td>
</tr><tr>
<td>
`variance`
</td>
<td>
A 1D variance Tensor with size matching the last dimension of t.
This is the second output from tf.nn.moments,
or a saved moving average thereof.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
A 1D beta Tensor with size matching the last dimension of t.
An offset to be added to the normalized tensor.
</td>
</tr><tr>
<td>
`gamma`
</td>
<td>
A 1D gamma Tensor with size matching the last dimension of t.
If "scale_after_normalization" is true, this tensor will be multiplied
with the normalized tensor.
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
`scale_after_normalization`
</td>
<td>
A bool indicating whether the resulted tensor
needs to be multiplied with gamma.
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
A batch-normalized `t`.
</td>
</tr>

</table>



#### References:

Batch Normalization - Accelerating Deep Network Training by Reducing Internal Covariate Shift:
  [Ioffe et al., 2015](http://proceedings.mlr.press/v37/ioffe15.html)
  ([pdf](http://proceedings.mlr.press/v37/ioffe15.pdf))
