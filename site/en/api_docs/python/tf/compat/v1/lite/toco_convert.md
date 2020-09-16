description: Convert a model using TOCO. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.lite.toco_convert" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.lite.toco_convert

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/lite/python/convert.py#L500-L527">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convert a model using TOCO. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.lite.toco_convert(
    input_data, input_tensors, output_tensors, *args, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `lite.TFLiteConverter` instead.

Typically this function is used to convert from TensorFlow GraphDef to TFLite.
Conversion can be customized by providing arguments that are forwarded to
`build_toco_convert_protos` (see documentation for details). This function has
been deprecated. Please use `lite.TFLiteConverter` instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_data`
</td>
<td>
Input data (i.e. often `sess.graph_def`),
</td>
</tr><tr>
<td>
`input_tensors`
</td>
<td>
List of input tensors. Type and shape are computed using
`foo.shape` and `foo.dtype`.
</td>
</tr><tr>
<td>
`output_tensors`
</td>
<td>
List of output tensors (only .name is used from this).
</td>
</tr><tr>
<td>
`*args`
</td>
<td>
See `build_toco_convert_protos`,
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
See `build_toco_convert_protos`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The converted data. For example if TFLite was the destination, then
this will be a tflite flatbuffer in a bytes array.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
Defined in `build_toco_convert_protos`.
</td>
</tr>

</table>

