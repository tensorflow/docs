description: Enable or disable the use of TensorFloat-32 on supported hardware.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.enable_tensor_float_32_execution" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental.enable_tensor_float_32_execution

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/config.py#L40-L90">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enable or disable the use of TensorFloat-32 on supported hardware.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.enable_tensor_float_32_execution`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental.enable_tensor_float_32_execution(
    enabled
)
</code></pre>



<!-- Placeholder for "Used in" -->

[TensorFloat-32](https://blogs.nvidia.com/blog/2020/05/14/tensorfloat-32-precision-format),
or TF32 for short, is a math mode for NVIDIA Ampere GPUs. TensorFloat-32
execution causes certain float32 ops, such as matrix multiplications and
convolutions, to run much faster on Ampere GPUs but with reduced precision.
This reduced precision should not impact convergence of deep learning models
in practice.

TensorFloat-32 is enabled by default. TensorFloat-32 is only supported on
Ampere GPUs, so all other hardware will use the full float32 precision
regardless of whether TensorFloat-32 is enabled or not. If you want to use the
full float32 precision on Ampere, you can disable TensorFloat-32 execution
with this function. For example:

```python
x = tf.fill((2, 2), 1.0001)
y = tf.fill((2, 2), 1.)
# TensorFloat-32 is enabled, so matmul is run with reduced precision
print(tf.linalg.matmul(x, y))  # [[2., 2.], [2., 2.]]
tf.config.experimental.enable_tensor_float_32_execution(False)
# Matmul is run with full precision
print(tf.linalg.matmul(x, y))  # [[2.0002, 2.0002], [2.0002, 2.0002]]
```

To check whether TensorFloat-32 execution is currently enabled, use
<a href="../../../tf/config/experimental/tensor_float_32_execution_enabled.md"><code>tf.config.experimental.tensor_float_32_execution_enabled</code></a>.

If TensorFloat-32 is enabled, float32 inputs of supported ops, such as
<a href="../../../tf/linalg/matmul.md"><code>tf.linalg.matmul</code></a>, will be rounded from 23 bits of precision to 10 bits of
precision in most cases. This allows the ops to execute much faster by
utilizing the GPU's tensor cores. TensorFloat-32 has the same dynamic range as
float32, meaning it is no more likely to underflow or overflow than float32.
Ops still use float32 accumulation when TensorFloat-32 is enabled. Enabling or
disabling TensorFloat-32 only affects Ampere GPUs and subsequent GPUs that
support TensorFloat-32.

Note TensorFloat-32 is not always used in supported ops, as only inputs of
certain shapes are supported. Support for more input shapes and more ops may
be added in the future. As a result, precision of float32 ops may decrease in
minor versions of TensorFlow.

TensorFloat-32 is also used for some complex64 ops. Currently, TensorFloat-32
is used in fewer cases for complex64 as it is for float32.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`enabled`
</td>
<td>
Bool indicating whether to enable TensorFloat-32 execution.
</td>
</tr>
</table>

