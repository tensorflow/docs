page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Lambda


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L658-L919">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Lambda`

Wraps arbitrary expressions as a `Layer` object.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Lambda`
* Class `tf.compat.v2.keras.layers.Lambda`


<!-- Placeholder for "Used in" -->

The `Lambda` layer exists so that arbitrary TensorFlow functions
can be used when constructing `Sequential` and Functional API
models. `Lambda` layers are best suited for simple operations or
quick experimentation. For more advanced use cases, subclassing
<a href="../../../tf/keras/layers/Layer"><code>keras.layers.Layer</code></a> is preferred. One reason for this is that
when saving a Model, `Lambda` layers are saved by serializing the
Python bytecode, whereas subclassed Layers are saved via overriding
their `get_config` method and are thus more portable. Models that rely
on subclassed Layers are also often easier to visualize and reason
about.

#### Examples:



```python
# add a x -> x^2 layer
model.add(Lambda(lambda x: x ** 2))
```

```python
# add a layer that returns the concatenation
# of the positive part of the input and
# the opposite of the negative part

def antirectifier(x):
    x -= K.mean(x, axis=1, keepdims=True)
    x = K.l2_normalize(x, axis=1)
    pos = K.relu(x)
    neg = K.relu(-x)
    return K.concatenate([pos, neg], axis=1)

model.add(Lambda(antirectifier))
```

Variables can be created within a `Lambda` layer. Like with
other layers, these variables will be created only once and reused
if the `Lambda` layer is called on new inputs. If creating more
than one variable in a given `Lambda` instance, be sure to use
a different name for each variable. Note that calling sublayers
from within a `Lambda` is not supported.

Example of variable creation:

```python
def linear_transform(x):
  v1 = tf.Variable(1., name='multiplier')
  v2 = tf.Variable(0., name='bias')
  return x*v1 + v2

linear_layer = Lambda(linear_transform)
model.add(linear_layer)
model.add(keras.layers.Dense(10, activation='relu'))
model.add(linear_layer)  # Reuses existing Variables
```

Note that creating two instances of `Lambda` using the same function
will *not* share Variables between the two instances. Each instance of
`Lambda` will create and manage its own weights.

#### Arguments:


* <b>`function`</b>: The function to be evaluated. Takes input tensor as first
  argument.
* <b>`output_shape`</b>: Expected output shape from function. This argument can be
  inferred if not explicitly provided. Can be a tuple or function. If a
  tuple, it only specifies the first dimension onward;
  sample dimension is assumed either the same as the input: `output_shape =
    (input_shape[0], ) + output_shape` or, the input is `None` and
  the sample dimension is also `None`: `output_shape = (None, ) +
    output_shape` If a function, it specifies the entire shape as a function
    of the
  input shape: `output_shape = f(input_shape)`
* <b>`mask`</b>: Either None (indicating no masking) or a callable with the same
  signature as the `compute_mask` layer method, or a tensor that will be
  returned as output mask regardless what the input is.
* <b>`arguments`</b>: Optional dictionary of keyword arguments to be passed to the
  function.
Input shape: Arbitrary. Use the keyword argument input_shape (tuple of
  integers, does not include the samples axis) when using this layer as the
  first layer in a model.
Output shape: Specified by `output_shape` argument

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L741-L757">View source</a>

``` python
__init__(
    function,
    output_shape=None,
    mask=None,
    arguments=None,
    **kwargs
)
```
