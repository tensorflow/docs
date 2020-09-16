description: Layer that reshapes inputs into the given shape.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Reshape" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Reshape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/core.py#L432-L536">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer that reshapes inputs into the given shape.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Reshape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Reshape(
    target_shape, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Input shape:

Arbitrary, although all dimensions in the input shape must be known/fixed.
Use the keyword argument `input_shape` (tuple of integers, does not include
the samples/batch size axis) when using this layer as the first layer
in a model.



#### Output shape:

`(batch_size,) + target_shape`



#### Example:



```
>>> # as first layer in a Sequential model
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Reshape((3, 4), input_shape=(12,)))
>>> # model.output_shape == (None, 3, 4), `None` is the batch size.
>>> model.output_shape
(None, 3, 4)
```

```
>>> # as intermediate layer in a Sequential model
>>> model.add(tf.keras.layers.Reshape((6, 2)))
>>> model.output_shape
(None, 6, 2)
```

```
>>> # also supports shape inference using `-1` as dimension
>>> model.add(tf.keras.layers.Reshape((-1, 2, 2)))
>>> model.output_shape
(None, None, 2, 2)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`target_shape`
</td>
<td>
Target shape. Tuple of integers, does not include the
samples dimension (batch size).
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Any additional layer keyword arguments.
</td>
</tr>
</table>



