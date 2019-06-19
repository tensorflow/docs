page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.squeeze

``` python
tf.keras.backend.squeeze(
    x,
    axis
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Removes a 1-dimension from the tensor at index "axis".

#### Arguments:

* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: Axis to drop.


#### Returns:

A tensor with the same data as `x` but reduced dimensions.