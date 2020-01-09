page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.variable

``` python
tf.keras.backend.variable(
    value,
    dtype=None,
    name=None,
    constraint=None
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/backend.py).

Instantiates a variable and returns it.

#### Arguments:

* <b>`value`</b>: Numpy array, initial value of the tensor.
* <b>`dtype`</b>: Tensor type.
* <b>`name`</b>: Optional name string for the tensor.
* <b>`constraint`</b>: Optional projection function to be
        applied to the variable after an optimizer update.


#### Returns:

    A variable instance (with Keras metadata included).

Examples:
```python
    >>> from keras import backend as K
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val, dtype='float64', name='example_var')
    >>> K.dtype(kvar)
    'float64'
    >>> print(kvar)
    example_var
    >>> kvar.eval()
    array([[ 1.,  2.],
           [ 3.,  4.]])
```