

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.utils.mat2d_to_layer_params

``` python
mat2d_to_layer_params(
    vector_template,
    mat2d
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/utils.py).

Converts a canonical 2D matrix representation back to a vector.

#### Args:

* <b>`vector_template`</b>: A Tensor or pair of Tensors shaped like layer parameters.
* <b>`mat2d`</b>: A 2D Tensor with the same shape as the value of
      layer_params_to_mat2d(vector_template).


#### Returns:

A Tensor or pair of Tensors with the same coefficients as mat2d and the same
    shape as vector_template.