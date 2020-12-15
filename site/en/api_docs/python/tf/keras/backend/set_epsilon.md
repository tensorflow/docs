description: Sets the value of the fuzz factor used in numeric expressions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.set_epsilon" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.set_epsilon

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/backend_config.py#L48-L64">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the value of the fuzz factor used in numeric expressions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.set_epsilon`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.set_epsilon(
    value
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
float. New value of epsilon.
</td>
</tr>
</table>



#### Example:


>>> tf.keras.backend.epsilon()
1e-07
>>> tf.keras.backend.set_epsilon(1e-5)
>>> tf.keras.backend.epsilon()
1e-05
 >>> tf.keras.backend.set_epsilon(1e-7)