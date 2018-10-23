

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.cast

``` python
tf.keras.backend.cast(
    x,
    dtype
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/backend.py).

Casts a tensor to a different dtype and returns it.

You can cast a Keras variable but it still returns a Keras tensor.

#### Arguments:

* <b>`x`</b>: Keras tensor (or variable).
* <b>`dtype`</b>: String, either (`'float16'`, `'float32'`, or `'float64'`).


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