description: Sets the learning phase to a fixed value. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.set_learning_phase" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.set_learning_phase

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L398-L426">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the learning phase to a fixed value. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.set_learning_phase`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.set_learning_phase(
    value
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2020-10-11.
Instructions for updating:
Simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.

The backend learning phase affects any code that calls
<a href="../../../tf/keras/backend/learning_phase.md"><code>backend.learning_phase()</code></a>
In particular, all Keras built-in layers use the learning phase as the default
for the `training` arg to <a href="../../../tf/keras/layers/Layer.md#__call__"><code>Layer.__call__</code></a>.

User-written layers and models can achieve the same behavior with code that
looks like:

```python
  def call(self, inputs, training=None):
    if training is None:
      training = backend.learning_phase()
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
Learning phase value, either 0 or 1 (integers).
0 = test, 1 = train
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
if `value` is neither `0` nor `1`.
</td>
</tr>
</table>

