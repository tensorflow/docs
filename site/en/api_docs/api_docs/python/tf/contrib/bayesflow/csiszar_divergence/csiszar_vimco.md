

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.csiszar_divergence.csiszar_vimco

``` python
csiszar_vimco(
    f,
    p_log_prob,
    q,
    num_draws,
    num_batch_draws=1,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py).

Use VIMCO to lower the variance of gradient[csiszar_function(Avg(logu))].

This function generalizes "Variational Inference for Monte Carlo Objectives"
(VIMCO), i.e., https://arxiv.org/abs/1602.06725, to Csiszar f-Divergences.

Note: if `q.reparameterization_type = distribution.FULLY_REPARAMETERIZED`,
consider using `monte_carlo_csiszar_f_divergence`.

The VIMCO loss is:

```none
vimco = f(Avg{logu[i] : i=0,...,m-1})
where,
  logu[i] = log( p(x, h[i]) / q(h[i] | x) )
  h[i] iid~ q(H | x)
```

Interestingly, the VIMCO gradient is not the naive gradient of `vimco`.
Rather, it is characterized by:

```none
grad[vimco] - variance_reducing_term
where,
  variance_reducing_term = Sum{ grad[log q(h[i] | x)] *
                                  (vimco - f(log Avg{h[j;i] : j=0,...,m-1}))
                               : i=0, ..., m-1 }
  h[j;i] = { u[j]                             j!=i
           { GeometricAverage{ u[k] : k!=i}   j==i
```

(We omitted `stop_gradient` for brevity. See implementation for more details.)

The `Avg{h[j;i] : j}` term is a kind of "swap-out average" where the `i`-th
element has been replaced by the leave-`i`-out Geometric-average.

This implementation prefers numerical precision over efficiency, i.e.,
`O(num_draws * num_batch_draws * prod(batch_shape) * prod(event_shape))`.
(The constant may be fairly large, perhaps around 12.)

#### Args:

* <b>`f`</b>: Python `callable` representing a Csiszar-function in log-space.
* <b>`p_log_prob`</b>: Python `callable` representing the natural-log of the
    probability under distribution `p`. (In variational inference `p` is the
    joint distribution.)
* <b>`q`</b>: `tf.Distribution`-like instance; must implement: `sample(n, seed)`, and
    `log_prob(x)`. (In variational inference `q` is the approximate posterior
    distribution.)
* <b>`num_draws`</b>: Integer scalar number of draws used to approximate the
    f-Divergence expectation.
* <b>`num_batch_draws`</b>: Integer scalar number of draws used to approximate the
    f-Divergence expectation.
* <b>`seed`</b>: Python `int` seed for `q.sample`.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.


#### Returns:

* <b>`vimco`</b>: The Csiszar f-Divergence generalized VIMCO objective.


#### Raises:

* <b>`ValueError`</b>: if `num_draws < 2`.