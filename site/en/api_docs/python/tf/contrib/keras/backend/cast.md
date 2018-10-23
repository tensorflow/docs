

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.cast

### `tf.contrib.keras.backend.cast`

``` python
cast(
    x,
    dtype
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Casts a tensor to a different dtype and returns it.

You can cast a Keras variable but it still returns a Keras tensor.

#### Arguments:

    x: Keras tensor (or variable).
    dtype: String, either (`'float16'`, `'float32'`, or `'float64'`).


#### Returns:

    Keras tensor with dtype `dtype`.

Example:
```python
    >>> from keras import backend as K
    >>> input = K.placeholder((2, 3), dtype='float32')
    >>> input
    <tf.Tensor 'Placeholder_2:0' shape=(2, 3) dtype=float32>
    # It doesn't work in-place as below.
    >>> K.cast(input, dtype='float16')
    <tf.Tensor 'Cast_1:0' shape=(2, 3) dtype=float16>
    >>> input
    <tf.Tensor 'Placeholder_2:0' shape=(2, 3) dtype=float32>
    # you need to assign it.
    >>> input = K.cast(input, dtype='float16')
    >>> input
    <tf.Tensor 'Cast_2:0' shape=(2, 3) dtype=float16>
```