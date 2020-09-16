description: Reduce learning rate when a metric has stopped improving.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.callbacks.ReduceLROnPlateau" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="in_cooldown"/>
<meta itemprop="property" content="set_model"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.keras.callbacks.ReduceLROnPlateau

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/callbacks.py#L2155-L2274">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reduce learning rate when a metric has stopped improving.

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.callbacks.ReduceLROnPlateau`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss', factor=0.1, patience=10, verbose=0, mode='auto',
    min_delta=0.0001, cooldown=0, min_lr=0, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Models often benefit from reducing the learning rate by a factor
of 2-10 once learning stagnates. This callback monitors a
quantity and if no improvement is seen for a 'patience' number
of epochs, the learning rate is reduced.

#### Example:



```python
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.001)
model.fit(X_train, Y_train, callbacks=[reduce_lr])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`monitor`
</td>
<td>
quantity to be monitored.
</td>
</tr><tr>
<td>
`factor`
</td>
<td>
factor by which the learning rate will be reduced. new_lr = lr *
factor
</td>
</tr><tr>
<td>
`patience`
</td>
<td>
number of epochs with no improvement after which learning rate
will be reduced.
</td>
</tr><tr>
<td>
`verbose`
</td>
<td>
int. 0: quiet, 1: update messages.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
one of {auto, min, max}. In `min` mode, lr will be reduced when the
quantity monitored has stopped decreasing; in `max` mode it will be
reduced when the quantity monitored has stopped increasing; in `auto`
mode, the direction is automatically inferred from the name of the
monitored quantity.
</td>
</tr><tr>
<td>
`min_delta`
</td>
<td>
threshold for measuring the new optimum, to only focus on
significant changes.
</td>
</tr><tr>
<td>
`cooldown`
</td>
<td>
number of epochs to wait before resuming normal operation after
lr has been reduced.
</td>
</tr><tr>
<td>
`min_lr`
</td>
<td>
lower bound on the learning rate.
</td>
</tr>
</table>



## Methods

<h3 id="in_cooldown"><code>in_cooldown</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/callbacks.py#L2273-L2274">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>in_cooldown()
</code></pre>




<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/callbacks.py#L548-L549">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_model(
    model
)
</code></pre>




<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/callbacks.py#L545-L546">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    params
)
</code></pre>






