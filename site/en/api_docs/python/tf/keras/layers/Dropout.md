description: Applies Dropout to the input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Dropout" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Dropout

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/core.py#L144-L244">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies Dropout to the input.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Dropout`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Dropout(
    rate, noise_shape=None, seed=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The Dropout layer randomly sets input units to 0 with a frequency of `rate`
at each step during training time, which helps prevent overfitting.
Inputs not set to 0 are scaled up by 1/(1 - rate) such that the sum over
all inputs is unchanged.

Note that the Dropout layer only applies when `training` is set to True
such that no values are dropped during inference. When using `model.fit`,
`training` will be appropriately set to True automatically, and in other
contexts, you can set the kwarg explicitly to True when calling the layer.

(This is in contrast to setting `trainable=False` for a Dropout layer.
`trainable` does not affect the layer's behavior, as Dropout does
not have any variables/weights that can be frozen during training.)

```
>>> tf.random.set_seed(0)
>>> layer = tf.keras.layers.Dropout(.2, input_shape=(2,))
>>> data = np.arange(10).reshape(5, 2).astype(np.float32)
>>> print(data)
[[0. 1.]
 [2. 3.]
 [4. 5.]
 [6. 7.]
 [8. 9.]]
>>> outputs = layer(data, training=True)
>>> print(outputs)
tf.Tensor(
[[ 0.    1.25]
 [ 2.5   3.75]
 [ 5.    6.25]
 [ 7.5   8.75]
 [10.    0.  ]], shape=(5, 2), dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`rate`
</td>
<td>
Float between 0 and 1. Fraction of the input units to drop.
</td>
</tr><tr>
<td>
`noise_shape`
</td>
<td>
1D integer tensor representing the shape of the
binary dropout mask that will be multiplied with the input.
For instance, if your inputs have shape
`(batch_size, timesteps, features)` and
you want the dropout mask to be the same for all timesteps,
you can use `noise_shape=(batch_size, 1, features)`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A Python integer to use as random seed.
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: Input tensor (of any rank).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode (adding dropout) or in inference mode (doing nothing).


