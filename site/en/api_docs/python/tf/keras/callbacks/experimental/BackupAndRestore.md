description: Callback to back up and restore the training state.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.callbacks.experimental.BackupAndRestore" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="set_model"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.keras.callbacks.experimental.BackupAndRestore

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks.py#L1446-L1555">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Callback to back up and restore the training state.

Inherits From: [`Callback`](../../../../tf/keras/callbacks/Callback.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.callbacks.experimental.BackupAndRestore(
    backup_dir
)
</code></pre>



<!-- Placeholder for "Used in" -->

`BackupAndRestore` callback is intended to recover from interruptions that
happened in the middle of a model.fit execution by backing up the
training states in a temporary checkpoint file (based on TF CheckpointManager)
at the end of each epoch. If training restarted before completion, the
training state and model are restored to the most recently saved state at the
beginning of a new model.fit() run.
Note that user is responsible to bring jobs back up.
This callback is important for the backup and restore mechanism for fault
tolerance purpose. And the model to be restored from an previous checkpoint is
expected to be the same as the one used to back up. If user changes arguments
passed to compile or fit, the checkpoint saved for fault tolerance can become
invalid.

#### Note:


1. This callback is not compatible with disabling eager execution.
2. A checkpoint is saved at the end of each epoch, when restoring we'll redo
any partial work from an unfinished epoch in which the training got restarted
(so the work done before a interruption doesn't affect the final model state).
3. This works for both single worker and multi-worker mode, only
MirroredStrategy and MultiWorkerMirroredStrategy are supported for now.

#### Example:



```
>>> class InterruptingCallback(tf.keras.callbacks.Callback):
...   def on_epoch_begin(self, epoch, logs=None):
...     if epoch == 4:
...       raise RuntimeError('Interrupting!')
>>> callback = tf.keras.callbacks.experimental.BackupAndRestore(
... backup_dir="/tmp")
>>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
>>> model.compile(tf.keras.optimizers.SGD(), loss='mse')
>>> try:
...   model.fit(np.arange(100).reshape(5, 20), np.zeros(5), epochs=10,
...             batch_size=1, callbacks=[callback, InterruptingCallback()],
...             verbose=0)
... except:
...   pass
>>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5), epochs=10,
...             batch_size=1, callbacks=[callback], verbose=0)
>>> # Only 6 more epochs are run, since first trainning got interrupted at
>>> # zero-indexed epoch 4, second training will continue from 4 to 9.
>>> len(history.history['loss'])
6
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`backup_dir`
</td>
<td>
String, path to save the model file. This is the directory in
which the system stores temporary files to recover the model from jobs
terminated unexpectedly. The directory cannot be reused elsewhere to
store other checkpoints, e.g. by BackupAndRestore callback of another
training, or by another callback (ModelCheckpoint) of the same training.
</td>
</tr>
</table>



## Methods

<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks.py#L1525-L1526">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_model(
    model
)
</code></pre>




<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/callbacks.py#L616-L617">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    params
)
</code></pre>






