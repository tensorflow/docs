description: Set if JIT compilation is enabled.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.optimizer.set_jit" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.optimizer.set_jit

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/config.py#L125-L136">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Set if JIT compilation is enabled.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.optimizer.set_jit`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.optimizer.set_jit(
    enabled
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that optimizations are only applied to code that is compiled into a
graph. In eager mode, which is the TF2 API default, that means only code that
is defined under a tf.function decorator.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`enabled`
</td>
<td>
Whether to enable JIT compilation.
</td>
</tr>
</table>

