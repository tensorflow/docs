description: Options used for manipulating TFRecord files.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.TFRecordOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_compression_type_string"/>
<meta itemprop="property" content="compression_type_map"/>
</div>

# tf.io.TFRecordOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/tf_record.py#L43-L149">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Options used for manipulating TFRecord files.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.TFRecordOptions`, `tf.compat.v1.python_io.TFRecordOptions`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.TFRecordOptions(
    compression_type=None, flush_mode=None, input_buffer_size=None,
    output_buffer_size=None, window_bits=None, compression_level=None,
    compression_method=None, mem_level=None, compression_strategy=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`compression_type`
</td>
<td>
`"GZIP"`, `"ZLIB"`, or `""` (no compression).
</td>
</tr><tr>
<td>
`flush_mode`
</td>
<td>
flush mode or `None`, Default: Z_NO_FLUSH.
</td>
</tr><tr>
<td>
`input_buffer_size`
</td>
<td>
int or `None`.
</td>
</tr><tr>
<td>
`output_buffer_size`
</td>
<td>
int or `None`.
</td>
</tr><tr>
<td>
`window_bits`
</td>
<td>
int or `None`.
</td>
</tr><tr>
<td>
`compression_level`
</td>
<td>
0 to 9, or `None`.
</td>
</tr><tr>
<td>
`compression_method`
</td>
<td>
compression method or `None`.
</td>
</tr><tr>
<td>
`mem_level`
</td>
<td>
1 to 9, or `None`.
</td>
</tr><tr>
<td>
`compression_strategy`
</td>
<td>
strategy or `None`. Default: Z_DEFAULT_STRATEGY.
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
If compression_type is invalid.
</td>
</tr>
</table>



## Methods

<h3 id="get_compression_type_string"><code>get_compression_type_string</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/tf_record.py#L101-L125">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>get_compression_type_string(
    options
)
</code></pre>

Convert various option types to a unified string.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`options`
</td>
<td>
`TFRecordOption`, `TFRecordCompressionType`, or string.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Compression type as string (e.g. `'ZLIB'`, `'GZIP'`, or `''`).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If compression_type is invalid.
</td>
</tr>
</table>





## Class Variables

* `compression_type_map` <a id="compression_type_map"></a>
