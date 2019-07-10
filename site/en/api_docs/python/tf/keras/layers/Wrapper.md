page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Wrapper

## Class `Wrapper`

Abstract wrapper base class.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.Wrapper`
* Class `tf.compat.v2.keras.layers.Wrapper`
* Class `tf.keras.layers.Wrapper`



Defined in [`python/keras/layers/wrappers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/wrappers.py).

<!-- Placeholder for "Used in" -->

Wrappers take another layer and augment it in various ways.
Do not use this class as a layer, it is only an abstract base class.
Two usable wrappers are the `TimeDistributed` and `Bidirectional` wrappers.

#### Arguments:


* <b>`layer`</b>: The layer to be wrapped.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    layer,
    **kwargs
)
```






