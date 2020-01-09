page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.keras.initializers


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/initializers">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Keras initializer serialization / deserialization.

### Aliases:

* Module <a href="/api_docs/python/tf/keras/initializers"><code>tf.compat.v1.keras.initializers</code></a>


<!-- Placeholder for "Used in" -->


## Classes

[`class Constant`](../../tf/initializers/constant): Initializer that generates tensors with constant values.

[`class Identity`](../../tf/initializers/identity): Initializer that generates the identity matrix.

[`class Initializer`](../../tf/keras/initializers/Initializer): Initializer base class: all initializers inherit from this class.

[`class Ones`](../../tf/initializers/ones): Initializer that generates tensors initialized to 1.

[`class Orthogonal`](../../tf/initializers/orthogonal): Initializer that generates an orthogonal matrix.

[`class RandomNormal`](../../tf/keras/initializers/RandomNormal): Initializer that generates tensors with a normal distribution.

[`class RandomUniform`](../../tf/keras/initializers/RandomUniform): Initializer that generates tensors with a uniform distribution.

[`class TruncatedNormal`](../../tf/keras/initializers/TruncatedNormal): Initializer that generates a truncated normal distribution.

[`class VarianceScaling`](../../tf/initializers/variance_scaling): Initializer capable of adapting its scale to the shape of weights tensors.

[`class Zeros`](../../tf/zeros_initializer): Initializer that generates tensors initialized to 0.

[`class constant`](../../tf/initializers/constant): Initializer that generates tensors with constant values.

[`class glorot_normal`](../../tf/glorot_normal_initializer): The Glorot normal initializer, also called Xavier normal initializer.

[`class glorot_uniform`](../../tf/glorot_uniform_initializer): The Glorot uniform initializer, also called Xavier uniform initializer.

[`class identity`](../../tf/initializers/identity): Initializer that generates the identity matrix.

[`class normal`](../../tf/keras/initializers/RandomNormal): Initializer that generates tensors with a normal distribution.

[`class ones`](../../tf/initializers/ones): Initializer that generates tensors initialized to 1.

[`class orthogonal`](../../tf/initializers/orthogonal): Initializer that generates an orthogonal matrix.

[`class random_normal`](../../tf/keras/initializers/RandomNormal): Initializer that generates tensors with a normal distribution.

[`class random_uniform`](../../tf/keras/initializers/RandomUniform): Initializer that generates tensors with a uniform distribution.

[`class truncated_normal`](../../tf/keras/initializers/TruncatedNormal): Initializer that generates a truncated normal distribution.

[`class uniform`](../../tf/keras/initializers/RandomUniform): Initializer that generates tensors with a uniform distribution.

[`class zeros`](../../tf/zeros_initializer): Initializer that generates tensors initialized to 0.

## Functions

[`deserialize(...)`](../../tf/keras/initializers/deserialize): Return an `Initializer` object from its config.

[`get(...)`](../../tf/keras/initializers/get)

[`he_normal(...)`](../../tf/initializers/he_normal): He normal initializer.

[`he_uniform(...)`](../../tf/initializers/he_uniform): He uniform variance scaling initializer.

[`lecun_normal(...)`](../../tf/initializers/lecun_normal): LeCun normal initializer.

[`lecun_uniform(...)`](../../tf/initializers/lecun_uniform): LeCun uniform initializer.

[`serialize(...)`](../../tf/keras/initializers/serialize)
