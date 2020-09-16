description: Information on how to save this Variable as a slice.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.Variable.SaveSliceInfo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="to_proto"/>
</div>

# tf.Variable.SaveSliceInfo

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/variables.py#L1257-L1336">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Information on how to save this Variable as a slice.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.Variable.SaveSliceInfo`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.Variable.SaveSliceInfo(
    full_name=None, full_shape=None, var_offset=None, var_shape=None,
    save_slice_info_def=None, import_scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Provides internal support for saving variables as slices of a larger
variable.  This API is not public and is subject to change.

#### Available properties:



* full_name
* full_shape
* var_offset
* var_shape

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`full_name`
</td>
<td>
Name of the full variable of which this `Variable` is a
slice.
</td>
</tr><tr>
<td>
`full_shape`
</td>
<td>
Shape of the full variable, as a list of int.
</td>
</tr><tr>
<td>
`var_offset`
</td>
<td>
Offset of this `Variable` into the full variable, as a list
of int.
</td>
</tr><tr>
<td>
`var_shape`
</td>
<td>
Shape of this `Variable`, as a list of int.
</td>
</tr><tr>
<td>
`save_slice_info_def`
</td>
<td>
`SaveSliceInfoDef` protocol buffer. If not `None`,
recreates the SaveSliceInfo object its contents. `save_slice_info_def`
and other arguments are mutually exclusive.
</td>
</tr><tr>
<td>
`import_scope`
</td>
<td>
Optional `string`. Name scope to add. Only used when
initializing from protocol buffer.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`spec`
</td>
<td>
Computes the spec string used for saving.
</td>
</tr>
</table>



## Methods

<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/variables.py#L1314-L1336">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_proto(
    export_scope=None
)
</code></pre>

Returns a SaveSliceInfoDef() proto.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_scope`
</td>
<td>
Optional `string`. Name scope to remove.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `SaveSliceInfoDef` protocol buffer, or None if the `Variable` is not
in the specified name scope.
</td>
</tr>

</table>





