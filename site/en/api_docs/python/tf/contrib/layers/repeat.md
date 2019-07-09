

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.repeat

``` python
tf.contrib.layers.repeat(
    inputs,
    repetitions,
    layer,
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/layers/python/layers/layers.py).

See the guide: [Layers (contrib) > Higher level ops for building neural network layers](../../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers)

Applies the same layer with the same arguments repeatedly.

```python
  y = repeat(x, 3, conv2d, 64, [3, 3], scope='conv1')
  # It is equivalent to:

  x = conv2d(x, 64, [3, 3], scope='conv1/conv1_1')
  x = conv2d(x, 64, [3, 3], scope='conv1/conv1_2')
  y = conv2d(x, 64, [3, 3], scope='conv1/conv1_3')
```

If the `scope` argument is not given in `kwargs`, it is set to
`layer.__name__`, or `layer.func.__name__` (for `functools.partial`
objects). If neither `__name__` nor `func.__name__` is available, the
layers are called with `scope='stack'`.

#### Args:

* <b>`inputs`</b>: A `Tensor` suitable for layer.
* <b>`repetitions`</b>: Int, number of repetitions.
* <b>`layer`</b>: A layer with arguments `(inputs, *args, **kwargs)`
* <b>`*args`</b>: Extra args for the layer.
* <b>`**kwargs`</b>: Extra kwargs for the layer.


#### Returns:

A tensor result of applying the layer, repetitions times.

#### Raises:

* <b>`ValueError`</b>: If the op is unknown or wrong.