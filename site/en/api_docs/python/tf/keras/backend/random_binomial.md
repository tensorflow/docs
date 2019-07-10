page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.random_binomial

Returns a tensor with random binomial distribution of values.

### Aliases:

* `tf.compat.v1.keras.backend.random_binomial`
* `tf.compat.v2.keras.backend.random_binomial`
* `tf.keras.backend.random_binomial`

``` python
tf.keras.backend.random_binomial(
    shape,
    p=0.0,
    dtype=None,
    seed=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

The binomial distribution with parameters `n` and `p` is the probability
distribution of the number of successful Bernoulli process. Only supports
`n` = 1 for now.

#### Arguments:


* <b>`shape`</b>: A tuple of integers, the shape of tensor to create.
* <b>`p`</b>: A float, `0. <= p <= 1`, probability of binomial distribution.
* <b>`dtype`</b>: String, dtype of returned tensor.
* <b>`seed`</b>: Integer, random seed.


#### Returns:

A tensor.
