page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.zero_fraction

### Aliases:

* `tf.math.zero_fraction`
* `tf.nn.zero_fraction`

``` python
tf.math.zero_fraction(
    value,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/nn_impl.py).

Returns the fraction of zeros in `value`.

If `value` is empty, the result is `nan`.

This is useful in summaries to measure and report sparsity.  For example,

```python
    z = tf.nn.relu(...)
    summ = tf.summary.scalar('sparsity', tf.nn.zero_fraction(z))
```

#### Args:

* <b>`value`</b>: A tensor of numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The fraction of zeros in `value`, with type `float32`.