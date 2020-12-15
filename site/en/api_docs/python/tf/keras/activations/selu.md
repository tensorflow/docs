description: Scaled Exponential Linear Unit (SELU).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.selu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.selu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/activations.py#L136-L187">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Scaled Exponential Linear Unit (SELU).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.selu`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.selu(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->

The Scaled Exponential Linear Unit (SELU) activation function is defined as:

- `if x > 0: return scale * x`
- `if x < 0: return scale * alpha * (exp(x) - 1)`

where `alpha` and `scale` are pre-defined constants
(`alpha=1.67326324` and `scale=1.05070098`).

Basically, the SELU activation function multiplies `scale` (> 1) with the
output of the <a href="../../../tf/keras/activations/elu.md"><code>tf.keras.activations.elu</code></a> function to ensure a slope larger
than one for positive inputs.

The values of `alpha` and `scale` are
chosen so that the mean and variance of the inputs are preserved
between two consecutive layers as long as the weights are initialized
correctly (see <a href="../../../tf/keras/initializers/LecunNormal.md"><code>tf.keras.initializers.LecunNormal</code></a> initializer)
and the number of input units is "large enough"
(see reference paper for more information).

#### Example Usage:



```
>>> num_classes = 10  # 10-class problem
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Dense(64, kernel_initializer='lecun_normal',
...                                 activation='selu'))
>>> model.add(tf.keras.layers.Dense(32, kernel_initializer='lecun_normal',
...                                 activation='selu'))
>>> model.add(tf.keras.layers.Dense(16, kernel_initializer='lecun_normal',
...                                 activation='selu'))
>>> model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A tensor or variable to compute the activation function for.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The scaled exponential unit activation: `scale * elu(x, alpha)`.
</td>
</tr>

</table>



#### Notes:

- To be used together with the
  <a href="../../../tf/keras/initializers/LecunNormal.md"><code>tf.keras.initializers.LecunNormal</code></a> initializer.
- To be used together with the dropout variant
  <a href="../../../tf/keras/layers/AlphaDropout.md"><code>tf.keras.layers.AlphaDropout</code></a> (not regular dropout).



#### References:

- [Klambauer et al., 2017](https://arxiv.org/abs/1706.02515)
