description: Scope class for bfloat16 variables so that the model uses custom getter.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.bfloat16_scope" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.bfloat16_scope

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/bfloat16.py#L71-L82">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Scope class for bfloat16 variables so that the model uses custom getter.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>tf.compat.v1.tpu.bfloat16_scope(
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This enables variables to be read as bfloat16 type when using get_variable.