

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.in_top_k

### `tf.contrib.keras.backend.in_top_k`

``` python
in_top_k(
    predictions,
    targets,
    k
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Returns whether the `targets` are in the top `k` `predictions`.

#### Arguments:

    predictions: A tensor of shape `(batch_size, classes)` and type `float32`.
    targets: A 1D tensor of length `batch_size` and type `int32` or `int64`.
    k: An `int`, number of top elements to consider.


#### Returns:

    A 1D tensor of length `batch_size` and type `bool`.
    `output[i]` is `True` if `predictions[i, targets[i]]` is within top-`k`
    values of `predictions[i]`.