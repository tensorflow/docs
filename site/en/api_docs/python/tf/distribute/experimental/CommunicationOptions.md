description: Options for cross device communications like All-reduce.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.CommunicationOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.distribute.experimental.CommunicationOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/collective_util.py#L55-L118">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Options for cross device communications like All-reduce.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.experimental.CommunicationOptions`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.CommunicationOptions(
    bytes_per_pack=0, timeout_seconds=None,
    implementation=tf.distribute.experimental.CollectiveCommunication.AUTO
)
</code></pre>



<!-- Placeholder for "Used in" -->

This can be passed to methods like
`tf.distribute.get_replica_context().all_reduce()` to optimize collective
operation performance. Note that these are only hints, which may or may not
change the actual behavior. Some options only apply to certain strategy and
are ignored by others.

One common optimization is to break gradients all-reduce into multiple packs
so that weight updates can overlap with gradient all-reduce.

#### Examples:



```python
options = tf.distribute.experimental.CommunicationOptions(
    bytes_per_pack=50 * 1024 * 1024,
    timeout_seconds=120,
    implementation=tf.distribute.experimental.CommunicationImplementation.NCCL
)
grads = tf.distribute.get_replica_context().all_reduce(
    'sum', grads, options=options)
optimizer.apply_gradients(zip(grads, vars),
    experimental_aggregate_gradients=False)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`bytes_per_pack`
</td>
<td>
a non-negative integer. Breaks collective operations into
packs of certain size. If it's zero, the value is determined
automatically. This only applies to all-reduce with
`MultiWorkerMirroredStrategy` currently.
</td>
</tr><tr>
<td>
`timeout_seconds`
</td>
<td>
a float or None, timeout in seconds. If not None, the
collective raises <a href="../../../tf/errors/DeadlineExceededError.md"><code>tf.errors.DeadlineExceededError</code></a> if it takes longer
than this timeout. Zero disables timeout. This can be useful when
debugging hanging issues.  This should only be used for debugging since
it creates a new thread for each collective, i.e. an overhead of
`timeout_seconds * num_collectives_per_second` more threads. This only
works for <a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>.
</td>
</tr><tr>
<td>
`implementation`
</td>
<td>
a
<a href="../../../tf/distribute/experimental/CommunicationImplementation.md"><code>tf.distribute.experimental.CommunicationImplementation</code></a>. This is a hint
on the preferred communication implementation. Possible values include
`AUTO`, `RING`, and `NCCL`. NCCL is generally more performant for GPU,
but doesn't work for CPU. This only works for
<a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>.
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
When arguments have invalid value.
</td>
</tr>
</table>



