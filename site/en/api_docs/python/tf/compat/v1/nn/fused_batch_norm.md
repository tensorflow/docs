description: Batch normalization.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.fused_batch_norm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.fused_batch_norm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_impl.py#L1567-L1671">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batch normalization.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.fused_batch_norm(
    x, scale, offset, mean=None, variance=None, epsilon=0.001, data_format='NHWC',
    is_training=(True), name=None, exponential_avg_factor=1.0
)
</code></pre>



<!-- Placeholder for "Used in" -->


See Source: [Batch Normalization: Accelerating Deep Network Training by
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
Input `Tensor` of 4 or 5 dimensions.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
A `Tensor` of 1 dimension for scaling.
</td>
</tr><tr>
<td>
`offset`
</td>
<td>
A `Tensor` of 1 dimension for bias.
</td>
</tr><tr>
<td>
`mean`
</td>
<td>
A `Tensor` of 1 dimension for population mean. The shape and meaning
of this argument depends on the value of is_training and
exponential_avg_factor as follows:
is_training==False (inference):
Mean must be a `Tensor` of the same shape as scale containing the
estimated population mean computed during training.
is_training==True and exponential_avg_factor == 1.0:
Mean must be None.
is_training==True and exponential_avg_factor != 1.0:
Mean must be a `Tensor` of the same shape as scale containing the
exponential running mean.
</td>
</tr><tr>
<td>
`variance`
</td>
<td>
A `Tensor` of 1 dimension for population variance. The shape and
meaning of this argument depends on the value of is_training and
exponential_avg_factor as follows:
is_training==False (inference):
Variance must be a `Tensor` of the same shape as scale containing
the estimated population variance computed during training.
is_training==True and exponential_avg_factor == 1.0:
Variance must be None.
is_training==True and exponential_avg_factor != 1.0:
Variance must be a `Tensor` of the same shape as scale containing
the exponential running variance.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A small float number added to the variance of x.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
The data format for x. Support "NHWC" (default) or "NCHW" for
4D tenors and "NDHWC" or "NCDHW" for 5D tensors.
</td>
</tr><tr>
<td>
`is_training`
</td>
<td>
A bool value to specify if the operation is used for
training or inference.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr><tr>
<td>
`exponential_avg_factor`
</td>
<td>
A float number (usually between 0 and 1) used
for controlling the decay of the running
population average of mean and variance.
If set to 1.0, the current batch average is
returned.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`y`
</td>
<td>
A 4D or 5D Tensor for the normalized, scaled, offsetted x.
</td>
</tr><tr>
<td>
`running_mean`
</td>
<td>
A 1D Tensor for the exponential running mean of x.
The output value is (1 - exponential_avg_factor) * mean +
exponential_avg_factor * batch_mean), where batch_mean
is the mean of the current batch in x.
</td>
</tr><tr>
<td>
`running_var`
</td>
<td>
A 1D Tensor for the exponential running variance
The output value is (1 - exponential_avg_factor) * variance +
exponential_avg_factor * batch_variance), where batch_variance
is the variance of the current batch in x.
</td>
</tr>
</table>



#### References:

Batch Normalization - Accelerating Deep Network Training by Reducing
Internal Covariate Shift:
  [Ioffe et al., 2015](http://proceedings.mlr.press/v37/ioffe15.html)
  ([pdf](http://proceedings.mlr.press/v37/ioffe15.pdf))
