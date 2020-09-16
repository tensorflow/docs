description: Applies Dropout to the input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.Dropout" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.compat.v1.layers.Dropout

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/layers/core.py#L191-L226">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies Dropout to the input.

Inherits From: [`Dropout`](../../../../tf/keras/layers/Dropout.md), [`Layer`](../../../../tf/compat/v1/layers/Layer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.Dropout(
    rate=0.5, noise_shape=None, seed=None, name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

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
`rate`
</td>
<td>
The dropout rate, between 0 and 1. E.g. `rate=0.1` would drop out
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
<a href="../../../../tf/compat/v1/set_random_seed.md"><code>tf.compat.v1.set_random_seed</code></a>.
for behavior.
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
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.
</td>
</tr><tr>
<td>
`scope_name`
</td>
<td>

</td>
</tr>
</table>



