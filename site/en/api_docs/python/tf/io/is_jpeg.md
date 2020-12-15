description: Convenience function to check if the 'contents' encodes a JPEG image.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.is_jpeg" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.is_jpeg

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L2838-L2855">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convenience function to check if the 'contents' encodes a JPEG image.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.image.is_jpeg`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.is_jpeg`, `tf.compat.v1.io.is_jpeg`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.is_jpeg(
    contents, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`contents`
</td>
<td>
0-D `string`. The encoded image bytes.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar boolean tensor indicating if 'contents' may be a JPEG image.
is_jpeg is susceptible to false positives.
</td>
</tr>

</table>

