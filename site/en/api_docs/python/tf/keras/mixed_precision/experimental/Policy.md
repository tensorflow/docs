description: A deprecated dtype policy for a Keras layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.experimental.Policy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.mixed_precision.experimental.Policy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L322-L410">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A deprecated dtype policy for a Keras layer.

Inherits From: [`Policy`](../../../../tf/keras/mixed_precision/Policy.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.experimental.Policy(
    name, loss_scale='auto'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: This class is now deprecated and will be removed soon. Please use the
non-experimental class <a href="../../../../tf/keras/mixed_precision/Policy.md"><code>tf.keras.mixed_precision.Policy</code></a> instead.

The difference between this class and the non-experimental class is that this
class has a `loss_scale` field and the non-experimental class does not. The
loss scale is only used by <a href="../../../../tf/keras/Model.md#compile"><code>tf.keras.Model.compile</code></a>, which automatically wraps
the optimizer with a `LossScaleOptimizer` if the optimzier is not already a
`LossScaleOptimizer`. For the non-experimental Policy class, <a href="../../../../tf/keras/Model.md#compile"><code>Model.compile</code></a>
instead wraps the optimizer with a `LossScaleOptimizer` if <a href="../../../../tf/keras/mixed_precision/Policy.md#name"><code>Policy.name</code></a> is
"mixed_float16".

When deserializing objects with an experimental policy using functions like
<a href="../../../../tf/keras/utils/deserialize_keras_object.md"><code>tf.keras.utils.deserialize_keras_object</code></a>, the policy will be deserialized as
the non-experimental <a href="../../../../tf/keras/mixed_precision/Policy.md"><code>tf.keras.mixed_precision.Policy</code></a>, and the loss scale
will silently be dropped. This is so that SavedModels that are generated
with an expeirmental policy can be restored after the experimental policy is
removed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
A string. Can be one of the following values:
* Any dtype name, such as 'float32' or 'float64'. Both the variable and
compute dtypes will be that dtype.
* 'mixed_float16' or 'mixed_bfloat16': The compute dtype is float16 or
bfloat16, while the variable dtype is float32. With 'mixed_float16',
a dynamic loss scale is used. These policies are used for mixed
precision training.
</td>
</tr><tr>
<td>
`loss_scale`
</td>
<td>
A <a href="../../../../tf/mixed_precision/experimental/LossScale.md"><code>tf.compat.v1.mixed_precision.LossScale</code></a>, an int (which
uses a `FixedLossScale`), the string "dynamic" (which uses a
`DynamicLossScale`), or None (which uses no loss scale). Defaults to
`"auto"`. In the `"auto"` case: 1) if `name` is `"mixed_float16"`, then
use `loss_scale="dynamic"`. 2) otherwise, do not use a loss scale. Only
<a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>s, not layers, use the loss scale, and it is only used
during <a href="../../../../tf/keras/Model.md#fit"><code>Model.fit</code></a>, <a href="../../../../tf/keras/Model.md#train_on_batch"><code>Model.train_on_batch</code></a>, and other similar methods.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`compute_dtype`
</td>
<td>
The compute dtype of this policy.

This is the dtype layers will do their computations in. Typically layers
output tensors with the compute dtype as well.

Note that even if the compute dtype is float16 or bfloat16, hardware devices
may not do individual adds, multiplies, and other fundamental operations in
float16 or bfloat16, but instead may do some of them in float32 for numeric
stability. The compute dtype is the dtype of the inputs and outputs of the
TensorFlow ops that the layer executes. Internally, many TensorFlow ops will
do certain internal calculations in float32 or some other device-internal
intermediate format with higher precision than float16/bfloat16, to increase
numeric stability.

For example, a <a href="../../../../tf/keras/layers/Dense.md"><code>tf.keras.layers.Dense</code></a> layer, when run on a GPU with a
float16 compute dtype, will pass float16 inputs to <a href="../../../../tf/linalg/matmul.md"><code>tf.linalg.matmul</code></a>. But,
<a href="../../../../tf/linalg/matmul.md"><code>tf.linalg.matmul</code></a> will do use float32 intermediate math. The performance
benefit of float16 is still apparent, due to increased memory bandwidth and
the fact modern GPUs have specialized hardware for computing matmuls on
float16 inputs while still keeping intermediate computations in float32.
</td>
</tr><tr>
<td>
`loss_scale`
</td>
<td>
Returns the loss scale of this Policy.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Returns the name of this policy.
</td>
</tr><tr>
<td>
`variable_dtype`
</td>
<td>
The variable dtype of this policy.

This is the dtype layers will create their variables in, unless a layer
explicitly chooses a different dtype. If this is different than
<a href="../../../../tf/keras/mixed_precision/Policy.md#compute_dtype"><code>Policy.compute_dtype</code></a>, Layers will cast variables to the compute dtype to
avoid type errors.

Variable regularizers are run in the variable dtype, not the compute dtype.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L404-L410">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config, custom_objects=None
)
</code></pre>




<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L393-L402">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>






