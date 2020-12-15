description: Disable the eager/graph unified numerics checking mechanism.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.disable_check_numerics" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.disable_check_numerics

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/debug/lib/check_numerics_callback.py#L447-L471">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Disable the eager/graph unified numerics checking mechanism.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.disable_check_numerics`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.debugging.disable_check_numerics()
</code></pre>



<!-- Placeholder for "Used in" -->

This method can be used after a call to <a href="../../tf/debugging/enable_check_numerics.md"><code>tf.debugging.enable_check_numerics()</code></a>
to disable the numerics-checking mechanism that catches infinity and NaN
values output by ops executed eagerly or in tf.function-compiled graphs.

This method is idempotent. Calling it multiple times has the same effect
as calling it once.

This method takes effect only on the thread in which it is called.