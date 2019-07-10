page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Dot

## Class `Dot`

Layer that computes a dot product between samples in two tensors.



### Aliases:

* Class `tf.compat.v1.keras.layers.Dot`
* Class `tf.compat.v2.keras.layers.Dot`
* Class `tf.keras.layers.Dot`



Defined in [`python/keras/layers/merge.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/merge.py).

<!-- Placeholder for "Used in" -->

E.g. if applied to a list of two tensors `a` and `b` of shape
`(batch_size, n)`, the output will be a tensor of shape `(batch_size, 1)`
where each entry `i` will be the dot product between
`a[i]` and `b[i]`.

#### Arguments:


* <b>`axes`</b>: Integer or tuple of integers,
    axis or axes along which to take the dot product.
* <b>`normalize`</b>: Whether to L2-normalize samples along the
    dot product axis before taking the dot product.
    If set to True, then the output of the dot product
    is the cosine proximity between the two samples.
* <b>`**kwargs`</b>: Standard layer keyword arguments.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    axes,
    normalize=False,
    **kwargs
)
```






