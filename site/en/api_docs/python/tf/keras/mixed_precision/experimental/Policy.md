page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.mixed_precision.experimental.Policy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/mixed_precision/experimental/Policy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/mixed_precision/experimental/policy.py#L39-L313">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Policy`

A dtype policy for a Keras layer.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/mixed_precision/experimental/Policy"><code>tf.compat.v1.keras.mixed_precision.experimental.Policy</code></a>
* Class <a href="/api_docs/python/tf/keras/mixed_precision/experimental/Policy"><code>tf.compat.v2.keras.mixed_precision.experimental.Policy</code></a>


<!-- Placeholder for "Used in" -->

A dtype policy determines dtype-related aspects of a layer, such as its
computation and variable dtypes. Each layer has a policy. Policies can be
passed to the 'dtype' argument of layer constructors, or a global policy can
be set with 'tf.keras.mixed_precision.experimental.set_policy'. A layer will
default to the global policy if no policy is passed to it's constructor.

For most models, each layer will have the same computation dtype and variable
dtype, which will typically be float32. However, when mixed precision
training is used, most layers will instead have a float16 computation dtype
and a float32 variable dtype. See [this
link](https://docs.nvidia.com/deeplearning/sdk/mixed-precision-training/index.html)
for more information on mixed precision training. When the variable dtype does
not match the computation dtype, variables will be automatically casted to the
computation dtype to avoid type errors.

Policies also have a <a href="../../../../tf/train/experimental/LossScale"><code>tf.train.experimental.LossScale</code></a> instance, which is used
by Models to performance loss scaling. Layers which are not Models ignore
the loss scale.

Policies are constructed by passing a string to the constructor, e.g.
`tf.keras.mixed_precision.experimental.Policy('float32')`. The string
determines the compute and variable dtypes. Currently, it can be one of
in one of the following forms:

  * Any dtype name, such as 'float32' or 'float64'. Both the variable and
    compute dtypes will be that dtype.
  * '<dtype>_with_float32_vars', where <dtype> is any dtype. The compute dtype
    will be <dtype>, while the variable dtype is float32. This can be used for
    mixed precision, which uses float16 or bfloat16 for most computations, and
    float32 for variables, but it is recommended to use the 'mixed_float16' or
    'mixed_bfloat16' policies instead.
  * 'mixed_float16' or 'mixed_bfloat16': Similar to
    'float16_with_float32_vars' or 'bfloat16_with_float32_vars' respectively.
    'mixed_float16' is identical to 'float16_with_float32_vars' except the
    loss_scale is dynamic by default. 'mixed_bfloat16' is currently identical
    to 'bfloat16_with_float32_vars'. More changes may be added to these mixed
    policies in the future, to further differentiate them from
    [b]float16_with_float32_vars.

### How to use mixed precision in layers with Policies

To use mixed precision in a model, the 'mixed_float16' policy can
be used. <a href="../../../../tf/keras/mixed_precision/experimental/set_policy"><code>tf.keras.mixed_precision.experimental.set_policy</code></a> can be used to set
the default policy for layers if no policy is passed to them. For example:

```python
tf.keras.mixed_precision.experimental.set_policy('mixed_float16')
model = tf.keras.models.Sequential(
    tf.keras.layers.Input((100,)),
    # Dense layers use global policy of 'mixed_float16', which does
    # computations in float16 while keeping variables in float32.
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(10),
    # Softmax should be done in float32 for numeric stability. We pass
    # dtype='float32' to use float32 instead of the global policy.
    tf.keras.layers.Activation('Softmax', dtype='float32')
)
model.fit(...)  # Train `model`
```

Alternatively, the policy can be passed to individual layers instead of
setting the global policy with `set_policy`:

```python
policy = tf.keras.mixed_precision.experimental.Policy('mixed_float16')
model = tf.keras.models.Sequential(
    tf.keras.layers.Input((100,)),
    tf.keras.layers.Dense(10, dtype=policy),
    tf.keras.layers.Dense(10, dtype=policy),
    # Softmax should be done in float32 for numeric stability.
    tf.keras.layers.Activation('Softmax', dtype='float32')
)
model.fit(...)  # Train `model`
```

As the above example shows, strings can be directly passed to layer
constructors in the `dtype` argument instead of policies, but only if the
string is convertible to a dtype.

### The deprecated "infer" policy

In addition to a dtype or "<dtype>_with_float32_vars", a policy can also be
"infer". This Policy is deprecated, and it is not recommended. When a layer
has an infer policy, it will infer the computation and variable dtype from
the first input the first time the layer is called.

Once the layer is called for the first time, the layer's policy will change to
the dtype of the first input.

Similarly to "infer", there is a deprecated "infer_with_float32_vars" policy
that infers the compute dtype, but not the variable dtype.

In TensorFlow 1, only the "infer" and "infer_with_float32_vars" policies are
available.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/mixed_precision/experimental/policy.py#L140-L195">View source</a>

``` python
__init__(
    name,
    loss_scale=USE_DEFAULT
)
```

Constructs the policy.

The `name` argument determines the compute and variable dtype, and has no
additional effect on the Policy. The compute and variable dtypes can only be
specified through `name`, and cannot be specified directly.

#### Args:


* <b>`name`</b>: A string. Can be one of the following values:
  * Any dtype name, such as 'float32' or 'float64'. Both the variable and
    compute dtypes will be that dtype.
  * '<dtype>_with_float32_vars', where <dtype> is any dtype. The compute
    dtype will be <dtype>, while the variable dtype is float32. This can
    be used for mixed precision, which uses float16 or bfloat16 for most
    computations, and float32 for variables, but it is recommended to use
    the 'mixed_float16' or 'mixed_bfloat16' policies instead.
  * 'mixed_float16' or 'mixed_bfloat16': Similar to
    'float16_with_float32_vars' or 'bfloat16_with_float32_vars'
    respectively. 'mixed_float16' is identical to
    'float16_with_float32_vars' except the loss_scale is dynamic by
    default. 'mixed_bfloat16' is currently identical to
    'bfloat16_with_float32_vars'. More changes may be added to these mixed
    policies in the future, to further differentiate them from
    [b]float16_with_float32_vars.
  * 'infer' or 'infer_with_float32_vars' (deprecated): Infer the
    computation dtype from the input dtype.
* <b>`loss_scale`</b>: A <a href="../../../../tf/train/experimental/LossScale"><code>tf.train.experimental.LossScale</code></a>, or a value convertible to
  one such as "dynamic". Defaults to using no loss scaling unless `name`
  is "mixed_float16", in which case this defaults to "dynamic". Only
  <a href="../../../../tf/keras/Model"><code>tf.keras.Model</code></a>s, not layers, use the loss scale, and it is only used
  during <a href="../../../../tf/keras/Model#fit"><code>Model.fit</code></a> or <a href="../../../../tf/keras/Model#train_on_batch"><code>Model.train_on_batch</code></a>.



## Properties

<h3 id="compute_dtype"><code>compute_dtype</code></h3>

The compute dtype of this policy.

This is the dtype layers will do their computations in.

If this is None, the policy is "infer" or "infer_with_float32_vars" and
`variable_dtype` is either None or float32 respectively.

Note that even if the compute dtype is float16 or bfloat16, hardware devices
may not do individual adds, multiplies, and other fundamental operations in
[b]float16, but instead may do some of them in float32 for numeric
stability. The compute dtype is the dtype of the inputs and outputs of the
TensorFlow ops that the layer executes. Internally, many TensorFlow ops will
do certain internal calculations in float32, or some other device-internal
intermediate format with higher precision than [b]float16, to increase
numeric stability.

For example, a <a href="../../../../tf/keras/layers/Dense"><code>tf.keras.layers.Dense</code></a> layer, when run on a GPU with a
float16 compute dtype, will pass float16 inputs to tf.matmul. But, tf.matmul
will do use float32 intermediate math. The performance benefit of float16 is
still apparent, due to increased memory bandwidth and the fact GPUs have
specialized hardware for computating matmuls on float16 while still keeping
intermediate computations in float32.

#### Returns:

The variable dtype of this policy, or None if the variable dtype should be
inferred from the inputs.


<h3 id="loss_scale"><code>loss_scale</code></h3>

Returns the loss scale of this Policy.


#### Returns:

A <a href="../../../../tf/train/experimental/LossScale"><code>tf.train.experimental.LossScale</code></a>, or None.


<h3 id="name"><code>name</code></h3>

Returns the name of this policy.


<h3 id="should_cast_variables"><code>should_cast_variables</code></h3>

Returns True if variables should be casted.

This is true if the variable dtype is not the same as the compute dtype.

#### Returns:

True, if variables should be casted.


<h3 id="variable_dtype"><code>variable_dtype</code></h3>

The variable dtype of this policy.

This is the dtype layers will create their variables in, unless a layer
explicit chooses a different dtype. If this is different than
<a href="../../../../tf/keras/mixed_precision/experimental/Policy#compute_dtype"><code>Policy.compute_dtype</code></a> and both are non-None, Layers will cast variables to
the compute dtype to avoid type errors.

If this is None, the policy is "infer" and the `compute_dtype` is also None.
If `compute_dtype` is None, this is either None or float32.

#### Returns:

The variable dtype of this policy, or None if the variable dtype should be
inferred from the inputs.
