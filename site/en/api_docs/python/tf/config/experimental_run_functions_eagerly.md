description: Enables / disables eager execution of <a href="../../tf/function.md"><code>tf.function</code></a>s. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental_run_functions_eagerly" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental_run_functions_eagerly

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/def_function.py#L316-L337">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enables / disables eager execution of <a href="../../tf/function.md"><code>tf.function</code></a>s. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental_run_functions_eagerly`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental_run_functions_eagerly(
    run_eagerly
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../tf/config/run_functions_eagerly.md"><code>tf.config.run_functions_eagerly</code></a> instead of the experimental version.

Calling <a href="../../tf/config/experimental_run_functions_eagerly.md"><code>tf.config.experimental_run_functions_eagerly(True)</code></a> will make all
invocations of <a href="../../tf/function.md"><code>tf.function</code></a> run eagerly instead of running as a traced graph
function.

See <a href="../../tf/config/run_functions_eagerly.md"><code>tf.config.run_functions_eagerly</code></a> for an example.

Note: This flag has no effect on functions passed into tf.data transformations
as arguments. tf.data functions are never executed eagerly and are always
executed as a compiled Tensorflow Graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`run_eagerly`
</td>
<td>
Boolean. Whether to run functions eagerly.
</td>
</tr>
</table>

