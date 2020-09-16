description: Scaled Exponential Linear Unit (SELU).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.selu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.selu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/activations.py#L101-L156">
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

The Scaled Exponential Linear Unit (SELU) activation function is:
`scale * x` if `x > 0` and `scale * alpha * (exp(x) - 1)` if `x < 0`
where `alpha` and `scale` are pre-defined constants
(`alpha = 1.67326324`
and `scale = 1.05070098`).
The SELU activation function multiplies  `scale` > 1 with the
`[elu](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras/activations/elu)`
(Exponential Linear Unit (ELU)) to ensure a slope larger than one
for positive net inputs.

The values of `alpha` and `scale` are
chosen so that the mean and variance of the inputs are preserved
between two consecutive layers as long as the weights are initialized
correctly (see [`lecun_normal` initialization]
(https://www.tensorflow.org/api_docs/python/tf/keras/initializers/lecun_normal))
and the number of inputs is "large enough"
(see references for more information).

![]https://cdn-images-1.medium.com/max/1600/1*m0e8lZU_Zrkh4ESfQkY2Pw.png
(Courtesy: Blog on Towards DataScience at
https://towardsdatascience.com/selu-make-fnns-great-again-snn-8d61526802a9)

#### Example Usage:



```
>>> n_classes = 10  #10-class problem
>>> from tensorflow.python.keras.layers import Dense
>>> model = tf.keras.Sequential()
>>> model.add(Dense(64, kernel_initializer='lecun_normal',
...                 activation='selu', input_shape=(28, 28, 1)))
>>> model.add(Dense(32, kernel_initializer='lecun_normal',
...                 activation='selu'))
>>> model.add(Dense(16, kernel_initializer='lecun_normal',
...                 activation='selu'))
>>> model.add(Dense(n_classes, activation='softmax'))
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


# Note
    - To be used together with the initialization "[lecun_normal]
    (https://www.tensorflow.org/api_docs/python/tf/keras/initializers/lecun_normal)".
    - To be used together with the dropout variant "[AlphaDropout]
    (https://www.tensorflow.org/api_docs/python/tf/keras/layers/AlphaDropout)".

#### References:

[Self-Normalizing Neural Networks (Klambauer et al, 2017)]
(https://arxiv.org/abs/1706.02515)
