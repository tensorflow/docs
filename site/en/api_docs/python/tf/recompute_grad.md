description: An eager-compatible version of recompute_grad.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.recompute_grad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.recompute_grad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/custom_gradient.py#L461-L530">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An eager-compatible version of recompute_grad.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.recompute_grad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.recompute_grad(
    f
)
</code></pre>



<!-- Placeholder for "Used in" -->

For f(*args, **kwargs), this supports gradients with respect to args or
kwargs, but kwargs are currently only supported in eager-mode.
Note that for keras layer and model objects, this is handled automatically.

Warning: If `f` was originally a tf.keras Model or Layer object, `g` will not
be able to access the member variables of that object, because `g` returns
through the wrapper function `inner`.  When recomputing gradients through
objects that inherit from keras, we suggest keeping a reference to the
underlying object around for the purpose of accessing these variables.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`f`
</td>
<td>
function `f(*x)` that returns a `Tensor` or sequence of `Tensor` outputs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A function `g` that wraps `f`, but which recomputes `f` on the backwards
pass of a gradient call.
</td>
</tr>

</table>

