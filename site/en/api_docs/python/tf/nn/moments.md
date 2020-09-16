description: Calculates the mean and variance of x.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.moments" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.moments

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_impl.py#L1217-L1250">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculates the mean and variance of `x`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.moments(
    x, axes, shift=None, keepdims=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The mean and variance are calculated by aggregating the contents of `x`
across `axes`.  If `x` is 1-D and `axes = [0]` this is just the mean
and variance of a vector.

Note: shift is currently not used; the true mean is computed and used.

When using these moments for batch normalization (see
<a href="../../tf/nn/batch_normalization.md"><code>tf.nn.batch_normalization</code></a>):

 * for so-called "global normalization", used with convolutional filters with
   shape `[batch, height, width, depth]`, pass `axes=[0, 1, 2]`.
 * for simple batch normalization pass `axes=[0]` (batch only).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
Array of ints.  Axes along which to compute mean and
variance.
</td>
</tr><tr>
<td>
`shift`
</td>
<td>
Not used in the current implementation.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
produce moments with the same dimensionality as the input.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name used to scope the operations that compute the moments.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Two `Tensor` objects: `mean` and `variance`.
</td>
</tr>

</table>

