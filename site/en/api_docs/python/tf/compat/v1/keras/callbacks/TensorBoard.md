description: Enable visualizations for TensorBoard.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.callbacks.TensorBoard" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="set_model"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.compat.v1.keras.callbacks.TensorBoard

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks_v1.py#L42-L469">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enable visualizations for TensorBoard.

Inherits From: [`TensorBoard`](../../../../../tf/keras/callbacks/TensorBoard.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.callbacks.TensorBoard(
    log_dir='./logs', histogram_freq=0, batch_size=32, write_graph=(True),
    write_grads=(False), write_images=(False), embeddings_freq=0,
    embeddings_layer_names=None, embeddings_metadata=None, embeddings_data=None,
    update_freq='epoch', profile_batch=2
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

```sh
tensorboard --logdir=path_to_your_logs
```

You can find more information about TensorBoard
[here](https://www.tensorflow.org/get_started/summaries_and_tensorboard).

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
`write_grads`
</td>
<td>
whether to visualize gradient histograms in TensorBoard.
`histogram_freq` must be greater than 0.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
size of batch of inputs to feed to the network for histograms
computation.
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
`embeddings_freq`
</td>
<td>
frequency (in epochs) at which selected embedding layers
will be saved. If set to 0, embeddings won't be computed. Data to be
visualized in TensorBoard's Embedding tab must be passed as
`embeddings_data`.
</td>
</tr><tr>
<td>
`embeddings_layer_names`
</td>
<td>
a list of names of layers to keep eye on. If None
or empty list all the embedding layer will be watched.
</td>
</tr><tr>
<td>
`embeddings_metadata`
</td>
<td>
a dictionary which maps layer name to a file name in
which metadata for this embedding layer is saved.
[Here are details](
https://www.tensorflow.org/how_tos/embedding_viz/#metadata_optional)
about metadata files format. In case if the same metadata file is
used for all embedding layers, string can be passed.
</td>
</tr><tr>
<td>
`embeddings_data`
</td>
<td>
data to be embedded at layers specified in
`embeddings_layer_names`. Numpy array (if the model has a single input)
or list of Numpy arrays (if the model has multiple inputs). Learn more
about embeddings [in this guide](
https://www.tensorflow.org/programmers_guide/embedding).
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
samples. Note that writing too frequently to TensorBoard can slow down
your training.
</td>
</tr><tr>
<td>
`profile_batch`
</td>
<td>
Profile the batch to sample compute characteristics. By
default, it will profile the second batch. Set profile_batch=0 to
disable profiling.
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




#### Eager Compatibility
Using the `TensorBoard` callback will work when eager execution is enabled,
with the restriction that outputting histogram summaries of weights and
gradients is not supported. Consequently, `histogram_freq` will be ignored.



## Methods

<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks_v1.py#L234-L312">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_model(
    model
)
</code></pre>

Sets Keras model and creates summary ops.


<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks.py#L616-L617">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    params
)
</code></pre>






