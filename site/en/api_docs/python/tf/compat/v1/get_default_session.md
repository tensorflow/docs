description: Returns the default session for the current thread.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.get_default_session" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.get_default_session

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L5457-L5472">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the default session for the current thread.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.get_default_session()
</code></pre>



<!-- Placeholder for "Used in" -->

The returned `Session` will be the innermost session on which a
`Session` or `Session.as_default()` context has been entered.

NOTE: The default session is a property of the current thread. If you
create a new thread, and wish to use the default session in that
thread, you must explicitly add a `with sess.as_default():` in that
thread's function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The default `Session` being used in the current thread.
</td>
</tr>

</table>

