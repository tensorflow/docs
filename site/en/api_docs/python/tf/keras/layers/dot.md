

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.dot

``` python
tf.keras.layers.dot(
    inputs,
    axes,
    normalize=False,
    **kwargs
)
```



Defined in [`tensorflow/python/keras/_impl/keras/layers/merge.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/layers/merge.py).

Functional interface to the `Dot` layer.

#### Arguments:

* <b>`inputs`</b>: A list of input tensors (at least 2).
* <b>`axes`</b>: Integer or tuple of integers,
        axis or axes along which to take the dot product.
* <b>`normalize`</b>: Whether to L2-normalize samples along the
        dot product axis before taking the dot product.
        If set to True, then the output of the dot product
        is the cosine proximity between the two samples.
* <b>`**kwargs`</b>: Standard layer keyword arguments.


#### Returns:

A tensor, the dot product of the samples from the inputs.