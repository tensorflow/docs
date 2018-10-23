

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.metropolis_hastings.uniform_random_proposal

``` python
uniform_random_proposal(
    step_size=1.0,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/metropolis_hastings_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/bayesflow/python/ops/metropolis_hastings_impl.py).

Returns a callable that adds a random uniform tensor to the input.

This function returns a callable that accepts one `Tensor` argument of any
shape and a real data type (i.e. `tf.float32` or `tf.float64`). It adds a
sample from a random uniform distribution drawn from [-stepsize, stepsize]
to its input. It also returns the log of the ratio of the probability of
moving from the input point to the proposed point, but since this log ratio is
identically equal to 0 (because the probability of drawing a value `x` from
the symmetric uniform distribution is the same as the probability of drawing
`-x`), it simply returns None for the second element of the returned tuple.

#### Args:

* <b>`step_size`</b>: A positive `float` or a scalar tensor of real dtype
    controlling the scale of the uniform distribution.
    If step_size = a, then draws are made uniformly from [-a, a].
* <b>`seed`</b>: `int` or None. The random seed for this `Op`. If `None`, no seed is
    applied.
* <b>`name`</b>: A string that sets the name for this `Op`.


#### Returns:

* <b>`proposal_fn`</b>:  A callable accepting one float-like `Tensor` and returning a
  2-tuple. The first value in the tuple is a `Tensor` of the same shape and
  dtype as the input argument and the second element of the tuple is None.