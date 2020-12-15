description: Compute the exponential moving average of a value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.moving_average_update" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.moving_average_update

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L1728-L1768">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute the exponential moving average of a value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.moving_average_update`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.moving_average_update(
    x, value, momentum
)
</code></pre>



<!-- Placeholder for "Used in" -->

The moving average 'x' is updated with 'value' following:

```
x = x * momentum + value * (1 - momentum)
```

#### For example:



```
>>> x = tf.Variable(0.0)
>>> momentum=0.9
>>> moving_average_update(x, value = 2.0, momentum=momentum).numpy()
>>> x.numpy()
0.2
```

The result will be biased towards the initial value of the variable.

If the variable was initialized to zero, you can divide by
`1 - momentum ** num_updates` to debias it (Section 3 of
[Kingma et al., 2015](https://arxiv.org/abs/1412.6980)):

```
>>> num_updates = 1.0
>>> x_zdb = x/(1 - momentum**num_updates)
>>> x_zdb.numpy()
2.0
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
A Variable, the moving average.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A tensor with the same shape as `x`, the new value to be
averaged in.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
The moving average momentum.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The updated variable.
</td>
</tr>

</table>

