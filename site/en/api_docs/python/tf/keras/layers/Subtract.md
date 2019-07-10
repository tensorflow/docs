page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Subtract

## Class `Subtract`

Layer that subtracts two inputs.



### Aliases:

* Class `tf.compat.v1.keras.layers.Subtract`
* Class `tf.compat.v2.keras.layers.Subtract`
* Class `tf.keras.layers.Subtract`



Defined in [`python/keras/layers/merge.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/merge.py).

<!-- Placeholder for "Used in" -->

It takes as input a list of tensors of size 2,
both of the same shape, and returns a single tensor, (inputs[0] - inputs[1]),
also of the same shape.

#### Examples:



```python
    import keras

    input1 = keras.layers.Input(shape=(16,))
    x1 = keras.layers.Dense(8, activation='relu')(input1)
    input2 = keras.layers.Input(shape=(32,))
    x2 = keras.layers.Dense(8, activation='relu')(input2)
    # Equivalent to subtracted = keras.layers.subtract([x1, x2])
    subtracted = keras.layers.Subtract()([x1, x2])

    out = keras.layers.Dense(4)(subtracted)
    model = keras.models.Model(inputs=[input1, input2], outputs=out)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(**kwargs)
```






