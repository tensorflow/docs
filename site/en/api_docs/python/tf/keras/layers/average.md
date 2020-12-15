description: Functional interface to the <a href="../../../tf/keras/layers/Average.md"><code>tf.keras.layers.Average</code></a> layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.average" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.layers.average

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/merge.py#L817-L850">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface to the <a href="../../../tf/keras/layers/Average.md"><code>tf.keras.layers.Average</code></a> layer.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.average`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.average(
    inputs, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```
>>> x1 = np.ones((2, 2))
>>> x2 = np.zeros((2, 2))
>>> y = tf.keras.layers.Average()([x1, x2])
>>> y.numpy().tolist()
[[0.5, 0.5], [0.5, 0.5]]
```

Usage in a functional model:

```
>>> input1 = tf.keras.layers.Input(shape=(16,))
>>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1)
>>> input2 = tf.keras.layers.Input(shape=(32,))
>>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2)
>>> avg = tf.keras.layers.Average()([x1, x2])
>>> out = tf.keras.layers.Dense(4)(avg)
>>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of input tensors (at least 2).
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Standard layer keyword arguments.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor, the average of the inputs.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If there is a shape mismatch between the inputs and the shapes
cannot be broadcasted to match.
</td>
</tr>
</table>

