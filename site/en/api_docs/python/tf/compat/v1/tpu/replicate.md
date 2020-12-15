description: Builds a graph operator that runs a replicated TPU computation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.replicate" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.replicate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu.py#L815-L915">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Builds a graph operator that runs a replicated TPU computation.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.replicate(
    computation, inputs=None, infeed_queue=None, device_assignment=None, name=None,
    maximum_shapes=None, padding_spec=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Example for the basic usage that `inputs` has static shape:

```python

def computation(x):
  x = x + 1
  return tf.math.reduce_mean(x)

x = tf.convert_to_tensor([1., 2., 3.])
y = tf.convert_to_tensor([4., 5., 6.])
tf.compat.v1.tpu.replicate(computation, inputs=[[x], [y]])
```

If the `inputs` has dynamic shapes and you would like to automatically
bucketize the inputs to avoid XLA recompilation. See the advanced example
below:

```python

def computation(x):
  x = x + 1
  return tf.math.reduce_mean(x)

# Assume input tensors in two replicas `x` and `y` both have dynamic shape
# ([None, 2]).
tf.compat.v1.tpu.replicate(
  computation,
  inputs=[x, y],
  maximum_shapes=[tf.TensorShape([None, None])],
  padding_spec=tf.compat.v1.tpu.PaddingSpec.POWER_OF_TWO)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`computation`
</td>
<td>
A Python function that builds the computation to replicate.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A list of lists of input tensors or `None` (equivalent to
`[[]]`), indexed by `[replica_num][input_num]`. All replicas must
have the same number of inputs. Each input can be a nested structure
containing values that are convertible to tensors. Note that passing an
N-dimension list of compatible values will result in a N-dimension list of
scalar tensors rather than a single Rank-N tensors. If you need different
behavior, convert part of inputs to tensors with <a href="../../../../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>.
</td>
</tr><tr>
<td>
`infeed_queue`
</td>
<td>
If not `None`, the `InfeedQueue` from which to append a tuple
of arguments as inputs to computation.
</td>
</tr><tr>
<td>
`device_assignment`
</td>
<td>
If not `None`, a `DeviceAssignment` describing the
mapping between logical cores in the computation with physical cores in
the TPU topology. Uses a default device assignment if `None`. The
`DeviceAssignment` may be omitted if each replica of the computation uses
only one core, and there is either only one replica, or the number of
replicas is equal to the number of cores in the TPU system.
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
`maximum_shapes`
</td>
<td>
A nested structure of tf.TensorShape representing the shape
to which the respective component of each input element in each replica
should be padded. Any unknown dimensions (e.g.
tf.compat.v1.Dimension(None) in a tf.TensorShape or -1 in a tensor-like
object) will be padded to the maximum size of that dimension over all
replicas. The structure of `maximum_shapes` needs to be the same as
`inputs[0]`.
</td>
</tr><tr>
<td>
`padding_spec`
</td>
<td>
An enum specified by `tpu.PaddingSpec`. This describes the
padding policy when the `inputs` to `tpu.replicate` is dynamic.
One usage is to enable automatic bucketizing on the inputs by setting the
value to `tpu.PaddingSpec.POWER_OF_TWO`, which can help to reduce the
recompilation in the XLA side.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of outputs, indexed by `[replica_num]` each output can be a nested
structure same as what computation() returns with a few exceptions.

Exceptions include:
1) None output: a NoOp would be returned which control-depends on
computation.
2) Single value output: A tuple containing the value would be returned.
3) Operation-only outputs: a NoOp would be returned which
control-depends on computation.
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
If all replicas do not have equal numbers of input tensors.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the number of inputs per replica does not match
the number of formal parameters to `computation`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the static `inputs` dimensions don't match with the values
given in `maximum_shapes`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the structure of inputs per replica does not match
the structure of `maximum_shapes`.
</td>
</tr>
</table>

