page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.nn.alpha_dropout

``` python
tf.contrib.nn.alpha_dropout(
    x,
    keep_prob,
    noise_shape=None,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/contrib/nn/python/ops/alpha_dropout.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/nn/python/ops/alpha_dropout.py).

Computes alpha dropout.

Alpha Dropout is a dropout that maintains the self-normalizing property. For
an input with zero mean and unit standard deviation, the output of
Alpha Dropout maintains the original mean and standard deviation of the input.

See [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)

#### Args:

* <b>`x`</b>: A tensor.
* <b>`keep_prob`</b>: A scalar `Tensor` with the same type as x. The probability
    that each element is kept.
* <b>`noise_shape`</b>: A 1-D `Tensor` of type `int32`, representing the
    shape for randomly generated keep/drop flags.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    <a href="../../../tf/set_random_seed"><code>tf.set_random_seed</code></a> for behavior.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A Tensor of the same shape of `x`.


#### Raises:

* <b>`ValueError`</b>: If `keep_prob` is not in `(0, 1]`.