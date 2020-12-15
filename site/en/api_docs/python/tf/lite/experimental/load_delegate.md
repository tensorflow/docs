description: Returns loaded Delegate object.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lite.experimental.load_delegate" />
<meta itemprop="path" content="Stable" />
</div>

# tf.lite.experimental.load_delegate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/lite/python/interpreter.py#L132-L156">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns loaded Delegate object.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lite.experimental.load_delegate`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lite.experimental.load_delegate(
    library, options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`library`
</td>
<td>
Name of shared library containing the
[TfLiteDelegate](https://www.tensorflow.org/lite/performance/delegates).
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Dictionary of options that are required to load the delegate. All
keys and values in the dictionary should be convertible to str. Consult
the documentation of the specific delegate for required and legal options.
(default None)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Delegate object.
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
Delegate failed to load.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If delegate loading is used on unsupported platform.
</td>
</tr>
</table>

