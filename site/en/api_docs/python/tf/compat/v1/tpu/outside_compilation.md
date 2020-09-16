description: Builds part of a computation outside any current TPU replicate scope.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.outside_compilation" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.outside_compilation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/tpu/tpu.py#L661-L780">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Builds part of a computation outside any current TPU replicate scope.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.outside_compilation(
    computation, *args, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

`tf.tpu.outside_compilation()` is used to run ops in `computation` on CPU
instead of running on TPU. For example, users can run ops that are not
supported on TPU's (e.g. tf.summary.write()) by explicitly placing those
ops on CPU's. Below usage of outside compilation will place ops in
`computation_with_string_ops` on CPU.

#### Example usage:



```python
def computation_with_string_ops(x):
  # strings types are not supported on TPU's and below ops must
  # run on CPU instead.
  output = tf.strings.format('1{}', x)
  return tf.strings.to_number(output)

def tpu_computation():
  # Expected output is 11.
  output = tf.tpu.outside_compilation(computation_with_string_ops, 1)
```

Outside compilation should be called inside TPUReplicateContext. That is,
`tf.tpu.outside_compilation()` should be called inside a function that is
passed to `tpu.split_compile_and_replicate()` -- this is implied when
outside compilation is invoked inside a function passed to TPUStrategy
`run()`. If invoked outside of TPUReplicateContext,
then this simply returns the result of `computation`, and therefore,
would be a no-op. Note that outside compilation is different from
`tf.distribute.experimental.TPUStrategy.merge_call()` as logic in
outside compilation is replicated and executed separately for each
replica. On the other hand, `merge_call()` requires a `merge_fn`
to aggregate the inputs from different replicas and is executed only
once.

For variables placed in TPU device, which includes variables created inside
TPUStrategy scope, outside compilation logic must not include variable
read/write. For variables placed on host, which is the case when variables
created via TPUEstimator, variable read/write is only allowed if the variable
is not accessed by any other ops in the TPU computation. Variable read/write
from outside compilation cluster is not visible from TPU computation and
vice versa. Therefore, if outside compilation logic contains such host
variables read/write ops and if the variables are accessed by TPU
computation as well, then this may lead to deadlock.

Internally, `tf.tpu.outside_compilation()` adds outside compilation
attributes to all ops in `computation`. During later graph pass, these
ops with outside compilation attribute is extracted out and replicated
into a host-side graph. Inputs to this extract host-side graph is sent
from TPU computation graph to host graph via a pair of XlaSendToHost and
XlaRecvFromHost ops. Note that using `tf.tpu.outside_compilation()`
may result in tensor transfer between TPU and CPU, leading to non-trivial
performance impact.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`computation`
</td>
<td>
A Python function that builds the computation to
place on the host.
</td>
</tr><tr>
<td>
`*args`
</td>
<td>
the positional arguments for the computation.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
the keyword arguments for the computation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The Tensors returned by computation.
</td>
</tr>

</table>

