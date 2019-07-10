page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.maxout

``` python
tf.contrib.layers.maxout(
    inputs,
    num_units,
    axis=-1,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/layers/python/layers/layers.py).

Adds a maxout op from https://arxiv.org/abs/1302.4389

"Maxout Networks" Ian J. Goodfellow, David Warde-Farley, Mehdi Mirza, Aaron
Courville,
 Yoshua Bengio

Usually the operation is performed in the filter/channel dimension. This can
also be
used after fully-connected layers to reduce number of features.

#### Arguments:

* <b>`inputs`</b>: Tensor input
* <b>`num_units`</b>: Specifies how many features will remain after maxout
    in the `axis` dimension (usually channel).
    This must be a factor of number of features.
* <b>`axis`</b>: The dimension where max pooling will be performed. Default is the
  last dimension.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

A `Tensor` representing the results of the pooling operation.


#### Raises:

* <b>`ValueError`</b>: if num_units is not multiple of number of features.