description: Exponential Linear Unit.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.elu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.elu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/activations.py#L90-L137">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Exponential Linear Unit.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.elu`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.elu(
    x, alpha=1.0
)
</code></pre>



<!-- Placeholder for "Used in" -->

The exponential linear unit (ELU) with `alpha > 0` is:
`x` if `x > 0` and
`alpha * (exp(x) - 1)` if `x < 0`
The ELU hyperparameter `alpha` controls the value to which an
ELU saturates for negative net inputs. ELUs diminish the
vanishing gradient effect.

ELUs have negative values which pushes the mean of the activations
closer to zero.
Mean activations that are closer to zero enable faster learning as they
bring the gradient closer to the natural gradient.
ELUs saturate to a negative value when the argument gets smaller.
Saturation means a small derivative which decreases the variation
and the information that is propagated to the next layer.

#### Example Usage:



```
>>> import tensorflow as tf
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='elu',
...          input_shape=(28, 28, 1)))
>>> model.add(tf.keras.layers.MaxPooling2D((2, 2)))
>>> model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='elu'))
>>> model.add(tf.keras.layers.MaxPooling2D((2, 2)))
>>> model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='elu'))
```

<tensorflow.python.keras.engine.sequential.Sequential object ...>

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Input tensor.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
A scalar, slope of negative section. `alpha` controls the value to
which an ELU saturates for negative net inputs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The exponential linear unit (ELU) activation function: `x` if `x > 0` and
`alpha * (exp(x) - 1)` if `x < 0`.
</td>
</tr>

</table>



#### Reference:

[Fast and Accurate Deep Network Learning by Exponential Linear Units
(ELUs) (Clevert et al, 2016)](https://arxiv.org/abs/1511.07289)
