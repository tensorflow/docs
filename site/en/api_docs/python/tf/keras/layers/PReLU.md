page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.PReLU


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/advanced_activations.py#L72-L158">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `PReLU`

Parametric Rectified Linear Unit.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.PReLU`
* Class `tf.compat.v2.keras.layers.PReLU`


<!-- Placeholder for "Used in" -->


#### It follows:


`f(x) = alpha * x for x < 0`,
`f(x) = x for x >= 0`,
where `alpha` is a learned array with the same shape as x.

#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as the input.



#### Arguments:


* <b>`alpha_initializer`</b>: Initializer function for the weights.
* <b>`alpha_regularizer`</b>: Regularizer for the weights.
* <b>`alpha_constraint`</b>: Constraint for the weights.
* <b>`shared_axes`</b>: The axes along which to share learnable
  parameters for the activation function.
  For example, if the incoming feature maps
  are from a 2D convolution
  with output shape `(batch, height, width, channels)`,
  and you wish to share parameters across space
  so that each filter only has one set of parameters,
  set `shared_axes=[1, 2]`.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/advanced_activations.py#L102-L118">View source</a>

``` python
__init__(
    alpha_initializer='zeros',
    alpha_regularizer=None,
    alpha_constraint=None,
    shared_axes=None,
    **kwargs
)
```
