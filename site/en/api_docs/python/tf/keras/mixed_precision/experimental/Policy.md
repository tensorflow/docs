page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.mixed_precision.experimental.Policy

## Class `Policy`

A mixed precision policy for a Keras layer.



### Aliases:

* Class `tf.compat.v1.keras.mixed_precision.experimental.Policy`
* Class `tf.compat.v2.keras.mixed_precision.experimental.Policy`
* Class `tf.keras.mixed_precision.experimental.Policy`



Defined in [`python/keras/mixed_precision/experimental/policy.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/mixed_precision/experimental/policy.py).

<!-- Placeholder for "Used in" -->

A mixed precision policy determines the floating-point dtype that Keras layers
should create variables in. For non-default policies, if the variable dtype
does not match the input dtype, variables will automatically be casted to the
input dtype to avoid type errors. Policies can be passed to the 'dtype'
argument of layer constructors, or a global policy can be set with
'set_policy'.

In the near future, policies will also determine the computation dtype of
layers, as well as the loss scaling algorithm.

Policies are intended to enable mixed precision training, which require using
float32 variables and [b]float16 computations for most layers. The term "mixed
precision" refers to the use of both float16 (or bfloat16) and float32 in a
model. See https://arxiv.org/abs/1710.03740 for more information on mixed
precision training.

Policies are constructed by passing a string to the `name` constructor
argument. `name` determines the behavior of the policy. Currently, `name` can
be one of the following values.

  * 'infer': Infer the variable and computation dtypes from the input dtype.
    This is the default behavior.
  * 'infer_float32_vars': Infer the computation dtypes from the input
    dtype, but create variables in float32. Variables will be casted to the
    computation dtype. This is intended to enable mixed precision. Users can
    cast tensors to float16 before passing them to a layer, which causes the
    layer to run it's computation in float16 while keeping variables in
    float32.

To use mixed precision in a model, the 'infer_float32_vars' policy can be used
alongside float16 input tensors, which results in float16 computations and
float32 variables. For example:

```python
tf.keras.mixed_precision.experimental.set_policy('infer_float32_vars')
model = tf.keras.models.Sequential(
    tf.keras.layers.Input((100,), dtype='float16'),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Lambda(lambda x: tf.cast(x, 'float32')),
    tf.keras.layers.Activation('Softmax')
)
```

Alternatively, the policy can be passed to individual layers instead of
setting the global policy with `set_policy`:

```python
policy = tf.keras.mixed_precision.experimental.Policy('infer_float32_vars')
model = tf.keras.models.Sequential(
    tf.keras.layers.Input((100,), dtype='float16'),
    tf.keras.layers.Dense(10, dtype=policy),
    tf.keras.layers.Dense(10, dtype=policy),
    tf.keras.layers.Lambda(lambda x: tf.cast(x, 'float32')),
    tf.keras.layers.Activation('Softmax')
)
```

Note that a LossScaleOptimizer should also be used for mixed precision models
to avoid numerical underflow. See `LossScaleOptimizer`.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(name)
```






## Properties

<h3 id="default_variable_dtype"><code>default_variable_dtype</code></h3>

Returns the default variable dtype of this policy.

This is the dtype layers will create their variables in, unless a layer
explicit chooses a different dtype. Layers will cast variables to the
appropriate dtype to avoid type errors.

#### Returns:

The default variable dtype of this policy, or None if the default variable
dtype should be derived from the inputs.


<h3 id="name"><code>name</code></h3>

Returns the name of the policy: "infer" or "infer_float32_vars.


<h3 id="should_cast_variables"><code>should_cast_variables</code></h3>

Returns true if variables should be casted.




