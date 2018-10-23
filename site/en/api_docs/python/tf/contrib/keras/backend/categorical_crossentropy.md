

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.categorical_crossentropy

### `tf.contrib.keras.backend.categorical_crossentropy`

``` python
categorical_crossentropy(
    output,
    target,
    from_logits=False
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Categorical crossentropy between an output tensor and a target tensor.

#### Arguments:

    output: A tensor resulting from a softmax
        (unless `from_logits` is True, in which
        case `output` is expected to be the logits).
    target: A tensor of the same shape as `output`.
    from_logits: Boolean, whether `output` is the
        result of a softmax, or is a tensor of logits.


#### Returns:

    Output tensor.