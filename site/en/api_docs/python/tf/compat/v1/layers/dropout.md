description: Applies Dropout to the input. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.dropout" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.layers.dropout

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/legacy_tf_layers/core.py#L229-L271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies Dropout to the input. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.dropout(
    inputs, rate=0.5, noise_shape=None, seed=None, training=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use keras.layers.dropout instead.

Dropout consists in randomly setting a fraction `rate` of input units to 0
at each update during training time, which helps prevent overfitting.
The units that are kept are scaled by `1 / (1 - rate)`, so that their
sum is unchanged at training time and inference time.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
Tensor input.
</td>
</tr><tr>
<td>
`rate`
</td>
<td>
The dropout rate, between 0 and 1. E.g. "rate=0.1" would drop out
10% of input units.
</td>
</tr><tr>
<td>
`noise_shape`
</td>
<td>
1D tensor of type `int32` representing the shape of the
binary dropout mask that will be multiplied with the input.
For instance, if your inputs have shape
`(batch_size, timesteps, features)`, and you want the dropout mask
to be the same for all timesteps, you can use
`noise_shape=[batch_size, 1, features]`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A Python integer. Used to create random seeds. See
<a href="../../../../tf/compat/v1/set_random_seed.md"><code>tf.compat.v1.set_random_seed</code></a>
for behavior.
</td>
</tr><tr>
<td>
`training`
</td>
<td>
Either a Python boolean, or a TensorFlow boolean scalar tensor
(e.g. a placeholder). Whether to return the output in training mode
(apply dropout) or in inference mode (return the input untouched).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the layer (string).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor.
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
if eager execution is enabled.
</td>
</tr>
</table>

