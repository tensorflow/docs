


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.sum_regularizer

### `tf.contrib.layers.sum_regularizer`

```
tf.contrib.layers.sum_regularizer(regularizer_list, scope=None)
```


See the guide: [Layers (contrib) > Regularizers](../../../../../api_guides/python/contrib.layers#Regularizers)

Returns a function that applies the sum of multiple regularizers.

#### Args:

* <b>`regularizer_list`</b>: A list of regularizers to apply.
* <b>`scope`</b>: An optional scope name


#### Returns:

  A function with signature `sum_reg(weights)` that applies the
  sum of all the input regularizers.

Defined in [`tensorflow/contrib/layers/python/layers/regularizers.py`](https://www.tensorflow.org/code/tensorflow/contrib/layers/python/layers/regularizers.py).

