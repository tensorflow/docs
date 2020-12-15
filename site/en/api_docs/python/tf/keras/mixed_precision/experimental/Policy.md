description: A dtype policy for a Keras layer.

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
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/mixed_precision/experimental/policy.py#L41-L478">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A dtype policy for a Keras layer.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.experimental.Policy(
    name, loss_scale=USE_DEFAULT
)
</code></pre>



<!-- Placeholder for "Used in" -->

A dtype policy determines dtype-related aspects of a layer, such as its
computation and variable dtypes. Each layer has a policy. Policies can be
passed to the `dtype` argument of layer constructors, or a global policy can
be set with <a href="../../../../tf/keras/mixed_precision/experimental/set_policy.md"><code>tf.keras.mixed_precision.experimental.set_policy</code></a>. A layer will
default to the global policy if no policy is passed to it's constructor.

For many models, each layer's policy will have the same compute dtype and
variable dtype, which will typically be float32. In this case, we refer to the
singular dtype as the layer's dtype, which can be queried by the property
<a href="../../../../tf/keras/layers/Layer.md#dtype"><code>tf.keras.layers.Layer.dtype</code></a>.

When mixed precision training is used, most layers will instead have a float16
or bfloat16 compute dtype and a float32 variable dtype, and so the layer does
not have a single dtype. When the variable dtype does not match the compute
dtype, variables will be automatically casted to the compute dtype to avoid
type errors. In this case, <a href="../../../../tf/keras/layers/Layer.md#dtype"><code>tf.keras.layers.Layer.dtype</code></a> refers to the
variable dtype, not the compute dtype. See [the mixed precision guide](
  https://www.tensorflow.org/guide/keras/mixed_precision) for more
information on how to use mixed precision.

Certain policies also have a <a href="../../../../tf/mixed_precision/experimental/LossScale.md"><code>tf.mixed_precision.experimental.LossScale</code></a>
instance, which is used by <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>s to performance loss scaling. Loss
scaling is a technique used with mixed precision to avoid numerical underflow
in float16 gradients. Loss scaling is only done by Models in <a href="../../../../tf/keras/Model.md#fit"><code>Model.fit</code></a>,
<a href="../../../../tf/keras/Model.md#train_on_batch"><code>Model.train_on_batch</code></a>, and similar methods. Layers which are not Models
ignore the loss scale.

Policies are constructed by passing a string to the constructor, e.g.
`tf.keras.mixed_precision.experimental.Policy('float32')`. The string
determines the compute and variable dtypes. It can be one of the following:

  * Any dtype name, such as 'float32' or 'float64'. Both the variable and
    compute dtypes will be that dtype. No loss scaling is done by default.
  * 'mixed_float16' or 'mixed_bfloat16': The compute dtype is float16 or
    bfloat16, while the variable dtype is float32. These policies are used for
    mixed precision training. With 'mixed_float16', a dynamic loss scale is
    used by default. 'mixed_bfloat16' does no loss scaling by default, as loss
    scaling is unnecessary with bfloat16.

### How to use mixed precision in a Keras model

To use mixed precision in a Keras model, the `'mixed_float16'` or
`'mixed_bfloat16'` policy can be used.
<a href="../../../../tf/keras/mixed_precision/experimental/set_policy.md"><code>tf.keras.mixed_precision.experimental.set_policy</code></a> can be used to set the
default policy for layers if no policy is passed to them. For example:

```
>>> tf.keras.mixed_precision.experimental.set_policy('mixed_float16')
>>> model = tf.keras.models.Sequential([
...     tf.keras.layers.Input((100,)),
...     # Dense layers use global policy of 'mixed_float16', which does
...     # computations in float16 while keeping variables in float32.
...     tf.keras.layers.Dense(10),
...     tf.keras.layers.Dense(10),
...     # Softmax should be done in float32 for numeric stability. We pass
...     # dtype='float32' to use float32 instead of the global policy.
...     tf.keras.layers.Activation('softmax', dtype='float32')
... ])
```

Alternatively, the policy can be passed to individual layers instead of
setting the global policy with `set_policy`:

```
>>> policy = tf.keras.mixed_precision.experimental.Policy('mixed_float16')
>>> model = tf.keras.models.Sequential([
...     tf.keras.layers.Input((100,)),
...     tf.keras.layers.Dense(10, dtype=policy),
...     tf.keras.layers.Dense(10, dtype=policy),
...     # Softmax should be done in float32 for numeric stability.
...     tf.keras.layers.Activation('softmax', dtype='float32')
... ])
```

Note the `'mixed_float16'` policy will apply loss scaling by default in
<a href="../../../../tf/keras/Model.md#fit"><code>Model.fit</code></a>, <a href="../../../../tf/keras/Model.md#train_on_batch"><code>Model.train_on_batch</code></a>, and other training methods. If no such
method is used (e.g., a custom training loop is used) and `'mixed_float16'` is
used, the loss scale must be manually applied. See
<a href="../../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.experimental.LossScaleOptimizer</code></a> for details. For
`'mixed_bfloat16'`, no loss scaling is done and loss scaling never needs to be
manually applied.

See [the mixed precision guide](
  https://www.tensorflow.org/guide/keras/mixed_precision) for more
information on using mixed precision

### How to use float64 in a Keras model

Using float64 is similar to mixed precision. Either the global policy can be
set to float64, or `dtype='float64'` can be passed to individual layers. For
example, to set the global policy:

```
>>> tf.keras.mixed_precision.experimental.set_policy('float64')
>>> model = tf.keras.models.Sequential([
...     tf.keras.layers.Input((100,)),
...     # All layers use global policy of 'float64', which does computations
...     # and creates variables in float64.
...     tf.keras.layers.Dense(10),
...     tf.keras.layers.Dense(10),
...     tf.keras.layers.Activation('softmax')
... ])
>>> # Optionaly set policy back to float32 if any other models use float32
>>> tf.keras.mixed_precision.experimental.set_policy('float32')
```

### How a layer uses its policy's compute dtype

A layer will cast its inputs to its compute dtype in TensorFlow 2. For
example:

```
>>> x = tf.ones((4, 4, 4, 4), dtype='float64')
>>> # `layer`'s policy defaults to float32.
>>> layer = tf.keras.layers.Conv2D(filters=4, kernel_size=2)
>>> # `layer` casts it's inputs to its compute dtype, which is float32, and
>>> # does computations in float32.
>>> y = layer(x)
>>> y.dtype
tf.float32
```

Note that the base <a href="../../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a> class inserts the casts. If
subclassing your own layer, you do not have to insert any casts.

Currently, only tensors in the first argument to the layer's `call` method are
casted. For example:

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

If writing your own layer, it is recommended to accept tensors only in the
first argument. This way, all tensors are casted to the layer's compute dtype.
`MyLayer` should therefore be written as:

```
>>> class MyLayer(tf.keras.layers.Layer):
...   # Now, all tensor inputs will be casted.
...   def call(self, inputs):
...     a, b = inputs
...     return a + 1., b + 1.
>>> a = tf.constant(1., dtype="float32")
>>> b = tf.constant(1., dtype="float32")
>>> layer = MyLayer(dtype="float64")
>>> x, y = layer((a, b))
>>> x.dtype
tf.float64
>>> y.dtype
tf.float64
```

Other arguments are not automatically casted for technical reasons, but this
may change in a future minor release.

The casting only occurs in TensorFlow 2, but can be enabled if
<a href="../../../../tf/compat/v1/disable_v2_behavior.md"><code>tf.compat.v1.disable_v2_behavior()</code></a> has been called with
<a href="../../../../tf/compat/v1/keras/layers/enable_v2_dtype_behavior.md"><code>tf.compat.v1.keras.layers.enable_v2_dtype_behavior()</code></a>.

A layer subclass can prevent its inputs from being autocasted by passing
`autocast=False` to the layer constructor. For example:

```
>>> class NonAutoCastingLayer(tf.keras.layers.Layer):
...   def __init__(self, **kwargs):
...     kwargs['autocast'] = False
...     super(NonAutoCastingLayer, self).__init__(**kwargs)
...   def call(self, inp):
...     return inp
>>> x = tf.ones((4, 4, 4, 4), dtype='float32')
>>> layer = NonAutoCastingLayer(dtype='float64')
>>> y = layer(x)  # Will not cast inputs to it's compute dtype of float64
>>> y.dtype
tf.float32
```

### How a layer uses its policy's variable dtype

The default dtype of variables created by <a href="../../../../tf/keras/layers/Layer.md#add_weight"><code>tf.keras.layers.Layer.add_weight</code></a>
is the layer's policy's variable dtype.

If a layer's compute and variable dtypes differ, `add_weight` will wrap
floating-point variables with a special wrapper called an `AutoCastVariable`.
This wrapper is identical to the original variable except it casts itself to
the layer's compute dtype when used within <a href="../../../../tf/keras/layers/Layer.md#call"><code>Layer.call</code></a>. Outside <a href="../../../../tf/keras/layers/Layer.md#call"><code>Layer.call</code></a>,
the variable is not casted.

A layer author can prevent a variable from being wrapped with an
`AutoCastVariable` by passing `experimental_autocast=False` to `add_weight`:

```
>>> class MyLayer(tf.keras.layers.Layer):
...  def build(self, input_shape):
...    self.x = self.add_weight('x')
...    self.y = self.add_weight('y', experimental_autocast=False)
>>> policy = tf.keras.mixed_precision.experimental.Policy('mixed_float16')
>>> layer = MyLayer(dtype=policy)
>>> layer.build((2, 2))
>>> layer.x
<AutoCastVariable 'x:0' shape=() dtype=float32 true_dtype=float32, numpy=...>
>>> layer.y
<tf.Variable 'y:0' shape=() dtype=float32, numpy=...>
```

Passing `experimental_autocast=False` is useful for layers which may
internally do some math in the variable dtype instead of the compute dtype.
For example, you may wish to compute variable statistics, such as mean and
variance, in the variable dtype.

### How to write a layer that supports mixed precision and float64.

For the most part, layers will automatically support mixed precision and
float64 without any additional work, due to the fact the base layer
automatically casts inputs, creates variables of the correct type, and in the
case of mixed precision, wraps variables with `AutoCastVariables`.

For example, this simple dense layer does not require any additional work to
support mixed precision or float64. Keras automatically casts the inputs and
variable to the appropriate dtype.

```
>>> class MyDense(tf.keras.layers.Layer):
...   def build(self, input_shape):
...     self.kernel = self.add_weight('kernel', (input_shape[-1], 10))
...   def call(self, inputs):
...     return tf.matmul(inputs, self.kernel)
```

```
>>> policy = tf.keras.mixed_precision.experimental.Policy('mixed_float16')
>>> layer = MyDense(dtype=policy)
>>> x = np.random.rand(10, 10)
>>> y = layer(x)
>>> y.dtype
tf.float16
```

The primary case where you need extra work to support mixed precision or
float64 is when you create a new tensor, such as with <a href="../../../../tf/ones.md"><code>tf.ones</code></a> or
<a href="../../../../tf/constant.md"><code>tf.constant</code></a>. In such cases, you must create the tensor of the correct dtype.
For example, suppose you modify the `MyDense` layer to add a random number to
the output using <a href="../../../../tf/random/normal.md"><code>tf.random.normal</code></a>. You must pass the input dtype to
<a href="../../../../tf/random/normal.md"><code>tf.random.normal</code></a> to ensure the dtypes match.

```
>>> class MyDense(tf.keras.layers.Layer):
...   def build(self, input_shape):
...     self.kernel = self.add_weight('kernel', (input_shape[-1], 10))
...   def call(self, inputs):
...     rand = tf.random.normal(shape=inputs.shape, dtype=inputs.dtype)
...     return tf.matmul(inputs, self.kernel) + rand
>>>
>>> layer = MyDense(dtype=policy)
>>> y = layer(x)
>>> y.dtype
tf.float16
```

If you did not pass `dtype=inputs.dtype` to <a href="../../../../tf/random/normal.md"><code>tf.random.normal</code></a>, a `TypeError`
would have occurred. This is because the dtype defaults to `"float32"`, so the
layer would only work if the inputs were float32.

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
A <a href="../../../../tf/mixed_precision/experimental/LossScale.md"><code>tf.mixed_precision.experimental.LossScale</code></a>, an int (which
uses a `FixedLossScale`), or the string "dynamic" (which uses a
`DynamicLossScale`). Defaults to using no loss scaling unless `name` is
"mixed_float16", in which case this defaults to "dynamic". Only
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

This is the dtype layers will do their computations in.

Note that even if the compute dtype is float16 or bfloat16, hardware devices
may not do individual adds, multiplies, and other fundamental operations in
[b]float16, but instead may do some of them in float32 for numeric
stability. The compute dtype is the dtype of the inputs and outputs of the
TensorFlow ops that the layer executes. Internally, many TensorFlow ops will
do certain internal calculations in float32, or some other device-internal
intermediate format with higher precision than [b]float16, to increase
numeric stability.

For example, a <a href="../../../../tf/keras/layers/Dense.md"><code>tf.keras.layers.Dense</code></a> layer, when run on a GPU with a
float16 compute dtype, will pass float16 inputs to tf.matmul. But, tf.matmul
will do use float32 intermediate math. The performance benefit of float16 is
still apparent, due to increased memory bandwidth and the fact modern GPUs
have specialized hardware for computing matmuls on float16 while still
keeping intermediate computations in float32.
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
`should_cast_variables`
</td>
<td>
Returns True if variables should be casted.

This is true if the variable dtype is not the same as the compute dtype.
</td>
</tr><tr>
<td>
`variable_dtype`
</td>
<td>
The variable dtype of this policy.

This is the dtype layers will create their variables in, unless a layer
explicitly chooses a different dtype. If this is different than
<a href="../../../../tf/keras/mixed_precision/experimental/Policy.md#compute_dtype"><code>Policy.compute_dtype</code></a>, Layers will cast variables to the compute dtype to
avoid type errors.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/mixed_precision/experimental/policy.py#L472-L478">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config, custom_objects=None
)
</code></pre>




<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/mixed_precision/experimental/policy.py#L461-L470">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>






