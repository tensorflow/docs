description: An offline converter for TF-TRT transformation for TF 2.0 SavedModels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.tensorrt.Converter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="build"/>
<meta itemprop="property" content="convert"/>
<meta itemprop="property" content="save"/>
</div>

# tf.experimental.tensorrt.Converter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/compiler/tensorrt/trt_convert.py#L880-L1266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An offline converter for TF-TRT transformation for TF 2.0 SavedModels.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.tensorrt.Converter(
    input_saved_model_dir=None, input_saved_model_tags=None,
    input_saved_model_signature_key=None, conversion_params=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Currently this is not available on Windows platform.

Note that in V2, is_dynamic_op=False is not supported, meaning TRT engines
will be built only when the corresponding TRTEngineOp is executed. But we
still provide a way to avoid the cost of building TRT engines during inference
(see more below).

There are several ways to run the conversion:

1. FP32/FP16 precision

   ```python
   params = tf.experimental.tensorrt.ConversionParams(
       precision_mode='FP16')
   converter = tf.experimental.tensorrt.Converter(
       input_saved_model_dir="my_dir", conversion_params=params)
   converter.convert()
   converter.save(output_saved_model_dir)
   ```

   In this case, no TRT engines will be built or saved in the converted
   SavedModel. But if input data is available during conversion, we can still
   build and save the TRT engines to reduce the cost during inference (see
   option 2 below).

2. FP32/FP16 precision with pre-built engines

   ```python
   params = tf.experimental.tensorrt.ConversionParams(
       precision_mode='FP16',
       # Set this to a large enough number so it can cache all the engines.
       maximum_cached_engines=16)
   converter = tf.experimental.tensorrt.Converter(
       input_saved_model_dir="my_dir", conversion_params=params)
   converter.convert()

   # Define a generator function that yields input data, and use it to execute
   # the graph to build TRT engines.
   # With TensorRT 5.1, different engines will be built (and saved later) for
   # different input shapes to the TRTEngineOp.
   def my_input_fn():
     for _ in range(num_runs):
       inp1, inp2 = ...
       yield inp1, inp2

   converter.build(input_fn=my_input_fn)  # Generate corresponding TRT engines
   converter.save(output_saved_model_dir)  # Generated engines will be saved.
   ```

   In this way, one engine will be built/saved for each unique input shapes of
   the TRTEngineOp. This is good for applications that cannot afford building
   engines during inference but have access to input data that is similar to
   the one used in production (for example, that has the same input shapes).
   Also, the generated TRT engines is platform dependent, so we need to run
   `build()` in an environment that is similar to production (e.g. with
   same type of GPU).

3. INT8 precision and calibration with pre-built engines

   ```python
   params = tf.experimental.tensorrt.ConversionParams(
       precision_mode='INT8',
       # Currently only one INT8 engine is supported in this mode.
       maximum_cached_engines=1,
       use_calibration=True)
   converter = tf.experimental.tensorrt.Converter(
       input_saved_model_dir="my_dir", conversion_params=params)

   # Define a generator function that yields input data, and run INT8
   # calibration with the data. All input data should have the same shape.
   # At the end of convert(), the calibration stats (e.g. range information)
   # will be saved and can be used to generate more TRT engines with different
   # shapes. Also, one TRT engine will be generated (with the same shape as
   # the calibration data) for save later.
   def my_calibration_input_fn():
     for _ in range(num_runs):
       inp1, inp2 = ...
       yield inp1, inp2

   converter.convert(calibration_input_fn=my_calibration_input_fn)

   # (Optional) Generate more TRT engines offline (same as the previous
   # option), to avoid the cost of generating them during inference.
   def my_input_fn():
     for _ in range(num_runs):
       inp1, inp2 = ...
       yield inp1, inp2
   converter.build(input_fn=my_input_fn)

   # Save the TRT engine and the engines.
   converter.save(output_saved_model_dir)
   ```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_saved_model_dir`
</td>
<td>
the directory to load the SavedModel which contains
the input graph to transforms. Used only when input_graph_def is None.
</td>
</tr><tr>
<td>
`input_saved_model_tags`
</td>
<td>
list of tags to load the SavedModel.
</td>
</tr><tr>
<td>
`input_saved_model_signature_key`
</td>
<td>
the key of the signature to optimize the
graph for.
</td>
</tr><tr>
<td>
`conversion_params`
</td>
<td>
a TrtConversionParams instance.
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
if the combination of the parameters is invalid.
</td>
</tr>
</table>



## Methods

<h3 id="build"><code>build</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/compiler/tensorrt/trt_convert.py#L1126-L1187">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>build(
    input_fn
)
</code></pre>

Run inference with converted graph in order to build TensorRT engines.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
a generator function that yields input data as a list or tuple,
which will be used to execute the converted signature to generate TRT
engines. Example:
`def input_fn():
# Let's assume a network with 2 input tensors. We generate 3 sets
# of dummy input data:
input_shapes = [[(1, 16), (2, 16)], # 1st input list
[(2, 32), (4, 32)], # 2nd list of two tensors
[(4, 32), (8, 32)]] # 3rd input list
for shapes in input_shapes:
# return a list of input tensors
yield [np.zeros(x).astype(np.float32) for x in shapes]`
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
build() is already called.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
the input_fx is None.
</td>
</tr>
</table>



<h3 id="convert"><code>convert</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/compiler/tensorrt/trt_convert.py#L1060-L1124">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>convert(
    calibration_input_fn=None
)
</code></pre>

Convert the input SavedModel in 2.0 format.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`calibration_input_fn`
</td>
<td>
a generator function that yields input data as a
list or tuple, which will be used to execute the converted signature for
calibration. All the returned input data should have the same shape.
Example: `def input_fn(): yield input1, input2, input3`
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the input combination is invalid.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The TF-TRT converted Function.
</td>
</tr>

</table>



<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/compiler/tensorrt/trt_convert.py#L1189-L1266">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save(
    output_saved_model_dir
)
</code></pre>

Save the converted SavedModel.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`output_saved_model_dir`
</td>
<td>
directory to saved the converted SavedModel.
</td>
</tr>
</table>





