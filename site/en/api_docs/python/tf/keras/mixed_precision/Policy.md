description: A dtype policy for a Keras layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.Policy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.mixed_precision.Policy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L37-L318">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A dtype policy for a Keras layer.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.Policy(
    name
)
</code></pre>



<!-- Placeholder for "Used in" -->

A dtype policy determines a layer's computation and variable dtypes. Each
layer has a policy. Policies can be passed to the `dtype` argument of layer
constructors, or a global policy can be set with
<a href="../../../tf/keras/mixed_precision/set_global_policy.md"><code>tf.keras.mixed_precision.set_global_policy</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
The policy name, which determines the compute and variable dtypes. Can
be any dtype name, such as `'float32'` or `'float64'`, which causes both
the compute and variable dtypes will be that dtype. Can also be the string
`'mixed_float16'` or `'mixed_bfloat16'`, which causes the compute dtype to
be float16 or bfloat16 and the variable dtype to be float32.
</td>
</tr>
</table>


Typically you only need to interact with dtype policies when using mixed
precision, which is the use of float16 or bfloat16 for computations and
float32 for variables. This is why the term `mixed_precision` appears in the
API name. Mixed precision can be enabled by passing `'mixed_float16'` or
`'mixed_bfloat16'` to `tf.keras.mixed_precision.set_global_policy`. See [the
mixed precision guide](https://www.tensorflow.org/guide/keras/mixed_precision)
for more information on how to use mixed precision.

```
>>> tf.keras.mixed_precision.set_global_policy('mixed_float16')
>>> layer1 = tf.keras.layers.Dense(10)
>>> layer1.dtype_policy  # `layer1` will automatically use mixed precision
<Policy "mixed_float16">
>>> # Can optionally override layer to use float32 instead of mixed precision.
>>> layer2 = tf.keras.layers.Dense(10, dtype='float32')
>>> layer2.dtype_policy
<Policy "float32">
>>> # Set policy back to initial float32 for future examples.
>>> tf.keras.mixed_precision.set_global_policy('float32')
```

In the example above, passing `dtype='float32'` to the layer is equivalent to
passing `dtype=tf.keras.mixed_precision.Policy('float32')`. In general,
passing a dtype to a layer is equivalent to passing the corresponding policy,
so it is never necessary to explicitly construct a `Policy` object.

Note: <a href="../../../tf/keras/Model.md#compile"><code>Model.compile</code></a> will automatically wrap an optimizer with a
<a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> if you use the `'mixed_float16'`
policy. If you use a custom training loop instead of calling <a href="../../../tf/keras/Model.md#compile"><code>Model.compile</code></a>,
you should explicitly use a <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> to
avoid numeric underflow with float16.

### How a layer uses its policy's compute dtype

A layer casts its inputs to its compute dtype. This causes the layer's
computations and output to also be in the compute dtype. For example:

```
>>> x = tf.ones((4, 4, 4, 4), dtype='float64')
>>> # `layer`'s policy defaults to float32.
>>> layer = tf.keras.layers.Conv2D(filters=4, kernel_size=2)
>>> layer.compute_dtype  # Equivalent to layer.dtype_policy.compute_dtype
'float32'
>>> # `layer` casts it's inputs to its compute dtype and does computations in
>>> # that dtype.
>>> y = layer(x)
>>> y.dtype
tf.float32
```

Note that the base <a href="../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a> class inserts the casts. If
subclassing your own layer, you do not have to insert any casts.

Currently, only tensors in the first argument to the layer's `call` method are
casted (although this will likely be changed in a future minor release). For
example:

```
>>> class MyLayer(tf.keras.layers.Layer):
...   # Bug! `b` will not be casted.
...   def call(self, a, b):
...     return a + 1., b + 1.
>>> a = tf.constant(1., dtype="float32")
>>> b = tf.constant(1., dtype="float32")
>>> layer = MyLayer(dtype="float64")
>>> x, y = layer(a, b)
>>> x.dtype
tf.float64
>>> y.dtype
tf.float32
```

If writing your own layer with multiple inputs, you should either explicitly
cast other tensors to `self.compute_dtype` in `call` or accept all tensors in
the first argument as a list.

The casting only occurs in TensorFlow 2. If
<a href="../../../tf/compat/v1/disable_v2_behavior.md"><code>tf.compat.v1.disable_v2_behavior()</code></a> has been called, you can enable the
casting behavior with <a href="../../../tf/compat/v1/keras/layers/enable_v2_dtype_behavior.md"><code>tf.compat.v1.keras.layers.enable_v2_dtype_behavior()</code></a>.

### How a layer uses its policy's variable dtype

The default dtype of variables created by <a href="../../../tf/keras/layers/Layer.md#add_weight"><code>tf.keras.layers.Layer.add_weight</code></a>
is the layer's policy's variable dtype.

If a layer's compute and variable dtypes differ, `add_weight` will wrap
floating-point variables with a special wrapper called an `AutoCastVariable`.
`AutoCastVariable` is identical to the original variable except it casts
itself to the layer's compute dtype when used within <a href="../../../tf/keras/layers/Layer.md#call"><code>Layer.call</code></a>. This means
if you are writing a layer, you do not have to explicitly cast the variables
to the layer's compute dtype. For example:

```
>>> class SimpleDense(tf.keras.layers.Layer):
...
...   def build(self, input_shape):
...     # With mixed precision, self.kernel is a float32 AutoCastVariable
...     self.kernel = self.add_weight('kernel', (input_shape[-1], 10))
...
...   def call(self, inputs):
...     # With mixed precision, self.kernel will be casted to float16
...     return tf.linalg.matmul(inputs, self.kernel)
...
>>> dtype_policy = tf.keras.mixed_precision.Policy('mixed_float16')
>>> layer = SimpleDense(dtype=dtype_policy)
>>> y = layer(tf.ones((10, 10)))
>>> y.dtype
tf.float16
>>> layer.kernel.dtype
tf.float32
```

A layer author can prevent a variable from being wrapped with an
`AutoCastVariable` by passing `experimental_autocast=False` to `add_weight`,
which is useful if the float32 value of the variable must be accessed within
the layer.

### How to write a layer that supports mixed precision and float64.

For the most part, layers will automatically support mixed precision and
float64 without any additional work, due to the fact the base layer
automatically casts inputs, creates variables of the correct type, and in the
case of mixed precision, wraps variables with `AutoCastVariables`.

The primary case where you need extra work to support mixed precision or
float64 is when you create a new tensor, such as with <a href="../../../tf/ones.md"><code>tf.ones</code></a> or
<a href="../../../tf/random/normal.md"><code>tf.random.normal</code></a>, In such cases, you must create the tensor of the correct
dtype. For example, if you call <a href="../../../tf/random/normal.md"><code>tf.random.normal</code></a>, you must pass the compute
dtype, which is the dtype the inputs have been casted to:

```
>>> class AddRandom(tf.keras.layers.Layer):
...
...   def call(self, inputs):
...     # We must pass `dtype=inputs.dtype`, otherwise a TypeError may
...     # occur when adding `inputs` to `rand`.
...     rand = tf.random.normal(shape=inputs.shape, dtype=inputs.dtype)
...     return inputs + rand
```

```
>>> dtype_policy = tf.keras.mixed_precision.Policy('mixed_float16')
>>> layer = AddRandom(dtype=dtype_policy)
>>> y = layer(x)
>>> y.dtype
tf.float16
```

If you did not pass `dtype=inputs.dtype` to <a href="../../../tf/random/normal.md"><code>tf.random.normal</code></a>, a
`TypeError` would have occurred. This is because the <a href="../../../tf/random/normal.md"><code>tf.random.normal</code></a>'s
dtype defaults to `"float32"`, but the input dtype is float16. You cannot add
a float32 tensor with a float16 tensor.



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

For example, a <a href="../../../tf/keras/layers/Dense.md"><code>tf.keras.layers.Dense</code></a> layer, when run on a GPU with a
float16 compute dtype, will pass float16 inputs to <a href="../../../tf/linalg/matmul.md"><code>tf.linalg.matmul</code></a>. But,
<a href="../../../tf/linalg/matmul.md"><code>tf.linalg.matmul</code></a> will do use float32 intermediate math. The performance
benefit of float16 is still apparent, due to increased memory bandwidth and
the fact modern GPUs have specialized hardware for computing matmuls on
float16 inputs while still keeping intermediate computations in float32.
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
<a href="../../../tf/keras/mixed_precision/Policy.md#compute_dtype"><code>Policy.compute_dtype</code></a>, Layers will cast variables to the compute dtype to
avoid type errors.

Variable regularizers are run in the variable dtype, not the compute dtype.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L310-L318">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config, custom_objects=None
)
</code></pre>




<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/policy.py#L307-L308">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>






