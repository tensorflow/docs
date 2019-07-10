page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.normal

Outputs random values from a normal distribution.

### Aliases:

* `tf.compat.v1.random.normal`
* `tf.compat.v1.random_normal`
* `tf.compat.v2.random.normal`
* `tf.random.normal`
* `tf.random_normal`

``` python
tf.random.normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.dtypes.float32,
    seed=None,
    name=None
)
```



Defined in [`python/ops/random_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/random_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output tensor.
* <b>`mean`</b>: A 0-D Tensor or Python value of type `dtype`. The mean of the normal
  distribution.
* <b>`stddev`</b>: A 0-D Tensor or Python value of type `dtype`. The standard deviation
  of the normal distribution.
* <b>`dtype`</b>: The type of the output.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distribution.
  See
  <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random normal values.
