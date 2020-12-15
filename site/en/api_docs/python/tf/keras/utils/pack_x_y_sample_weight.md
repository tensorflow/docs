description: Packs user-provided data into a tuple.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.pack_x_y_sample_weight" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.pack_x_y_sample_weight

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/data_adapter.py#L1474-L1513">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Packs user-provided data into a tuple.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.pack_x_y_sample_weight(
    x, y=None, sample_weight=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a convenience utility for packing data into the tuple formats
that <a href="../../../tf/keras/Model.md#fit"><code>Model.fit</code></a> uses.

#### Standalone usage:



```
>>> x = tf.ones((10, 1))
>>> data = tf.keras.utils.pack_x_y_sample_weight(x)
>>> isinstance(data, tf.Tensor)
True
>>> y = tf.ones((10, 1))
>>> data = tf.keras.utils.pack_x_y_sample_weight(x, y)
>>> isinstance(data, tuple)
True
>>> x, y = data
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
Features to pass to `Model`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Ground-truth targets to pass to `Model`.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Sample weight for each element.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tuple in the format used in <a href="../../../tf/keras/Model.md#fit"><code>Model.fit</code></a>.
</td>
</tr>

</table>

