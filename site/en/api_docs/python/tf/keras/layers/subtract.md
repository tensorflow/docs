page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.subtract

Functional interface to the `Subtract` layer.

### Aliases:

* `tf.compat.v1.keras.layers.subtract`
* `tf.compat.v2.keras.layers.subtract`
* `tf.keras.layers.subtract`

``` python
tf.keras.layers.subtract(
    inputs,
    **kwargs
)
```



Defined in [`python/keras/layers/merge.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/merge.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`inputs`</b>: A list of input tensors (exactly 2).
* <b>`**kwargs`</b>: Standard layer keyword arguments.


#### Returns:

A tensor, the difference of the inputs.



#### Examples:



```python
    import keras

    input1 = keras.layers.Input(shape=(16,))
    x1 = keras.layers.Dense(8, activation='relu')(input1)
    input2 = keras.layers.Input(shape=(32,))
    x2 = keras.layers.Dense(8, activation='relu')(input2)
    subtracted = keras.layers.subtract([x1, x2])

    out = keras.layers.Dense(4)(subtracted)
    model = keras.models.Model(inputs=[input1, input2], outputs=out)
```