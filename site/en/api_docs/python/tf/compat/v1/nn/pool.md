description: Performs an N-D pooling operation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.pool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_ops.py#L1109-L1280">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Performs an N-D pooling operation.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.pool(
    input, window_shape, pooling_type, padding, dilation_rate=None, strides=None,
    name=None, data_format=None, dilations=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

In the case that `data_format` does not start with "NC", computes for
    0 <= b < batch_size,
    0 <= x[i] < output_spatial_shape[i],
    0 <= c < num_channels:

```
  output[b, x[0], ..., x[N-1], c] =
    REDUCE_{z[0], ..., z[N-1]}
      input[b,
            x[0] * strides[0] - pad_before[0] + dilation_rate[0]*z[0],
            ...
            x[N-1]*strides[N-1] - pad_before[N-1] + dilation_rate[N-1]*z[N-1],
            c],
```

where the reduction function REDUCE depends on the value of `pooling_type`,
and pad_before is defined based on the value of `padding` as described in
the "returns" section of <a href="../../../../tf/nn/convolution.md"><code>tf.nn.convolution</code></a> for details.
The reduction never includes out-of-bounds positions.

In the case that `data_format` starts with `"NC"`, the `input` and output are
simply transposed as follows:

```
  pool(input, data_format, **kwargs) =
    tf.transpose(pool(tf.transpose(input, [0] + range(2,N+2) + [1]),
                      **kwargs),
                 [0, N+1] + range(1, N+1))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
Tensor of rank N+2, of shape
`[batch_size] + input_spatial_shape + [num_channels]` if data_format does
not start with "NC" (default), or
`[batch_size, num_channels] + input_spatial_shape` if data_format starts
with "NC".  Pooling happens over the spatial dimensions only.
</td>
</tr><tr>
<td>
`window_shape`
</td>
<td>
Sequence of N ints >= 1.
</td>
</tr><tr>
<td>
`pooling_type`
</td>
<td>
Specifies pooling operation, must be "AVG" or "MAX".
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
The padding algorithm, must be "SAME" or "VALID".
See the "returns" section of <a href="../../../../tf/nn/convolution.md"><code>tf.nn.convolution</code></a> for details.
</td>
</tr><tr>
<td>
`dilation_rate`
</td>
<td>
Optional.  Dilation rate.  List of N ints >= 1.
Defaults to [1]*N.  If any value of dilation_rate is > 1, then all values
of strides must be 1.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
Optional.  Sequence of N ints >= 1.  Defaults to [1]*N.
If any value of strides is > 1, then all values of dilation_rate must be
1.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional. Name of the op.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
A string or None.  Specifies whether the channel dimension of
the `input` and output is the last dimension (default, or if `data_format`
does not start with "NC"), or the second dimension (if `data_format`
starts with "NC").  For N=1, the valid values are "NWC" (default) and
"NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
For N=3, the valid values are "NDHWC" (default) and "NCDHW".
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
Alias for dilation_rate
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tensor of rank N+2, of shape
[batch_size] + output_spatial_shape + [num_channels]

if data_format is None or does not start with "NC", or

[batch_size, num_channels] + output_spatial_shape

if data_format starts with "NC",
where `output_spatial_shape` depends on the value of padding:

If padding = "SAME":
output_spatial_shape[i] = ceil(input_spatial_shape[i] / strides[i])

If padding = "VALID":
output_spatial_shape[i] =
ceil((input_spatial_shape[i] - (window_shape[i] - 1) * dilation_rate[i])
/ strides[i]).
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
if arguments are invalid.
</td>
</tr>
</table>

