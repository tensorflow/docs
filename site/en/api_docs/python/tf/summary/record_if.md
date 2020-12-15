description: Sets summary recording on or off per the provided boolean value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.record_if" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.record_if

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L124-L145">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets summary recording on or off per the provided boolean value.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>tf.summary.record_if(
    condition
)
</code></pre>



<!-- Placeholder for "Used in" -->

The provided value can be a python boolean, a scalar boolean Tensor, or
or a callable providing such a value; if a callable is passed it will be
invoked on-demand to determine whether summary writing will occur.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`condition`
</td>
<td>
can be True, False, a bool Tensor, or a callable providing such.
</td>
</tr>
</table>



#### Yields:

Returns a context manager that sets this value on enter and restores the
previous value on exit.
