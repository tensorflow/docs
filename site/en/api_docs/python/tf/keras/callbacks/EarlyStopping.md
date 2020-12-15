description: Stop training when a monitored metric has stopped improving.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.callbacks.EarlyStopping" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_monitor_value"/>
<meta itemprop="property" content="set_model"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.keras.callbacks.EarlyStopping

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L1660-L1791">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Stop training when a monitored metric has stopped improving.

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.callbacks.EarlyStopping`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', min_delta=0, patience=0, verbose=0, mode='auto',
    baseline=None, restore_best_weights=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Assuming the goal of a training is to minimize the loss. With this, the
metric to be monitored would be `'loss'`, and mode would be `'min'`. A
`model.fit()` training loop will check at end of every epoch whether
the loss is no longer decreasing, considering the `min_delta` and
`patience` if applicable. Once it's found no longer decreasing,
`model.stop_training` is marked True and the training terminates.

The quantity to be monitored needs to be available in `logs` dict.
To make it so, pass the loss or metrics at `model.compile()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`monitor`
</td>
<td>
Quantity to be monitored.
</td>
</tr><tr>
<td>
`min_delta`
</td>
<td>
Minimum change in the monitored quantity
to qualify as an improvement, i.e. an absolute
change of less than min_delta, will count as no
improvement.
</td>
</tr><tr>
<td>
`patience`
</td>
<td>
Number of epochs with no improvement
after which training will be stopped.
</td>
</tr><tr>
<td>
`verbose`
</td>
<td>
verbosity mode.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
One of `{"auto", "min", "max"}`. In `min` mode,
training will stop when the quantity
monitored has stopped decreasing; in `"max"`
mode it will stop when the quantity
monitored has stopped increasing; in `"auto"`
mode, the direction is automatically inferred
from the name of the monitored quantity.
</td>
</tr><tr>
<td>
`baseline`
</td>
<td>
Baseline value for the monitored quantity.
Training will stop if the model doesn't show improvement over the
baseline.
</td>
</tr><tr>
<td>
`restore_best_weights`
</td>
<td>
Whether to restore model weights from
the epoch with the best value of the monitored quantity.
If False, the model weights obtained at the last step of
training are used.
</td>
</tr>
</table>



#### Example:



```
>>> callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
>>> # This callback will stop the training when there is no improvement in
>>> # the validation loss for three consecutive epochs.
>>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
>>> model.compile(tf.keras.optimizers.SGD(), loss='mse')
>>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5),
...                     epochs=10, batch_size=1, callbacks=[callback],
...                     verbose=0)
>>> len(history.history['loss'])  # Only 4 epochs are run.
4
```

## Methods

<h3 id="get_monitor_value"><code>get_monitor_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L1784-L1791">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_monitor_value(
    logs
)
</code></pre>




<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L633-L634">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_model(
    model
)
</code></pre>




<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L630-L631">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    params
)
</code></pre>






