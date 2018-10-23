

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.layers.maxout

``` python
tf.contrib.layers.maxout(
    inputs,
    num_units,
    axis=-1,
    name=None
)
```



Defined in [`tensorflow/python/layers/maxout.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/layers/maxout.py).

Adds a maxout op from https://arxiv.org/abs/1302.4389

"Maxout Networks" Ian J. Goodfellow, David Warde-Farley, Mehdi Mirza, Aaron
Courville,
 Yoshua Bengio

 Usually the operation is performed in the filter/channel dimension. This can
 also be
 used after fully-connected layers to reduce number of features.

 Arguments:
 inputs: Tensor input
 num_units: Specifies how many features will remain after maxout in the `axis`
   dimension
       (usually channel). This must be multiple of number of `axis`.
 axis: The dimension where max pooling will be performed. Default is the
 last dimension.
 name: Optional scope for name_scope.

 Returns:
  A `Tensor` representing the results of the pooling operation.

 Raises:
  ValueError: if num_units is not multiple of number of features.