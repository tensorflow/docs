description: Enable visualizations for TensorBoard.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.callbacks.TensorBoard" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="set_model"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.keras.callbacks.TensorBoard

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks.py#L1823-L2266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enable visualizations for TensorBoard.

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.callbacks.TensorBoard(
    log_dir='logs', histogram_freq=0, write_graph=(True), write_images=(False),
    update_freq='epoch', profile_batch=2, embeddings_freq=0,
    embeddings_metadata=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

TensorBoard is a visualization tool provided with TensorFlow.

This callback logs events for TensorBoard, including:

* Metrics summary plots
* Training graph visualization
* Activation histograms
* Sampled profiling

If you have installed TensorFlow with pip, you should be able
to launch TensorBoard from the command line:

```
tensorboard --logdir=path_to_your_logs
```

You can find more information about TensorBoard
[here](https://www.tensorflow.org/get_started/summaries_and_tensorboard).

Example (Basic):

```python
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")
model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])
# run the tensorboard command to view the visualizations.
```

Example (Profile):

```python
# profile a single batch, e.g. the 5th batch.
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='./logs',
                                                      profile_batch=5)
model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])
# Now run the tensorboard command to view the visualizations (profile plugin).

# profile a range of batches, e.g. from 10 to 20.
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='./logs',
                                                      profile_batch='10,20')
model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])
# Now run the tensorboard command to view the visualizations (profile plugin).
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`log_dir`
</td>
<td>
the path of the directory where to save the log files to be
parsed by TensorBoard.
</td>
</tr><tr>
<td>
`histogram_freq`
</td>
<td>
frequency (in epochs) at which to compute activation and
weight histograms for the layers of the model. If set to 0, histograms
won't be computed. Validation data (or split) must be specified for
histogram visualizations.
</td>
</tr><tr>
<td>
`write_graph`
</td>
<td>
whether to visualize the graph in TensorBoard. The log file
can become quite large when write_graph is set to True.
</td>
</tr><tr>
<td>
`write_images`
</td>
<td>
whether to write model weights to visualize as image in
TensorBoard.
</td>
</tr><tr>
<td>
`update_freq`
</td>
<td>
`'batch'` or `'epoch'` or integer. When using `'batch'`,
writes the losses and metrics to TensorBoard after each batch. The same
applies for `'epoch'`. If using an integer, let's say `1000`, the
callback will write the metrics and losses to TensorBoard every 1000
batches. Note that writing too frequently to TensorBoard can slow down
your training.
</td>
</tr><tr>
<td>
`profile_batch`
</td>
<td>
Profile the batch(es) to sample compute characteristics.
profile_batch must be a non-negative integer or a tuple of integers.
A pair of positive integers signify a range of batches to profile.
By default, it will profile the second batch. Set profile_batch=0
to disable profiling.
</td>
</tr><tr>
<td>
`embeddings_freq`
</td>
<td>
frequency (in epochs) at which embedding layers will be
visualized. If set to 0, embeddings won't be visualized.
</td>
</tr><tr>
<td>
`embeddings_metadata`
</td>
<td>
a dictionary which maps layer name to a file name in
which metadata for this embedding layer is saved. See the
[details](
https://www.tensorflow.org/how_tos/embedding_viz/#metadata_optional)
about metadata files format. In case if the same metadata file is
used for all embedding layers, string can be passed.
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
If histogram_freq is set and no validation data is provided.
</td>
</tr>
</table>



## Methods

<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks.py#L1966-L1982">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_model(
    model
)
</code></pre>

Sets Keras model and writes graph if specified.


<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks.py#L616-L617">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    params
)
</code></pre>






