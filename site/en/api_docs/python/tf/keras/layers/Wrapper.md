page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Wrapper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/Wrapper">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/wrappers.py#L39-L86">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Wrapper`

Abstract wrapper base class.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/Wrapper"><code>tf.compat.v1.keras.layers.Wrapper</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/Wrapper"><code>tf.compat.v2.keras.layers.Wrapper</code></a>


<!-- Placeholder for "Used in" -->

Wrappers take another layer and augment it in various ways.
Do not use this class as a layer, it is only an abstract base class.
Two usable wrappers are the `TimeDistributed` and `Bidirectional` wrappers.

#### Arguments:


* <b>`layer`</b>: The layer to be wrapped.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/wrappers.py#L50-L57">View source</a>

``` python
__init__(
    layer,
    **kwargs
)
```
