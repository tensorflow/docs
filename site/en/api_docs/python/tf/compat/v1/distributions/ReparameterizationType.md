description: Instances of this class represent how sampling is reparameterized.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distributions.ReparameterizationType" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.distributions.ReparameterizationType

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/distributions/distribution.py#L216-L259">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instances of this class represent how sampling is reparameterized.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.distributions.ReparameterizationType(
    rep_type
)
</code></pre>



<!-- Placeholder for "Used in" -->

Two static instances exist in the distributions library, signifying
one of two possible properties for samples from a distribution:

`FULLY_REPARAMETERIZED`: Samples from the distribution are fully
  reparameterized, and straight-through gradients are supported.

`NOT_REPARAMETERIZED`: Samples from the distribution are not fully
  reparameterized, and straight-through gradients are either partially
  unsupported or are not supported at all. In this case, for purposes of
  e.g. RL or variational inference, it is generally safest to wrap the
  sample results in a `stop_gradients` call and use policy
  gradients / surrogate loss instead.

## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/distributions/distribution.py#L247-L259">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Determine if this `ReparameterizationType` is equal to another.

Since ReparameterizationType instances are constant static global
instances, equality checks if two instances' id() values are equal.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`other`
</td>
<td>
Object to compare against.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`self is other`.
</td>
</tr>

</table>





