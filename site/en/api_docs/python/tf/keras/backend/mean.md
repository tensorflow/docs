page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.mean

``` python
tf.keras.backend.mean(
    x,
    axis=None,
    keepdims=False
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py).

Mean of a tensor, alongside the specified axis.

#### Arguments:

* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: A list of integer. Axes to compute the mean.
* <b>`keepdims`</b>: A boolean, whether to keep the dimensions or not.
        If `keepdims` is `False`, the rank of the tensor is reduced
        by 1 for each entry in `axis`. If `keepdims` is `True`,
        the reduced dimensions are retained with length 1.


#### Returns:

A tensor with the mean of elements of `x`.