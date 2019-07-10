page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Dense

## Class `Dense`

Just your regular densely-connected NN layer.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Dense`
* Class `tf.compat.v2.keras.layers.Dense`
* Class `tf.keras.layers.Dense`



Defined in [`python/keras/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/core.py).

<!-- Placeholder for "Used in" -->

`Dense` implements the operation:
`output = activation(dot(input, kernel) + bias)`
where `activation` is the element-wise activation function
passed as the `activation` argument, `kernel` is a weights matrix
created by the layer, and `bias` is a bias vector created by the layer
(only applicable if `use_bias` is `True`).

Note: If the input to the layer has a rank greater than 2, then
it is flattened prior to the initial dot product with `kernel`.

#### Example:



```python
# as first layer in a sequential model:
model = Sequential()
model.add(Dense(32, input_shape=(16,)))
# now the model will take as input arrays of shape (*, 16)
# and output arrays of shape (*, 32)

# after the first layer, you don't need to specify
# the size of the input anymore:
model.add(Dense(32))
```

#### Arguments:


* <b>`units`</b>: Positive integer, dimensionality of the output space.
* <b>`activation`</b>: Activation function to use.
  If you don't specify anything, no activation is applied
  (ie. "linear" activation: `a(x) = x`).
* <b>`use_bias`</b>: Boolean, whether the layer uses a bias vector.
* <b>`kernel_initializer`</b>: Initializer for the `kernel` weights matrix.
* <b>`bias_initializer`</b>: Initializer for the bias vector.
* <b>`kernel_regularizer`</b>: Regularizer function applied to
  the `kernel` weights matrix.
* <b>`bias_regularizer`</b>: Regularizer function applied to the bias vector.
* <b>`activity_regularizer`</b>: Regularizer function applied to
  the output of the layer (its "activation")..
* <b>`kernel_constraint`</b>: Constraint function applied to
  the `kernel` weights matrix.
* <b>`bias_constraint`</b>: Constraint function applied to the bias vector.


#### Input shape:

N-D tensor with shape: `(batch_size, ..., input_dim)`.
The most common situation would be
a 2D input with shape `(batch_size, input_dim)`.



#### Output shape:

N-D tensor with shape: `(batch_size, ..., units)`.
For instance, for a 2D input with shape `(batch_size, input_dim)`,
the output would have shape `(batch_size, units)`.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    units,
    activation=None,
    use_bias=True,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    **kwargs
)
```






