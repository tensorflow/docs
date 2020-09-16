description: Functional interface to the <a href="../../../tf/keras/layers/Add.md"><code>tf.keras.layers.Add</code></a> layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.add" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.layers.add

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/merge.py#L736-L767">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface to the <a href="../../../tf/keras/layers/Add.md"><code>tf.keras.layers.Add</code></a> layer.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.add`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.add(
    inputs, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of input tensors (at least 2) with the same shape.
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
A tensor as the sum of the inputs. It has the same shape as the inputs.
</td>
</tr>

</table>



#### Examples:



```
>>> input_shape = (2, 3, 4)
>>> x1 = tf.random.normal(input_shape)
>>> x2 = tf.random.normal(input_shape)
>>> y = tf.keras.layers.add([x1, x2])
>>> print(y.shape)
(2, 3, 4)
```

Used in a functiona model:

```
>>> input1 = tf.keras.layers.Input(shape=(16,))
>>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1)
>>> input2 = tf.keras.layers.Input(shape=(32,))
>>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2)
>>> added = tf.keras.layers.add([x1, x2])
>>> out = tf.keras.layers.Dense(4)(added)
>>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)
```