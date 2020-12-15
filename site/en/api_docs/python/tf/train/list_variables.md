description: Lists the checkpoint keys and shapes of variables in a checkpoint.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.list_variables" />
<meta itemprop="path" content="Stable" />
</div>

# tf.train.list_variables

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/checkpoint_utils.py#L88-L118">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Lists the checkpoint keys and shapes of variables in a checkpoint.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.list_variables`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.train.list_variables(
    ckpt_dir_or_file
)
</code></pre>



<!-- Placeholder for "Used in" -->

Checkpoint keys are paths in a checkpoint graph.

#### Example usage:


```python

import tensorflow as tf
import os
ckpt_directory = "/tmp/training_checkpoints/ckpt"
ckpt = tf.train.Checkpoint(optimizer=optimizer, model=model)
manager = tf.train.CheckpointManager(ckpt, ckpt_directory, max_to_keep=3)
train_and_checkpoint(model, manager)
tf.train.list_variables(manager.latest_checkpoint)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ckpt_dir_or_file`
</td>
<td>
Directory with checkpoints file or path to checkpoint.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
List of tuples `(key, shape)`.
</td>
</tr>

</table>

