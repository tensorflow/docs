description: Sets the global dtype policy.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.set_global_policy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.mixed_precision.set_global_policy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L470-L526">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the global dtype policy.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.mixed_precision.experimental.set_policy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.set_global_policy(
    policy
)
</code></pre>



<!-- Placeholder for "Used in" -->

The global policy is the default <a href="../../../tf/keras/mixed_precision/Policy.md"><code>tf.keras.mixed_precision.Policy</code></a> used for
layers, if no policy is passed to the layer constructor.

```
>>> tf.keras.mixed_precision.set_global_policy('mixed_float16')
>>> tf.keras.mixed_precision.global_policy()
<Policy "mixed_float16">
>>> tf.keras.layers.Dense(10).dtype_policy
<Policy "mixed_float16">
>>> # Global policy is not used if a policy is directly passed to constructor
>>> tf.keras.layers.Dense(10, dtype='float64').dtype_policy
<Policy "float64">
>>> tf.keras.mixed_precision.set_global_policy('float32')
```

If no global policy is set, layers will instead default to a Policy
constructed from <a href="../../../tf/keras/backend/floatx.md"><code>tf.keras.backend.floatx()</code></a>.

To use mixed precision, the global policy should be set to `'mixed_float16'`
or `'mixed_bfloat16'`, so that every layer uses a 16-bit compute dtype and
float32 variable dtype by default.

Only floating point policies can be set as the global policy, such as
`'float32'` and `'mixed_float16'`. Non-floating point policies such as
`'int32'` and `'complex64'` cannot be set as the global policy because most
layers do not support such policies.

See <a href="../../../tf/keras/mixed_precision/Policy.md"><code>tf.keras.mixed_precision.Policy</code></a> for more information.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`policy`
</td>
<td>
A Policy, or a string that will be converted to a Policy. Can also
be None, in which case the global policy will be constructed from
<a href="../../../tf/keras/backend/floatx.md"><code>tf.keras.backend.floatx()</code></a>
</td>
</tr>
</table>

