

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.placeholder

### `tf.contrib.keras.backend.placeholder`

``` python
placeholder(
    shape=None,
    ndim=None,
    dtype=None,
    sparse=False,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Instantiates a placeholder tensor and returns it.

#### Arguments:

    shape: Shape of the placeholder
        (integer tuple, may include `None` entries).
    ndim: Number of axes of the tensor.
        At least one of {`shape`, `ndim`} must be specified.
        If both are specified, `shape` is used.
    dtype: Placeholder type.
    sparse: Boolean, whether the placeholder should have a sparse type.
    name: Optional name string for the placeholder.


#### Returns:

    Tensor instance (with Keras metadata included).

Examples:
```python
    >>> from keras import backend as K
    >>> input_ph = K.placeholder(shape=(2, 4, 5))
    >>> input_ph
    <tf.Tensor 'Placeholder_4:0' shape=(2, 4, 5) dtype=float32>
```