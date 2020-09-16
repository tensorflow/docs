description: Returns True if in a cross-replica context.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.in_cross_replica_context" />
<meta itemprop="path" content="Stable" />
</div>

# tf.distribute.in_cross_replica_context

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribution_strategy_context.py#L154-L176">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns `True` if in a cross-replica context.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.in_cross_replica_context`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.in_cross_replica_context()
</code></pre>



<!-- Placeholder for "Used in" -->

See <a href="../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context</code></a> for details.

```
assert not tf.distribute.in_cross_replica_context()
with strategy.scope():
  assert tf.distribute.in_cross_replica_context()

  def f():
    assert not tf.distribute.in_cross_replica_context()

  strategy.run(f)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
`True` if in a cross-replica context (`get_replica_context()` returns
`None`), or `False` if in a replica context (`get_replica_context()` returns
non-`None`).
</td>
</tr>

</table>

