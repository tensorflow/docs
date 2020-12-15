description: Softmax activation function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Softmax" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Softmax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/advanced_activations.py#L281-L344">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Softmax activation function.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Softmax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Softmax(
    axis=-1, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example without mask:



```
>>> inp = np.asarray([1., 2., 1.])
>>> layer = tf.keras.layers.Softmax()
>>> layer(inp).numpy()
array([0.21194157, 0.5761169 , 0.21194157], dtype=float32)
>>> mask = np.asarray([True, False, True], dtype=bool)
>>> layer(inp, mask).numpy()
array([0.5, 0. , 0.5], dtype=float32)
```

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
`axis`
</td>
<td>
Integer, or list of Integers, axis along which the softmax
normalization is applied.
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: The inputs, or logits to the softmax layer.
* <b>`mask`</b>: A boolean mask of the same shape as `inputs`. Defaults to `None`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
softmaxed output with the same shape as `inputs`.
</td>
</tr>

</table>



