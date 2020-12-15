description: Just your regular densely-connected NN layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Dense" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Dense

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/core.py#L1081-L1247">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Just your regular densely-connected NN layer.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Dense`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Dense(
    units, activation=None, use_bias=(True), kernel_initializer='glorot_uniform',
    bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None,
    activity_regularizer=None, kernel_constraint=None, bias_constraint=None,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

`Dense` implements the operation:
`output = activation(dot(input, kernel) + bias)`
where `activation` is the element-wise activation function
passed as the `activation` argument, `kernel` is a weights matrix
created by the layer, and `bias` is a bias vector created by the layer
(only applicable if `use_bias` is `True`).

Note: If the input to the layer has a rank greater than 2, then `Dense`
computes the dot product between the `inputs` and the `kernel` along the
last axis of the `inputs` and axis 1 of the `kernel` (using <a href="../../../tf/tensordot.md"><code>tf.tensordot</code></a>).
For example, if input has dimensions `(batch_size, d0, d1)`,
then we create a `kernel` with shape `(d1, units)`, and the `kernel` operates
along axis 2 of the `input`, on every sub-tensor of shape `(1, 1, d1)`
(there are `batch_size * d0` such sub-tensors).
The output in this case will have shape `(batch_size, d0, units)`.

Besides, layer attributes cannot be modified after the layer has been called
once (except the `trainable` attribute).

#### Example:



```
>>> # Create a `Sequential` model and add a Dense layer as the first layer.
>>> model = tf.keras.models.Sequential()
>>> model.add(tf.keras.Input(shape=(16,)))
>>> model.add(tf.keras.layers.Dense(32, activation='relu'))
>>> # Now the model will take as input arrays of shape (None, 16)
>>> # and output arrays of shape (None, 32).
>>> # Note that after the first layer, you don't need to specify
>>> # the size of the input anymore:
>>> model.add(tf.keras.layers.Dense(32))
>>> model.output_shape
(None, 32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`units`
</td>
<td>
Positive integer, dimensionality of the output space.
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function to use.
If you don't specify anything, no activation is applied
(ie. "linear" activation: `a(x) = x`).
</td>
</tr><tr>
<td>
`use_bias`
</td>
<td>
Boolean, whether the layer uses a bias vector.
</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>
Initializer for the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
Initializer for the bias vector.
</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>
Regularizer function applied to
the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Regularizer function applied to the bias vector.
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Regularizer function applied to
the output of the layer (its "activation").
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to
the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Constraint function applied to the bias vector.
</td>
</tr>
</table>



#### Input shape:

N-D tensor with shape: `(batch_size, ..., input_dim)`.
The most common situation would be
a 2D input with shape `(batch_size, input_dim)`.



#### Output shape:

N-D tensor with shape: `(batch_size, ..., units)`.
For instance, for a 2D input with shape `(batch_size, input_dim)`,
the output would have shape `(batch_size, units)`.


