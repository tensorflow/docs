description: Sets the global Policy.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.experimental.set_policy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.mixed_precision.experimental.set_policy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/mixed_precision/experimental/policy.py#L534-L559">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the global Policy.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.mixed_precision.experimental.set_policy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.experimental.set_policy(
    policy
)
</code></pre>



<!-- Placeholder for "Used in" -->

The global policy is the default policy used for layers, if no policy is
passed to the layer constructor. If no global policy is set, layers will
instead default to a Policy constructed from <a href="../../../../tf/keras/backend/floatx.md"><code>tf.keras.backend.floatx()</code></a> in
TensorFlow 2. In TensorFlow 1, layers default to an "infer" policy.

See <a href="../../../../tf/keras/mixed_precision/experimental/Policy.md"><code>keras.mixed_precision.experimental.Policy</code></a> for more information.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`policy`
</td>
<td>
A Policy, or a string that will be converted to a Policy..
</td>
</tr>
</table>

