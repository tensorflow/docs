description: Rectified Linear Unit activation function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.ReLU" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.ReLU

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/advanced_activations.py#L348-L433">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Rectified Linear Unit activation function.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.ReLU`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.ReLU(
    max_value=None, negative_slope=0, threshold=0, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

With default values, it returns element-wise `max(x, 0)`.

Otherwise, it follows:

```
  f(x) = max_value if x >= max_value
  f(x) = x if threshold <= x < max_value
  f(x) = negative_slope * (x - threshold) otherwise
```

#### Usage:



```
>>> layer = tf.keras.layers.ReLU()
>>> output = layer([-3.0, -1.0, 0.0, 2.0])
>>> list(output.numpy())
[0.0, 0.0, 0.0, 2.0]
>>> layer = tf.keras.layers.ReLU(max_value=1.0)
>>> output = layer([-3.0, -1.0, 0.0, 2.0])
>>> list(output.numpy())
[0.0, 0.0, 0.0, 1.0]
>>> layer = tf.keras.layers.ReLU(negative_slope=1.0)
>>> output = layer([-3.0, -1.0, 0.0, 2.0])
>>> list(output.numpy())
[-3.0, -1.0, 0.0, 2.0]
>>> layer = tf.keras.layers.ReLU(threshold=1.5)
>>> output = layer([-3.0, -1.0, 1.0, 2.0])
>>> list(output.numpy())
[0.0, 0.0, 0.0, 2.0]
```

#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the batch axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as the input.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`max_value`
</td>
<td>
Float >= 0. Maximum activation value. Default to None, which
means unlimited.
</td>
</tr><tr>
<td>
`negative_slope`
</td>
<td>
Float >= 0. Negative slope coefficient. Default to 0.
</td>
</tr><tr>
<td>
`threshold`
</td>
<td>
Float. Threshold value for thresholded activation. Default to 0.
</td>
</tr>
</table>



