description: Parameters that are used for TF-TRT conversion.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.tensorrt.ConversionParams" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="allow_build_at_runtime"/>
<meta itemprop="property" content="is_dynamic_op"/>
<meta itemprop="property" content="max_batch_size"/>
<meta itemprop="property" content="max_workspace_size_bytes"/>
<meta itemprop="property" content="maximum_cached_engines"/>
<meta itemprop="property" content="minimum_segment_size"/>
<meta itemprop="property" content="precision_mode"/>
<meta itemprop="property" content="rewriter_config_template"/>
<meta itemprop="property" content="use_calibration"/>
</div>

# tf.experimental.tensorrt.ConversionParams

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/compiler/tensorrt/trt_convert.py#L118-L181">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Parameters that are used for TF-TRT conversion.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.tensorrt.ConversionParams(
    rewriter_config_template=None,
    max_workspace_size_bytes=DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES,
    precision_mode=TrtPrecisionMode.FP32, minimum_segment_size=3,
    is_dynamic_op=(True), maximum_cached_engines=1, use_calibration=(True),
    max_batch_size=1, allow_build_at_runtime=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Fields:


* <b>`rewriter_config_template`</b>: a template RewriterConfig proto used to create a
  TRT-enabled RewriterConfig. If None, it will use a default one.
* <b>`max_workspace_size_bytes`</b>: the maximum GPU temporary memory which the TRT
  engine can use at execution time. This corresponds to the
  'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize().
* <b>`precision_mode`</b>: one the strings in
  TrtPrecisionMode.supported_precision_modes().
* <b>`minimum_segment_size`</b>: the minimum number of nodes required for a subgraph
  to be replaced by TRTEngineOp.
* <b>`is_dynamic_op`</b>: whether to generate dynamic TRT ops which will build the
  TRT network and engine at run time. i.e. Since TensorRT version < 6.0
  does not support dynamic dimensions other than the batch dimension, when
  the TensorFlow graph has a non-batch dimension of dynamic size, we would
  need to enable this option. This option should be set to True in TF 2.0.
* <b>`maximum_cached_engines`</b>: max number of cached TRT engines for dynamic TRT
  ops. Created TRT engines for a dynamic dimension are cached. This is the
  maximum number of engines that can be cached. If the number of cached
  engines is already at max but none of them supports the input shapes,
  the TRTEngineOp will fall back to run the original TF subgraph that
  corresponds to the TRTEngineOp.
* <b>`use_calibration`</b>: this argument is ignored if precision_mode is not INT8.
  If set to True, a calibration graph will be created to calibrate the
  missing ranges. The calibration graph must be converted to an inference
  graph by running calibration with calibrate(). If set to False,
  quantization nodes will be expected for every tensor in the graph
  (excluding those which will be fused). If a range is missing, an error
  will occur. Please note that accuracy may be negatively affected if
  there is a mismatch between which tensors TRT quantizes and which
  tensors were trained with fake quantization.
* <b>`max_batch_size`</b>: max size for the input batch. This parameter is only
  effective when use_implicit_batch is true.
* <b>`allow_build_at_runtime`</b>: whether to build TensorRT engines during runtime.
  If no TensorRT engine can be found in cache that can handle the given
  inputs during runtime, then a new TensorRT engine is built at runtime if
  allow_build_at_runtime=True, and otherwise native TF is used. This
  argument is only effective if is_dynamic_op=True.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`rewriter_config_template`
</td>
<td>

</td>
</tr><tr>
<td>
`max_workspace_size_bytes`
</td>
<td>

</td>
</tr><tr>
<td>
`precision_mode`
</td>
<td>

</td>
</tr><tr>
<td>
`minimum_segment_size`
</td>
<td>

</td>
</tr><tr>
<td>
`is_dynamic_op`
</td>
<td>

</td>
</tr><tr>
<td>
`maximum_cached_engines`
</td>
<td>

</td>
</tr><tr>
<td>
`use_calibration`
</td>
<td>

</td>
</tr><tr>
<td>
`max_batch_size`
</td>
<td>

</td>
</tr><tr>
<td>
`allow_build_at_runtime`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `allow_build_at_runtime` <a id="allow_build_at_runtime"></a>
* `is_dynamic_op` <a id="is_dynamic_op"></a>
* `max_batch_size` <a id="max_batch_size"></a>
* `max_workspace_size_bytes` <a id="max_workspace_size_bytes"></a>
* `maximum_cached_engines` <a id="maximum_cached_engines"></a>
* `minimum_segment_size` <a id="minimum_segment_size"></a>
* `precision_mode` <a id="precision_mode"></a>
* `rewriter_config_template` <a id="rewriter_config_template"></a>
* `use_calibration` <a id="use_calibration"></a>
