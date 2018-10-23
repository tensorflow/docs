

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.bayesflow.stochastic_gradient_estimators

### Module `tf.contrib.bayesflow.stochastic_gradient_estimators`



Defined in [`tensorflow/contrib/bayesflow/python/ops/stochastic_gradient_estimators.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/bayesflow/python/ops/stochastic_gradient_estimators.py).

Stochastic gradient estimators.

These functions are meant to be used in conjunction with `StochasticTensor`
(`loss_fn` parameter) and `surrogate_loss`.

See Gradient Estimation Using Stochastic Computation Graphs
(http://arxiv.org/abs/1506.05254) by Schulman et al., eq. 1 and section 4, for
mathematical details.

## Score function estimator

The score function is an unbiased estimator of the gradient of `E_p(x)[f(x)]`,
where `f(x)` can be considered to be a "loss" term. It is computed as
`E_p(x)[f(x) grad(log p(x))]`. A constant `b`, referred to here as the
"baseline", can be subtracted from `f(x)` without affecting the expectation. The
term `(f(x) - b)` is referred to here as the "advantage".

Note that the methods defined in this module actually compute the integrand of
the score function, such that when taking the gradient, the true score function
is computed.


## Baseline functions

Baselines reduce the variance of Monte Carlo estimate of an expectation. The
baseline for a stochastic node can be a function of all non-influenced nodes
(see section 4 of Schulman et al., linked above). Baselines are also known as
"control variates."

In the context of a MC estimate of `E_p(x)[f(x) - b]`, baseline functions have
the signature `(st, fx) => Tensor`, where `st` is a `StochasticTensor` backed by
the distribution `p(x)` and `fx` is the influenced loss.


