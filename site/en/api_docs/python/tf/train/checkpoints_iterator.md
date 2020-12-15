description: Continuously yield new checkpoint files as they appear.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.checkpoints_iterator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.train.checkpoints_iterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/checkpoint_utils.py#L138-L201">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Continuously yield new checkpoint files as they appear.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.checkpoints_iterator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.train.checkpoints_iterator(
    checkpoint_dir, min_interval_secs=0, timeout=None, timeout_fn=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The iterator only checks for new checkpoints when control flow has been
reverted to it. This means it can miss checkpoints if your code takes longer
to run between iterations than `min_interval_secs` or the interval at which
new checkpoints are written.

The `timeout` argument is the maximum number of seconds to block waiting for
a new checkpoint.  It is used in combination with the `timeout_fn` as
follows:

* If the timeout expires and no `timeout_fn` was specified, the iterator
  stops yielding.
* If a `timeout_fn` was specified, that function is called and if it returns
  a true boolean value the iterator stops yielding.
* If the function returns a false boolean value then the iterator resumes the
  wait for new checkpoints.  At this point the timeout logic applies again.

This behavior gives control to callers on what to do if checkpoints do not
come fast enough or stop being generated.  For example, if callers have a way
to detect that the training has stopped and know that no new checkpoints
will be generated, they can provide a `timeout_fn` that returns `True` when
the training has stopped.  If they know that the training is still going on
they return `False` instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
The directory in which checkpoints are saved.
</td>
</tr><tr>
<td>
`min_interval_secs`
</td>
<td>
The minimum number of seconds between yielding
checkpoints.
</td>
</tr><tr>
<td>
`timeout`
</td>
<td>
The maximum number of seconds to wait between checkpoints. If left
as `None`, then the process will wait indefinitely.
</td>
</tr><tr>
<td>
`timeout_fn`
</td>
<td>
Optional function to call after a timeout.  If the function
returns True, then it means that no new checkpoints will be generated and
the iterator will exit.  The function is called with no arguments.
</td>
</tr>
</table>



#### Yields:

String paths to latest checkpoint files as they arrive.
