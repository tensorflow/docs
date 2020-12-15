description: Applies an activation function to an output.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Activation" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Activation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/core.py#L407-L448">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies an activation function to an output.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Activation`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Activation(
    activation, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`activation`
</td>
<td>
Activation function, such as <a href="../../../tf/nn/relu.md"><code>tf.nn.relu</code></a>, or string name of
built-in activation function, such as "relu".
</td>
</tr>
</table>



#### Usage:



```
>>> layer = tf.keras.layers.Activation('relu')
>>> output = layer([-3.0, -1.0, 0.0, 2.0])
>>> list(output.numpy())
[0.0, 0.0, 0.0, 2.0]
>>> layer = tf.keras.layers.Activation(tf.nn.relu)
>>> output = layer([-3.0, -1.0, 0.0, 2.0])
>>> list(output.numpy())
[0.0, 0.0, 0.0, 2.0]
```

#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the batch axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.


