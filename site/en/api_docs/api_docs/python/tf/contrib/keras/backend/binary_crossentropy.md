

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.binary_crossentropy

``` python
binary_crossentropy(
    output,
    target,
    from_logits=False
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Binary crossentropy between an output tensor and a target tensor.

#### Arguments:

    output: A tensor.
    target: A tensor with the same shape as `output`.
    from_logits: Whether `output` is expected to be a logits tensor.
        By default, we consider that `output`
        encodes a probability distribution.


#### Returns:

    A tensor.