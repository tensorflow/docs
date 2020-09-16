description: Set a <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> as current without with strategy.scope().

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental_set_strategy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.distribute.experimental_set_strategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribution_strategy_context.py#L220-L266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Set a <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> as current without `with strategy.scope()`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.experimental_set_strategy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental_set_strategy(
    strategy
)
</code></pre>



<!-- Placeholder for "Used in" -->

```
tf.distribute.experimental_set_strategy(strategy1)
f()
tf.distribute.experimental_set_strategy(strategy2)
g()
tf.distribute.experimental_set_strategy(None)
h()
```

is equivalent to:

```
with strategy1.scope():
  f()
with strategy2.scope():
  g()
h()
```

In general, you should use the `with strategy.scope():` API, but this
alternative may be convenient in notebooks where you would have to put
each cell in a `with strategy.scope():` block.

Note: This should only be called outside of any TensorFlow scope to
avoid improper nesting.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`strategy`
</td>
<td>
A <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object or None.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If called inside a `with strategy.scope():`.
</td>
</tr>
</table>

