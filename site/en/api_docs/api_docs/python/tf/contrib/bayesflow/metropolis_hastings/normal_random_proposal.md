

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.metropolis_hastings.normal_random_proposal

``` python
normal_random_proposal(
    scale=1.0,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/metropolis_hastings_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/bayesflow/python/ops/metropolis_hastings_impl.py).

Returns a callable that adds a random normal tensor to the input.

This function returns a callable that accepts one `Tensor` argument of any
shape and a real data type (i.e. `tf.float32` or `tf.float64`). The callable
adds a sample from a normal distribution with the supplied standard deviation
and zero mean to its input argument (called the proposal point).
The callable returns a tuple with the proposal point as the first element.
The second element is identically `None`. It is included so the callable is
compatible with the expected signature of the proposal scheme argument in the
`metropolis_hastings` function. A value of `None` indicates that the
probability of going from the input point to the proposal point is equal to
the probability of going from the proposal point to the input point.

#### Args:

* <b>`scale`</b>: A positive `float` or a scalar tensor of any real dtype controlling
    the scale of the normal distribution.
* <b>`seed`</b>: `int` or None. The random seed for this `Op`. If `None`, no seed is
    applied.
* <b>`name`</b>: A string that sets the name for this `Op`.


#### Returns:

* <b>`proposal_fn`</b>: A callable accepting one float-like `Tensor` and returning a
  2-tuple. The first value in the tuple is a `Tensor` of the same shape and
  dtype as the input argument and the second element of the tuple is None.