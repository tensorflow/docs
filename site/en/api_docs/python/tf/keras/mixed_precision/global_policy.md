description: Returns the global dtype policy.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.global_policy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.mixed_precision.global_policy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L420-L451">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the global dtype policy.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.mixed_precision.experimental.global_policy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.global_policy()
</code></pre>



<!-- Placeholder for "Used in" -->

The global policy is the default <a href="../../../tf/keras/mixed_precision/Policy.md"><code>tf.keras.mixed_precision.Policy</code></a> used for
layers, if no policy is passed to the layer constructor. If no policy has been
set with <a href="../../../tf/keras/mixed_precision/set_global_policy.md"><code>keras.mixed_precision.set_global_policy</code></a>, this will return a policy
constructed from <a href="../../../tf/keras/backend/floatx.md"><code>tf.keras.backend.floatx()</code></a> (floatx defaults to float32).

```
>>> tf.keras.mixed_precision.global_policy()
<Policy "float32">
>>> tf.keras.layers.Dense(10).dtype_policy  # Defaults to the global policy
<Policy "float32">
```

If TensorFlow 2 behavior has been disabled with
<a href="../../../tf/compat/v1/disable_v2_behavior.md"><code>tf.compat.v1.disable_v2_behavior()</code></a>, this will instead return a special
"_infer" policy which infers the dtype from the dtype of the first input the
first time the layer is called. This behavior matches the behavior that
existed in TensorFlow 1.

See <a href="../../../tf/keras/mixed_precision/Policy.md"><code>tf.keras.mixed_precision.Policy</code></a> for more information on policies.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The global Policy.
</td>
</tr>

</table>

