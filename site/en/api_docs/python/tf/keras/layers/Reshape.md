page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Reshape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L376-L476">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Reshape`

Reshapes an output to a certain shape.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Reshape`
* Class `tf.compat.v2.keras.layers.Reshape`


### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)

### Used in the tutorials:

* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)




#### Arguments:


* <b>`target_shape`</b>: Target shape. Tuple of integers,
  does not include the samples dimension (batch size).


#### Input shape:

Arbitrary, although all dimensions in the input shaped must be fixed.
Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

`(batch_size,) + target_shape`



#### Example:



```python
# as first layer in a Sequential model
model = Sequential()
model.add(Reshape((3, 4), input_shape=(12,)))
# now: model.output_shape == (None, 3, 4)
# note: `None` is the batch dimension

# as intermediate layer in a Sequential model
model.add(Reshape((6, 2)))
# now: model.output_shape == (None, 6, 2)

# also supports shape inference using `-1` as dimension
model.add(Reshape((-1, 2, 2)))
# now: model.output_shape == (None, None, 2, 2)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L411-L413">View source</a>

``` python
__init__(
    target_shape,
    **kwargs
)
```
