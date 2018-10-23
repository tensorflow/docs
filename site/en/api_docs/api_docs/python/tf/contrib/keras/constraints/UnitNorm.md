

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.constraints.UnitNorm

## Class `UnitNorm`

Inherits From: [`Constraint`](../../../../tf/contrib/keras/constraints/Constraint)

### Aliases:

* Class `tf.contrib.keras.constraints.UnitNorm`
* Class `tf.contrib.keras.constraints.unit_norm`



Defined in [`tensorflow/contrib/keras/python/keras/constraints.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/constraints.py).

Constrains the weights incident to each hidden unit to have unit norm.

#### Arguments:

    axis: integer, axis along which to calculate weight norms.
        For instance, in a `Dense` layer the weight matrix
        has shape `(input_dim, output_dim)`,
        set `axis` to `0` to constrain each weight vector
        of length `(input_dim,)`.
        In a `Conv2D` layer with `data_format="channels_last"`,
        the weight tensor has shape
        `(rows, cols, input_depth, output_depth)`,
        set `axis` to `[0, 1, 2]`
        to constrain the weights of each filter tensor of size
        `(rows, cols, input_depth)`.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(axis=0)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(w)
```



<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```





