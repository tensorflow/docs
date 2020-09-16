description: Retrieves a Keras loss as a function/Loss class instance.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.get" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.get

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/losses.py#L1857-L1902">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Retrieves a Keras loss as a `function`/`Loss` class instance.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.losses.get`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.get`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.get(
    identifier
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `identifier` may be the string name of a loss function or `Loss` class.

```
>>> loss = tf.keras.losses.get("categorical_crossentropy")
>>> type(loss)
<class 'function'>
>>> loss = tf.keras.losses.get("CategoricalCrossentropy")
>>> type(loss)
<class '...tensorflow.python.keras.losses.CategoricalCrossentropy'>
```

You can also specify `config` of the loss to this function by passing dict
containing `class_name` and `config` as an identifier. Also note that the
`class_name` must map to a `Loss` class

```
>>> identifier = {"class_name": "CategoricalCrossentropy",
...               "config": {"from_logits": True}}
>>> loss = tf.keras.losses.get(identifier)
>>> type(loss)
<class '...tensorflow.python.keras.losses.CategoricalCrossentropy'>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`identifier`
</td>
<td>
A loss identifier. One of None or string name of a loss
function/class or loss configuration dictionary or a loss function or a
loss class instance
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras loss as a `function`/ `Loss` class instance.
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
If `identifier` cannot be interpreted.
</td>
</tr>
</table>

