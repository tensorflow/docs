description: Shards computation for parallel execution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.shard" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.shard

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/tpu.py#L1798-L1880">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Shards `computation` for parallel execution.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.shard(
    computation, inputs=None, num_shards=1, input_shard_axes=None,
    outputs_from_all_shards=(True), output_shard_axes=None, infeed_queue=None,
    device_assignment=None, name=None, xla_options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`inputs` must be a list of Tensors or None (equivalent to an empty list), each
of which has a corresponding split axis (from `input_shard_axes`). Each input
is split into `num_shards` pieces along the corresponding axis, and
computation is applied to each shard in parallel.

Tensors are broadcast to all shards if they are lexically captured by
`computation`. e.g.,

x = tf.constant(7)
def computation():
  return x + 3
... = shard(computation, ...)


as inputs.

If `outputs_from_all_shards` is true, the outputs from all shards of
`computation` are concatenated back together along their `output_shard_axes`.
Otherwise, each output is taken from an arbitrary shard.

Inputs and outputs of the computation must be at least rank-1 Tensors.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`computation`
</td>
<td>
A Python function that builds a computation to apply to each
shard of the input.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A list of input tensors or None (equivalent to an empty list). Each
input tensor has a corresponding shard axes, given by `input_shard_axes`,
which must have size divisible by `num_shards`.
</td>
</tr><tr>
<td>
`num_shards`
</td>
<td>
The number of shards.
</td>
</tr><tr>
<td>
`input_shard_axes`
</td>
<td>
A list of dimensions along which to shard `inputs`, or
`None`. `None` means "shard all inputs along dimension 0". If not `None`,
there must be one dimension per input.
</td>
</tr><tr>
<td>
`outputs_from_all_shards`
</td>
<td>
Boolean or list of boolean. For each output, if
`True`, outputs from all shards are concatenated along the corresponding
`output_shard_axes` entry. Otherwise, each output is taken
from an arbitrary shard. If the argument is a boolean, the argument's
value is used for each output.
</td>
</tr><tr>
<td>
`output_shard_axes`
</td>
<td>
A list of dimensions along which to concatenate the
outputs of `computation`, or `None`. `None` means "concatenate all outputs
along dimension 0". If not `None`, there must be one dimension per output.
Ignored if `outputs_from_all_shards` is False.
</td>
</tr><tr>
<td>
`infeed_queue`
</td>
<td>
If not `None`, the `InfeedQueue` to use to augment the inputs
of `computation`.
</td>
</tr><tr>
<td>
`device_assignment`
</td>
<td>
If not `None`, a `DeviceAssignment` describing the
mapping between logical cores in the computation with physical cores in
the TPU topology. Uses a default device assignment if `None`. The
`DeviceAssignment` may be omitted if each shard of the computation uses
only one core, and there is either only one shard, or the number of shards
is equal to the number of cores in the TPU system.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Deprecated) Does nothing.
</td>
</tr><tr>
<td>
`xla_options`
</td>
<td>
An instance of `tpu.XLAOptions` which indicates the options
passed to XLA compiler. Use `None` for default options.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of output tensors.
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
If num_shards <= 0
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If len(input_shard_axes) != len(inputs)
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If len(output_shard_axes) != len(outputs from `computation`)
</td>
</tr>
</table>

