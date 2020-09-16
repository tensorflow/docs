description: Converts a TensorFlow model into TensorFlow Lite model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lite.TFLiteConverter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="convert"/>
<meta itemprop="property" content="from_concrete_functions"/>
<meta itemprop="property" content="from_keras_model"/>
<meta itemprop="property" content="from_saved_model"/>
</div>

# tf.lite.TFLiteConverter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/lite.py#L904-L1076">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a TensorFlow model into TensorFlow Lite model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lite.TFLiteConverter(
    funcs, trackable_obj=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example usage:


```python
# Converting a SavedModel to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Converting a tf.Keras model to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Converting ConcreteFunctions to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_concrete_functions([func])
tflite_model = converter.convert()
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`funcs`
</td>
<td>
List of TensorFlow ConcreteFunctions. The list should not contain
duplicate elements.
</td>
</tr><tr>
<td>
`trackable_obj`
</td>
<td>
tf.AutoTrackable object associated with `funcs`. A
reference to this object needs to be maintained so that Variables do not
get garbage collected since functions have a weak reference to
Variables. This is only required when the tf.AutoTrackable object is not
maintained by the user (e.g. `from_saved_model`).
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`allow_custom_ops`
</td>
<td>
Boolean indicating whether to allow custom operations.
When False, any unknown operation is an error. When True, custom ops are
created for any op that is unknown. The developer needs to provide these
to the TensorFlow Lite runtime with a custom resolver. (default False)
</td>
</tr><tr>
<td>
`optimizations`
</td>
<td>
Experimental flag, subject to change. A list of optimizations
to apply when converting the model. E.g. `[Optimize.DEFAULT]`
</td>
</tr><tr>
<td>
`representative_dataset`
</td>
<td>
A representative dataset that can be used to
generate input and output samples for the model. The converter can use the
dataset to evaluate different optimizations. Note that this is an optional
attribute but it is necessary if INT8 is the only support builtin ops in
target ops.
</td>
</tr><tr>
<td>
`target_spec`
</td>
<td>
Experimental flag, subject to change. Specification of target
device.
</td>
</tr><tr>
<td>
`inference_input_type`
</td>
<td>
Data type of the input layer. Note that integer types
(tf.int8 and tf.uint8) are currently only supported for post training
integer quantization. (default tf.float32, must be in {tf.float32,
tf.int8, tf.uint8})
</td>
</tr><tr>
<td>
`inference_output_type`
</td>
<td>
Data type of the output layer. Note that integer
types (tf.int8 and tf.uint8) are currently only supported for post
training integer quantization. (default tf.float32, must be in
{tf.float32, tf.int8, tf.uint8})
</td>
</tr><tr>
<td>
`experimental_new_converter`
</td>
<td>
Experimental flag, subject to change. Enables
MLIR-based conversion instead of TOCO conversion. (default True)
</td>
</tr>
</table>



## Methods

<h3 id="convert"><code>convert</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/lite.py#L1063-L1076">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>convert()
</code></pre>

Converts a TensorFlow GraphDef based on instance variables.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The converted data in serialized format.
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
No concrete functions is specified.
Multiple concrete functions are specified.
Input shape is not specified.
Invalid quantization parameters.
</td>
</tr>
</table>



<h3 id="from_concrete_functions"><code>from_concrete_functions</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/lite.py#L964-L986">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_concrete_functions(
    funcs
)
</code></pre>

Creates a TFLiteConverter object from ConcreteFunctions.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`funcs`
</td>
<td>
List of TensorFlow ConcreteFunctions. The list should not contain
duplicate elements. Currently converter can only convert a single
ConcreteFunction. Converting multiple functions is under development.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
TFLiteConverter object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
Invalid input type.
</td>
</tr>

</table>



<h3 id="from_keras_model"><code>from_keras_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/lite.py#L1050-L1060">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_keras_model(
    model
)
</code></pre>

Creates a TFLiteConverter object from a Keras model.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`model`
</td>
<td>
tf.Keras.Model
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
TFLiteConverter object.
</td>
</tr>

</table>



<h3 id="from_saved_model"><code>from_saved_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/lite.py#L988-L1048">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_saved_model(
    saved_model_dir, signature_keys=None, tags=None
)
</code></pre>

Creates a TFLiteConverter object from a SavedModel directory.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`saved_model_dir`
</td>
<td>
SavedModel directory to convert.
</td>
</tr><tr>
<td>
`signature_keys`
</td>
<td>
List of keys identifying SignatureDef containing inputs
and outputs. Elements should not be duplicated. By default the
`signatures` attribute of the MetaGraphdef is used. (default
saved_model.signatures)
</td>
</tr><tr>
<td>
`tags`
</td>
<td>
Set of tags identifying the MetaGraphDef within the SavedModel to
analyze. All tags in the tag set must be present. (default set(SERVING))
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
TFLiteConverter object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
Invalid signature keys.
</td>
</tr>

</table>





