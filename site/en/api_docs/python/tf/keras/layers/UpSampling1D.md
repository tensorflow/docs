page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.UpSampling1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional.py#L1881-L1913">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `UpSampling1D`

Upsampling layer for 1D inputs.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.UpSampling1D`
* Class `tf.compat.v2.keras.layers.UpSampling1D`


<!-- Placeholder for "Used in" -->

Repeats each temporal step `size` times along the time axis.

#### Arguments:


* <b>`size`</b>: Integer. Upsampling factor.


#### Input shape:

3D tensor with shape: `(batch, steps, features)`.



#### Output shape:

3D tensor with shape: `(batch, upsampled_steps, features)`.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional.py#L1896-L1899">View source</a>

``` python
__init__(
    size=2,
    **kwargs
)
```
