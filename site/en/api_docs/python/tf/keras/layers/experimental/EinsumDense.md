description: A layer that uses tf.einsum as the backing computation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.EinsumDense" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.experimental.EinsumDense

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/einsum_dense.py#L34-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A layer that uses tf.einsum as the backing computation.

Inherits From: [`Layer`](../../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.EinsumDense`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.EinsumDense(
    equation, output_shape, activation=None, bias_axes=None,
    kernel_initializer='glorot_uniform', bias_initializer='zeros',
    kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    kernel_constraint=None, bias_constraint=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer can perform einsum calculations of arbitrary dimensionality.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`equation`
</td>
<td>
An equation describing the einsum to perform. This equation must
be a valid einsum string of the form `ab,bc->ac`, `...ab,bc->...ac`, or
`ab...,bc->ac...` where 'ab', 'bc', and 'ac' can be any valid einsum axis
expression sequence.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
The expected shape of the output tensor (excluding the batch
dimension and any dimensions represented by ellipses). You can specify
None for any dimension that is unknown or can be inferred from the input
shape.
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function to use. If you don't specify anything, no
activation is applied (that is, a "linear" activation: `a(x) = x`).
</td>
</tr><tr>
<td>
`bias_axes`
</td>
<td>
A string containing the output dimension(s) to apply a bias to.
Each character in the `bias_axes` string should correspond to a character
in the output portion of the `equation` string.
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
Regularizer function applied to the `kernel` weights
matrix.
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
Regularizer function applied to the output of the
layer (its "activation")..
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to the `kernel` weights
matrix.
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



#### Examples:



**Biased dense layer with einsums**

This example shows how to instantiate a standard Keras dense layer using
einsum operations. This example is equivalent to
<a href="../../../../tf/keras/layers/Dense.md"><code>tf.keras.layers.Dense(64, use_bias=True)</code></a>.

```
>>> layer = EinsumDense("ab,bc->ac", output_shape=64, bias_axes="c")
>>> input_tensor = tf.keras.Input(shape=[32])
>>> output_tensor = layer(input_tensor)
>>> output_tensor
<... shape=(None, 64) dtype=...>
```

**Applying a dense layer to a sequence**

This example shows how to instantiate a layer that applies the same dense
operation to every element in a sequence. Here, the 'output_shape' has two
values (since there are two non-batch dimensions in the output); the first
dimension in the output_shape is `None`, because the sequence dimension `b`
has an unknown shape.

```
>>> layer = EinsumDense("abc,cd->abd",
...                     output_shape=(None, 64),
...                     bias_axes="d")
>>> input_tensor = tf.keras.Input(shape=[32, 128])
>>> output_tensor = layer(input_tensor)
>>> output_tensor
<... shape=(None, 32, 64) dtype=...>
```

**Applying a dense layer to a sequence using ellipses**

This example shows how to instantiate a layer that applies the same dense
operation to every element in a sequence, but uses the ellipsis notation
instead of specifying the batch and sequence dimensions.

Because we are using ellipsis notation and have specified only one axis, the
output_shape arg is a single value. When instantiated in this way, the layer
can handle any number of sequence dimensions - including the case where no
sequence dimension exists.

```
>>> layer = EinsumDense("...x,xy->...y", output_shape=64, bias_axes="y")
>>> input_tensor = tf.keras.Input(shape=[32, 128])
>>> output_tensor = layer(input_tensor)
>>> output_tensor
<... shape=(None, 32, 64) dtype=...>
```

