page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Permute


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/Permute">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L480-L534">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Permute`

Permutes the dimensions of the input according to a given pattern.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/Permute"><code>tf.compat.v1.keras.layers.Permute</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/Permute"><code>tf.compat.v2.keras.layers.Permute</code></a>


<!-- Placeholder for "Used in" -->

Useful for e.g. connecting RNNs and convnets together.

#### Example:



```python
model = Sequential()
model.add(Permute((2, 1), input_shape=(10, 64)))
# now: model.output_shape == (None, 64, 10)
# note: `None` is the batch dimension
```

#### Arguments:


* <b>`dims`</b>: Tuple of integers. Permutation pattern, does not include the
  samples dimension. Indexing starts at 1.
  For instance, `(2, 1)` permutes the first and second dimensions
  of the input.


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same as the input shape, but with the dimensions re-ordered according
to the specified pattern.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/core.py#L510-L518">View source</a>

``` python
__init__(
    dims,
    **kwargs
)
```
