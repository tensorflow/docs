page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Concatenate


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/Concatenate">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/merge.py#L356-L443">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Concatenate`

Layer that concatenates a list of inputs.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/Concatenate"><code>tf.compat.v1.keras.layers.Concatenate</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/Concatenate"><code>tf.compat.v2.keras.layers.Concatenate</code></a>


<!-- Placeholder for "Used in" -->

It takes as input a list of tensors,
all of the same shape except for the concatenation axis,
and returns a single tensor, the concatenation of all inputs.

#### Arguments:


* <b>`axis`</b>: Axis along which to concatenate.
* <b>`**kwargs`</b>: standard layer keyword arguments.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/merge.py#L368-L372">View source</a>

``` python
__init__(
    axis=-1,
    **kwargs
)
```
