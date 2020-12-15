description: Returns a tensor whose value represents the total loss.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.get_total_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.get_total_loss

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/losses/util.py#L237-L266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a tensor whose value represents the total loss.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.get_total_loss(
    add_regularization_losses=(True), name='total_loss', scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

In particular, this adds any losses you have added with `tf.add_loss()` to
any regularization losses that have been added by regularization parameters
on layers constructors e.g. `tf.layers`. Be very sure to use this if you
are constructing a loss_op manually. Otherwise regularization arguments
on `tf.layers` methods will not function.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`add_regularization_losses`
</td>
<td>
A boolean indicating whether or not to use the
regularization losses in the sum.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the returned tensor.
</td>
</tr><tr>
<td>
`scope`
</td>
<td>
An optional scope name for filtering the losses to return. Note that
this filters the losses added with `tf.add_loss()` as well as the
regularization losses to that scope.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` whose value represents the total loss.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `losses` is not iterable.
</td>
</tr>
</table>

