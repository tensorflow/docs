page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.normalize_batch_in_training

``` python
tf.keras.backend.normalize_batch_in_training(
    x,
    gamma,
    beta,
    reduction_axes,
    epsilon=0.001
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py).

Computes mean and std for batch then apply batch_normalization on batch.

#### Arguments:

* <b>`x`</b>: Input tensor or variable.
* <b>`gamma`</b>: Tensor by which to scale the input.
* <b>`beta`</b>: Tensor with which to center the input.
* <b>`reduction_axes`</b>: iterable of integers,
        axes over which to normalize.
* <b>`epsilon`</b>: Fuzz factor.


#### Returns:

A tuple length of 3, `(normalized_tensor, mean, variance)`.