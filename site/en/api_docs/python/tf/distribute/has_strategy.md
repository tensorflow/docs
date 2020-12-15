description: Return if there is a current non-default <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.has_strategy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.distribute.has_strategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribution_strategy_context.py#L200-L213">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return if there is a current non-default <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.has_strategy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.has_strategy()
</code></pre>



<!-- Placeholder for "Used in" -->

```
assert not tf.distribute.has_strategy()
with strategy.scope():
  assert tf.distribute.has_strategy()
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
True if inside a `with strategy.scope():`.
</td>
</tr>

</table>

