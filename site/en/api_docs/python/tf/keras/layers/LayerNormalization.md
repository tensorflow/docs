description: Layer normalization layer (Ba et al., 2016).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.LayerNormalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.LayerNormalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/normalization.py#L957-L1212">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer normalization layer (Ba et al., 2016).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.LayerNormalization`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.LayerNormalization(
    axis=-1, epsilon=0.001, center=(True), scale=(True), beta_initializer='zeros',
    gamma_initializer='ones', beta_regularizer=None, gamma_regularizer=None,
    beta_constraint=None, gamma_constraint=None, trainable=(True), name=None,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Normalize the activations of the previous layer for each given example in a
batch independently, rather than across a batch like Batch Normalization.
i.e. applies a transformation that maintains the mean activation within each
example close to 0 and the activation standard deviation close to 1.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Integer or List/Tuple. The axis that should be normalized
(typically the features axis).
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
Small float added to variance to avoid dividing by zero.
</td>
</tr><tr>
<td>
`center`
</td>
<td>
If True, add offset of `beta` to normalized tensor.
If False, `beta` is ignored.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
If True, multiply by `gamma`.
If False, `gamma` is not used.
When the next layer is linear (also e.g. <a href="../../../tf/nn/relu.md"><code>nn.relu</code></a>),
this can be disabled since the scaling
will be done by the next layer.
</td>
</tr><tr>
<td>
`beta_initializer`
</td>
<td>
Initializer for the beta weight.
</td>
</tr><tr>
<td>
`gamma_initializer`
</td>
<td>
Initializer for the gamma weight.
</td>
</tr><tr>
<td>
`beta_regularizer`
</td>
<td>
Optional regularizer for the beta weight.
</td>
</tr><tr>
<td>
`gamma_regularizer`
</td>
<td>
Optional regularizer for the gamma weight.
</td>
</tr><tr>
<td>
`beta_constraint`
</td>
<td>
Optional constraint for the beta weight.
</td>
</tr><tr>
<td>
`gamma_constraint`
</td>
<td>
Optional constraint for the gamma weight.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` the variables will be marked as trainable.
</td>
</tr>
</table>



#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.



#### References:

- [Layer Normalization](https://arxiv.org/abs/1607.06450)


