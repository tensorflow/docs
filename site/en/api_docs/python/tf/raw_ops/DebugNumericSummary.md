description: Debug Numeric Summary Op.

robots: noindex

# tf.raw_ops.DebugNumericSummary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Debug Numeric Summary Op.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DebugNumericSummary`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DebugNumericSummary(
    input, device_name='', tensor_name='', debug_urls=[], lower_bound=float('-inf'),
    upper_bound=float('inf'), mute_if_healthy=(False), gated_grpc=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Provide a basic summary of numeric value types, range and distribution.

output: A double tensor of shape [14 + nDimensions], where nDimensions is the
  number of dimensions of the tensor's shape. The elements of output are:
  [0]: is initialized (1.0) or not (0.0).
  [1]: total number of elements
  [2]: NaN element count
  [3]: generalized -inf count: elements <= lower_bound. lower_bound is -inf by
    default.
  [4]: negative element count (excluding -inf), if lower_bound is the default
    -inf. Otherwise, this is the count of elements > lower_bound and < 0.
  [5]: zero element count
  [6]: positive element count (excluding +inf), if upper_bound is the default
    +inf. Otherwise, this is the count of elements < upper_bound and > 0.
  [7]: generalized +inf count, elements >= upper_bound. upper_bound is +inf by
    default.
Output elements [1:8] are all zero, if the tensor is uninitialized.
  [8]: minimum of all non-inf and non-NaN elements.
       If uninitialized or no such element exists: +inf.
  [9]: maximum of all non-inf and non-NaN elements.
       If uninitialized or no such element exists: -inf.
  [10]: mean of all non-inf and non-NaN elements.
        If uninitialized or no such element exists: NaN.
  [11]: variance of all non-inf and non-NaN elements.
        If uninitialized or no such element exists: NaN.
  [12]: Data type of the tensor encoded as an enum integer. See the DataType
        proto for more details.
  [13]: Number of dimensions of the tensor (ndims).
  [14+]: Sizes of the dimensions.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Input tensor, non-Reference type.
</td>
</tr><tr>
<td>
`device_name`
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`tensor_name`
</td>
<td>
An optional `string`. Defaults to `""`.
Name of the input tensor.
</td>
</tr><tr>
<td>
`debug_urls`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
List of URLs to debug targets, e.g.,
file:///foo/tfdbg_dump, grpc:://localhost:11011.
</td>
</tr><tr>
<td>
`lower_bound`
</td>
<td>
An optional `float`. Defaults to `float('-inf')`.
(float) The lower bound <= which values will be included in the
generalized -inf count. Default: -inf.
</td>
</tr><tr>
<td>
`upper_bound`
</td>
<td>
An optional `float`. Defaults to `float('inf')`.
(float) The upper bound >= which values will be included in the
generalized +inf count. Default: +inf.
</td>
</tr><tr>
<td>
`mute_if_healthy`
</td>
<td>
An optional `bool`. Defaults to `False`.
(bool) Do not send data to the debug URLs unless at least one
of elements [2], [3] and [7] (i.e., the nan count and the generalized -inf and
inf counts) is non-zero.
</td>
</tr><tr>
<td>
`gated_grpc`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether this op will be gated. If any of the debug_urls of this
debug node is of the grpc:// scheme, when the value of this attribute is set
to True, the data will not actually be sent via the grpc stream unless this
debug op has been enabled at the debug_url. If all of the debug_urls of this
debug node are of the grpc:// scheme and the debug op is enabled at none of
them, the output will be an empty Tensor.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `float64`.
</td>
</tr>

</table>

