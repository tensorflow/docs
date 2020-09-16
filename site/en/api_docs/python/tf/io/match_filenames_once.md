description: Save the list of files matching pattern, so it is only computed once.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.match_filenames_once" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.match_filenames_once

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/input.py#L58-L78">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Save the list of files matching pattern, so it is only computed once.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.match_filenames_once`, `tf.compat.v1.train.match_filenames_once`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.match_filenames_once(
    pattern, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

NOTE: The order of the files returned is deterministic.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`pattern`
</td>
<td>
A file pattern (glob), or 1D tensor of file patterns.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operations (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A variable that is initialized to the list of files matching the pattern(s).
</td>
</tr>

</table>

