description: Layer that adds a list of inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Add" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Add

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/merge.py#L221-L254">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer that adds a list of inputs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Add`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Add(
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It takes as input a list of tensors,
all of the same shape, and returns
a single tensor (also of the same shape).

#### Examples:



```
>>> input_shape = (2, 3, 4)
>>> x1 = tf.random.normal(input_shape)
>>> x2 = tf.random.normal(input_shape)
>>> y = tf.keras.layers.Add()([x1, x2])
>>> print(y.shape)
(2, 3, 4)
```

Used in a functional model:

```
>>> input1 = tf.keras.layers.Input(shape=(16,))
>>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1)
>>> input2 = tf.keras.layers.Input(shape=(32,))
>>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2)
>>> # equivalent to `added = tf.keras.layers.add([x1, x2])`
>>> added = tf.keras.layers.Add()([x1, x2])
>>> out = tf.keras.layers.Dense(4)(added)
>>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`**kwargs`
</td>
<td>
standard layer keyword arguments.
</td>
</tr>
</table>



