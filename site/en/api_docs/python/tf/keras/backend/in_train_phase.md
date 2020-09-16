description: Selects x in train phase, and alt otherwise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.in_train_phase" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.in_train_phase

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L4331-L4373">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Selects `x` in train phase, and `alt` otherwise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.in_train_phase`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.in_train_phase(
    x, alt, training=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that `alt` should have the *same shape* as `x`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
What to return in train phase
(tensor or callable that returns a tensor).
</td>
</tr><tr>
<td>
`alt`
</td>
<td>
What to return otherwise
(tensor or callable that returns a tensor).
</td>
</tr><tr>
<td>
`training`
</td>
<td>
Optional scalar tensor
(or Python boolean, or Python integer)
specifying the learning phase.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Either `x` or `alt` based on the `training` flag.
the `training` flag defaults to `K.learning_phase()`.
</td>
</tr>

</table>

