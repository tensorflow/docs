description: Returns all variables that maintain their moving averages.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.moving_average_variables" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.moving_average_variables

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/variables.py#L3156-L3175">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns all variables that maintain their moving averages.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.moving_average_variables(
    scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If an `ExponentialMovingAverage` object is created and the `apply()`
method is called on a list of variables, these variables will
be added to the `GraphKeys.MOVING_AVERAGE_VARIABLES` collection.
This convenience function returns the contents of that collection.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`scope`
</td>
<td>
(Optional.) A string. If supplied, the resulting list is filtered to
include only items whose `name` attribute matches `scope` using
`re.match`. Items without a `name` attribute are never returned if a scope
is supplied. The choice of `re.match` means that a `scope` without special
tokens filters by prefix.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of Variable objects.
</td>
</tr>

</table>

