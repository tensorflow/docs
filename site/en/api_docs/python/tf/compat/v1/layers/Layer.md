description: Base layer class.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.Layer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.compat.v1.layers.Layer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/legacy_tf_layers/base.py#L158-L582">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base layer class.

Inherits From: [`Layer`](../../../../tf/keras/layers/Layer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.Layer(
    trainable=(True), name=None, dtype=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It is considered legacy, and we recommend the use of <a href="../../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a>
instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`trainable`
</td>
<td>
Boolean, whether the layer's variables should be trainable.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String name of the layer.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Default dtype of the layer's weights (default of `None` means use the
type of the first input).
</td>
</tr>
</table>


Read-only properties:
  name: The name of the layer (string).
  dtype: Default dtype of the layer's weights (default of `None` means use the
    type of the first input).
  trainable_variables: List of trainable variables.
  non_trainable_variables: List of non-trainable variables.
  variables: List of all variables of this layer, trainable and
    non-trainable.
  updates: List of update ops of this layer.
  losses: List of losses added by this layer.
  trainable_weights: List of variables to be included in backprop.
  non_trainable_weights: List of variables that should not be
    included in backprop.
  weights: The concatenation of the lists trainable_weights and
    non_trainable_weights (in this order).

#### Mutable properties:


* <b>`trainable`</b>: Whether the layer should be trained (boolean).
* <b>`input_spec`</b>: Optional (list of) `InputSpec` object(s) specifying the
  constraints on inputs that can be accepted by the layer.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>

</td>
</tr><tr>
<td>
`scope_name`
</td>
<td>

</td>
</tr>
</table>



