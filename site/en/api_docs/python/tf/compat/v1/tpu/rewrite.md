description: Rewrites computation for execution on a TPU system.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.rewrite" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.rewrite

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu.py#L1852-L1902">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Rewrites `computation` for execution on a TPU system.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.rewrite(
    computation, inputs=None, infeed_queue=None, device_assignment=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`computation`
</td>
<td>
A Python function that builds a computation to apply to the
input. If the function takes n inputs, 'inputs' should be a list of n
tensors.

`computation` may return a list of operations and tensors. Tensors must
come before operations in the returned list.  The return value of
`rewrite` is a list of tensors corresponding to the tensors from the
output of `computation`.

All `Operation`s constructed during `computation` will be executed when
evaluating any of the returned output tensors, not just the ones returned.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A list of input tensors or `None` (equivalent to an empty list).
Each input can be a nested structure containing values that are
convertible to tensors. Note that passing an N-dimension list of
compatible values will result in a N-dimension list of scalar tensors
rather than a single Rank-N tensors. If you need different behavior,
convert part of inputs to tensors with <a href="../../../../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>.
</td>
</tr><tr>
<td>
`infeed_queue`
</td>
<td>
If not `None`, the `InfeedQueue` from which to append a tuple
of arguments as inputs to `computation`.
</td>
</tr><tr>
<td>
`device_assignment`
</td>
<td>
if not `None`, a `DeviceAssignment` describing the
mapping between logical cores in the computation with physical cores in
the TPU topology. May be omitted for a single-core computation, in which
case the core attached to task 0, TPU device 0 is used.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Deprecated) Does nothing.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Same data structure as if computation(*inputs) is called directly with some
exceptions for correctness. Exceptions include:
1) None output: a NoOp would be returned which control-depends on
computation.
2) Single value output: A tuple containing the value would be returned.
3) Operation-only outputs: a NoOp would be returned which
control-depends on computation.
</td>
</tr>

</table>


