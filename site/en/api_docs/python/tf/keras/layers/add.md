

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.layers.add

``` python
tf.keras.layers.add(
    inputs,
    **kwargs
)
```



Defined in [`tensorflow/python/keras/_impl/keras/layers/merge.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/layers/merge.py).

Functional interface to the `Add` layer.

#### Arguments:

* <b>`inputs`</b>: A list of input tensors (at least 2).
* <b>`**kwargs`</b>: Standard layer keyword arguments.


#### Returns:

    A tensor, the sum of the inputs.

Examples:

```python
    import keras

    input1 = keras.layers.Input(shape=(16,))
    x1 = keras.layers.Dense(8, activation='relu')(input1)
    input2 = keras.layers.Input(shape=(32,))
    x2 = keras.layers.Dense(8, activation='relu')(input2)
    added = keras.layers.add([x1, x2])

    out = keras.layers.Dense(4)(added)
    model = keras.models.Model(inputs=[input1, input2], outputs=out)
```