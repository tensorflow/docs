page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.LayerNormalization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/normalization.py#L874-L1046">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LayerNormalization`

Layer normalization layer (Ba et al., 2016).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.LayerNormalization`
* Class `tf.compat.v2.keras.layers.LayerNormalization`


### Used in the tutorials:

* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



Normalize the activations of the previous layer for each given example in a
batch independently, rather than across a batch like Batch Normalization.
i.e. applies a transformation that maintains the mean activation within each
example close to 0 and the activation standard deviation close to 1.

#### Arguments:


* <b>`axis`</b>: Integer or List/Tuple. The axis that should be normalized
  (typically the features axis).
* <b>`epsilon`</b>: Small float added to variance to avoid dividing by zero.
* <b>`center`</b>: If True, add offset of `beta` to normalized tensor.
    If False, `beta` is ignored.
* <b>`scale`</b>: If True, multiply by `gamma`.
  If False, `gamma` is not used.
  When the next layer is linear (also e.g. <a href="../../../tf/nn/relu"><code>nn.relu</code></a>),
  this can be disabled since the scaling
  will be done by the next layer.
* <b>`beta_initializer`</b>: Initializer for the beta weight.
* <b>`gamma_initializer`</b>: Initializer for the gamma weight.
* <b>`beta_regularizer`</b>: Optional regularizer for the beta weight.
* <b>`gamma_regularizer`</b>: Optional regularizer for the gamma weight.
* <b>`beta_constraint`</b>: Optional constraint for the beta weight.
* <b>`gamma_constraint`</b>: Optional constraint for the gamma weight.
* <b>`trainable`</b>: Boolean, if `True` the variables will be marked as trainable.


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.



#### References:

- [Layer Normalization](https://arxiv.org/abs/1607.06450)


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/normalization.py#L913-L947">View source</a>

``` python
__init__(
    axis=-1,
    epsilon=0.001,
    center=True,
    scale=True,
    beta_initializer='zeros',
    gamma_initializer='ones',
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
    trainable=True,
    name=None,
    **kwargs
)
```
