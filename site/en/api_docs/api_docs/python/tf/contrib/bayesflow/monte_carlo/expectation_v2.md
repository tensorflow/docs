

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.monte_carlo.expectation_v2

``` python
expectation_v2(
    f,
    samples,
    log_prob=None,
    use_reparametrization=True,
    axis=0,
    keep_dims=False,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/monte_carlo_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/bayesflow/python/ops/monte_carlo_impl.py).

Computes the Monte-Carlo approximation of `E_p[f(X)]`.

This function computes the Monte-Carlo approximation of an expectation, i.e.,

```none
E_p[f(X)] approx= m**-1 sum_i^m f(x_j),  x_j ~iid p(X)
```

where:

- `x_j = samples[j, ...]`,
- `log(p(samples)) = log_prob(samples)` and
- `m = prod(shape(samples)[axis])`.

Tricks: Reparameterization and Score-Gradient

When p is "reparameterized", i.e., a diffeomorphic transformation of a
parameterless distribution (e.g.,
`Normal(Y; m, s) <=> Y = sX + m, X ~ Normal(0,1)`), we can swap gradient and
expectation, i.e.,
`grad[ Avg{ s_i : i=1...n } ] = Avg{ grad[s_i] : i=1...n }` where
`S_n = Avg{s_i}` and `s_i = f(x_i), x_i ~ p`.

However, if p is not reparameterized, TensorFlow's gradient will be incorrect
since the chain-rule stops at samples of unreparameterized distributions. In
this circumstance using the Score-Gradient trick results in an unbiased
gradient, i.e.,

```none
grad[ E_p[f(X)] ]
= grad[ int dx p(x) f(x) ]
= int dx grad[ p(x) f(x) ]
= int dx [ p'(x) f(x) + p(x) f'(x) ]
= int dx p(x) [p'(x) / p(x) f(x) + f'(x) ]
= int dx p(x) grad[ f(x) p(x) / stop_grad[p(x)] ]
= E_p[ grad[ f(x) p(x) / stop_grad[p(x)] ] ]
```

Unless p is not reparametrized, it is usually preferable to
`use_reparametrization = True`.

Warning: users are responsible for verifying `p` is a "reparameterized"
distribution.

#### Args:

* <b>`f`</b>: Python callable which can return `f(samples)`.
* <b>`samples`</b>: `Tensor` of samples used to form the Monte-Carlo approximation of
    `E_p[f(X)]`.  A batch of samples should be indexed by `axis` dimensions.
* <b>`log_prob`</b>: Python callable which can return `log_prob(samples)`. Must
    correspond to the natural-logarithm of the pdf/pmf of each sample. Only
    required/used if `use_reparametrization=False`.
* <b>`use_reparametrization`</b>: Python `bool` indicating that the approximation
    should use the fact that the gradient of samples is unbiased.
* <b>`axis`</b>: The dimensions to average. If `None` (the default), averages all
    dimensions.
* <b>`keep_dims`</b>: If true, retains averaged dimensions with length 1.
* <b>`name`</b>: A `name_scope` for operations created by this function (optional).
    Default value: "expectation_v2".


#### Returns:

* <b>`approx_expectation`</b>: `Tensor` corresponding to the Monte-Carlo approximation
    of `E_p[f(X)]`.


#### Raises:

* <b>`ValueError`</b>: if `f` is not `callable`.
* <b>`ValueError`</b>: if `use_reparametrization=False` and `log_prob` is not
    `callable`.