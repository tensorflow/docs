description: Hints for collective operations like AllReduce.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.CollectiveHints" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.distribute.experimental.CollectiveHints

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/collective_util.py#L166-L230">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Hints for collective operations like AllReduce.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.experimental.CollectiveHints`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.CollectiveHints(
    bytes_per_pack=0, timeout_seconds=None
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



- bytes_per_pack

```python
hints = tf.distribute.experimental.CollectiveHints(
    bytes_per_pack=50 * 1024 * 1024)
grads = tf.distribute.get_replica_context().all_reduce(
    'sum', grads, experimental_hints=hints)
optimizer.apply_gradients(zip(grads, vars),
    experimental_aggregate_gradients=False)
```

- timeout_seconds

```python
strategy = tf.distribute.MirroredStrategy()
hints = tf.distribute.experimental.CollectiveHints(
    timeout_seconds=120)
try:
  strategy.reduce("sum", v, axis=None, experimental_hints=hints)
except tf.errors.DeadlineExceededError:
  do_something()
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
than this timeout. This can be useful when debugging hanging issues.
This should only be used for debugging since it creates a new thread for
each collective, i.e. an overhead of `timeout_seconds *
num_collectives_per_second` more threads.  This only works for
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



