

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.nn.zero_fraction

### `tf.nn.zero_fraction`

``` python
zero_fraction(
    value,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/nn_impl.py).

Returns the fraction of zeros in `value`.

If `value` is empty, the result is `nan`.

This is useful in summaries to measure and report sparsity.  For example,

```python
    z = tf.Relu(...)
    summ = tf.contrib.deprecated.scalar_summary('sparsity',
    tf.nn.zero_fraction(z))
```

#### Args:

* <b>`value`</b>: A tensor of numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  The fraction of zeros in `value`, with type `float32`.