page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.RepeatVector


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L614-L654">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RepeatVector`

Repeats the input n times.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.RepeatVector`
* Class `tf.compat.v2.keras.layers.RepeatVector`


<!-- Placeholder for "Used in" -->


#### Example:



```python
model = Sequential()
model.add(Dense(32, input_dim=32))
# now: model.output_shape == (None, 32)
# note: `None` is the batch dimension

model.add(RepeatVector(3))
# now: model.output_shape == (None, 3, 32)
```

#### Arguments:


* <b>`n`</b>: Integer, repetition factor.


#### Input shape:

2D tensor of shape `(num_samples, features)`.



#### Output shape:

3D tensor of shape `(num_samples, n, features)`.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/core.py#L639-L642">View source</a>

``` python
__init__(
    n,
    **kwargs
)
```
