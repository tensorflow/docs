

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.bayesflow.monte_carlo

### Module `tf.contrib.bayesflow.monte_carlo`



Defined in [`tensorflow/contrib/bayesflow/python/ops/monte_carlo.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/bayesflow/python/ops/monte_carlo.py).

Monte Carlo integration and helpers.

See the [BayesFlow Monte Carlo (contrib)](../../../../../api_guides/python/contrib.bayesflow.monte_carlo) guide.

## Functions

[`expectation(...)`](../../../tf/contrib/bayesflow/monte_carlo/expectation): Monte Carlo estimate of an expectation:  `E_p[f(Z)]` with sample mean.

[`expectation_importance_sampler(...)`](../../../tf/contrib/bayesflow/monte_carlo/expectation_importance_sampler): Monte Carlo estimate of `E_p[f(Z)] = E_q[f(Z) p(Z) / q(Z)]`.

[`expectation_importance_sampler_logspace(...)`](../../../tf/contrib/bayesflow/monte_carlo/expectation_importance_sampler_logspace): Importance sampling with a positive function, in log-space.

