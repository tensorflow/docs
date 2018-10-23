

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.features.tensor_pool

``` python
tf.contrib.gan.features.tensor_pool(
    input_values,
    pool_size=50,
    pooling_probability=0.5,
    name='tensor_pool'
)
```



Defined in [`tensorflow/contrib/gan/python/features/python/random_tensor_pool_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/gan/python/features/python/random_tensor_pool_impl.py).

Queue storing input values and returning random previously stored ones.

Every time the returned `output_value` is evaluated, `input_value` is
evaluated and its value either directly returned (with
`1-pooling_probability`) or stored in the pool and a random one of the samples
currently in the pool is popped and returned. As long as the pool in not fully
filled, the input_value is always directly returned, as well as stored in the
pool. Note during inference / testing, it may be appropriate to set
`pool_size` = 0 or `pooling_probability` = 0.

#### Args:

* <b>`input_values`</b>: A `Tensor`, or a list or tuple of `Tensor`s from which to read
    values to be pooled.
* <b>`pool_size`</b>: An integer specifying the maximum size of the pool. Defaults to
    50.
* <b>`pooling_probability`</b>: A float `Tensor` specifying the probability of getting
    a value from the pool, as opposed to just the current input.
* <b>`name`</b>: A string prefix for the name scope for all tensorflow ops.


#### Returns:

A `Tensor`, or a list or tuple of `Tensor`s (according to the type ofx
`input_values`) which is with given probability either the `input_values` or
a randomly chosen sample that was previously inserted in the pool.


#### Raises:

* <b>`ValueError`</b>: If `pool_size` is negative.