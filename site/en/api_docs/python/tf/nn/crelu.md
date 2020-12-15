description: Computes Concatenated ReLU.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.crelu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.crelu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L3442-L3445">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes Concatenated ReLU.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.crelu(
    features, axis=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Concatenates a ReLU which selects only the positive part of the activation
with a ReLU which selects only the *negative* part of the activation.
Note that as a result this non-linearity doubles the depth of the activations.
Source: [Understanding and Improving Convolutional Neural Networks via
Concatenated Rectified Linear Units. W. Shang, et
al.](https://arxiv.org/abs/1603.05201)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
`int16`, or `int8`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The axis that the output values are concatenated along. Default is -1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same type as `features`.
</td>
</tr>

</table>



#### References:

Understanding and Improving Convolutional Neural Networks via Concatenated
Rectified Linear Units:
  [Shang et al., 2016](http://proceedings.mlr.press/v48/shang16)
  ([pdf](http://proceedings.mlr.press/v48/shang16.pdf))
