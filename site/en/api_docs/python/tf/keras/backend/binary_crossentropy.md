

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.binary_crossentropy

``` python
tf.keras.backend.binary_crossentropy(
    target,
    output,
    from_logits=False
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/backend.py).

Binary crossentropy between an output tensor and a target tensor.

#### Arguments:

* <b>`target`</b>: A tensor with the same shape as `output`.
* <b>`output`</b>: A tensor.
* <b>`from_logits`</b>: Whether `output` is expected to be a logits tensor.
        By default, we consider that `output`
        encodes a probability distribution.


#### Returns:

A tensor.