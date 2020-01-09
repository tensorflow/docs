page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.InputLayer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/InputLayer">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/input_layer.py#L33-L159">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `InputLayer`

Layer to be used as an entry point into a Network (a graph of layers).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/InputLayer"><code>tf.compat.v1.keras.layers.InputLayer</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/InputLayer"><code>tf.compat.v2.keras.layers.InputLayer</code></a>


<!-- Placeholder for "Used in" -->

It can either wrap an existing tensor (pass an `input_tensor` argument)
or create a placeholder tensor (pass arguments `input_shape`, and
optionally, `dtype`).

It is generally recommend to use the functional layer API via `Input`,
(which creates an `InputLayer`) without directly using `InputLayer`.

This class can create placeholders for tf.Tensors, tf.SparseTensors, and
tf.RaggedTensors by choosing 'sparse=True' or 'ragged=True'.

#### Arguments:


* <b>`input_shape`</b>: Shape tuple (not including the batch axis), or `TensorShape`
  instance (not including the batch axis).
* <b>`batch_size`</b>: Optional input batch size (integer or None).
* <b>`dtype`</b>: Datatype of the input.
* <b>`input_tensor`</b>: Optional tensor to use as layer input
    instead of creating a placeholder.
* <b>`sparse`</b>: Boolean, whether the placeholder created is meant to be sparse.
* <b>`ragged`</b>: Boolean, whether the placeholder created is meant to be ragged.
    In this case, values of 'None' in the 'shape' argument represent
    ragged dimensions. For more information about RaggedTensors, see
    https://www.tensorflow.org/guide/ragged_tensors.
* <b>`name`</b>: Name of the layer (string).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/input_layer.py#L61-L149">View source</a>

``` python
__init__(
    input_shape=None,
    batch_size=None,
    dtype=None,
    input_tensor=None,
    sparse=False,
    name=None,
    ragged=False,
    **kwargs
)
```
