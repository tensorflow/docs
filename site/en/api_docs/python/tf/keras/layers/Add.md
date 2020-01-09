page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Add


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/Add">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/merge.py#L222-L249">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Add`

Layer that adds a list of inputs.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/Add"><code>tf.compat.v1.keras.layers.Add</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/Add"><code>tf.compat.v2.keras.layers.Add</code></a>


<!-- Placeholder for "Used in" -->

It takes as input a list of tensors,
all of the same shape, and returns
a single tensor (also of the same shape).

#### Examples:



```python
    import keras

    input1 = keras.layers.Input(shape=(16,))
    x1 = keras.layers.Dense(8, activation='relu')(input1)
    input2 = keras.layers.Input(shape=(32,))
    x2 = keras.layers.Dense(8, activation='relu')(input2)
    # equivalent to `added = keras.layers.add([x1, x2])`
    added = keras.layers.Add()([x1, x2])
    out = keras.layers.Dense(4)(added)
    model = keras.models.Model(inputs=[input1, input2], outputs=out)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/merge.py#L41-L43">View source</a>

``` python
__init__(**kwargs)
```
