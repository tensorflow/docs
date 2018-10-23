

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.placeholder

``` python
placeholder(
    shape=None,
    ndim=None,
    dtype=None,
    sparse=False,
    name=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Instantiates a placeholder tensor and returns it.

#### Arguments:

* <b>`shape`</b>: Shape of the placeholder
        (integer tuple, may include `None` entries).
* <b>`ndim`</b>: Number of axes of the tensor.
        At least one of {`shape`, `ndim`} must be specified.
        If both are specified, `shape` is used.
* <b>`dtype`</b>: Placeholder type.
* <b>`sparse`</b>: Boolean, whether the placeholder should have a sparse type.
* <b>`name`</b>: Optional name string for the placeholder.


#### Returns:

    Tensor instance (with Keras metadata included).

Examples:
```python
    >>> from keras import backend as K
    >>> input_ph = K.placeholder(shape=(2, 4, 5))
    >>> input_ph
    <tf.Tensor 'Placeholder_4:0' shape=(2, 4, 5) dtype=float32>
```