description: Parametric Rectified Linear Unit.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.PReLU" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.PReLU

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/advanced_activations.py#L87-L177">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Parametric Rectified Linear Unit.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.PReLU`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.PReLU(
    alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None,
    shared_axes=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### It follows:



```
  f(x) = alpha * x for x < 0
  f(x) = x for x >= 0
```

where `alpha` is a learned array with the same shape as x.

#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as the input.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`alpha_initializer`
</td>
<td>
Initializer function for the weights.
</td>
</tr><tr>
<td>
`alpha_regularizer`
</td>
<td>
Regularizer for the weights.
</td>
</tr><tr>
<td>
`alpha_constraint`
</td>
<td>
Constraint for the weights.
</td>
</tr><tr>
<td>
`shared_axes`
</td>
<td>
The axes along which to share learnable
parameters for the activation function.
For example, if the incoming feature maps
are from a 2D convolution
with output shape `(batch, height, width, channels)`,
and you wish to share parameters across space
so that each filter only has one set of parameters,
set `shared_axes=[1, 2]`.
</td>
</tr>
</table>



