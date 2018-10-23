

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.sparse_categorical_crossentropy

``` python
tf.keras.backend.sparse_categorical_crossentropy(
    target,
    output,
    from_logits=False
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/backend.py).

Categorical crossentropy with integer targets.

#### Arguments:

* <b>`target`</b>: An integer tensor.
* <b>`output`</b>: A tensor resulting from a softmax
        (unless `from_logits` is True, in which
        case `output` is expected to be the logits).
* <b>`from_logits`</b>: Boolean, whether `output` is the
        result of a softmax, or is a tensor of logits.


#### Returns:

Output tensor.