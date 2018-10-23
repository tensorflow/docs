

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.hmc.sample_chain

``` python
tf.contrib.bayesflow.hmc.sample_chain(
    num_results,
    target_log_prob_fn,
    current_state,
    step_size,
    num_leapfrog_steps,
    num_burnin_steps=0,
    num_steps_between_results=0,
    seed=None,
    current_target_log_prob=None,
    current_grads_target_log_prob=None,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/hmc_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/bayesflow/python/ops/hmc_impl.py).

Runs multiple iterations of one or more Hamiltonian Monte Carlo chains.

Hamiltonian Monte Carlo (HMC) is a Markov chain Monte Carlo (MCMC) algorithm
that takes a series of gradient-informed steps to produce a Metropolis
proposal. This function samples from an HMC Markov chain at `current_state`
and whose stationary distribution has log-unnormalized-density
`target_log_prob_fn()`.

This function samples from multiple chains in parallel. It assumes that the
the leftmost dimensions of (each) `current_state` (part) index an independent
chain.  The function `target_log_prob_fn()` sums log-probabilities across
event dimensions (i.e., current state (part) rightmost dimensions). Each
element of the output of `target_log_prob_fn()` represents the (possibly
unnormalized) log-probability of the joint distribution over (all) the current
state (parts).

The `current_state` can be represented as a single `Tensor` or a `list` of
`Tensors` which collectively represent the current state. When specifying a
`list`, one must also specify a list of `step_size`s.

Note: `target_log_prob_fn` is called exactly twice.

Since HMC states are correlated, it is sometimes desirable to produce
additional intermediate states, and then discard them, ending up with a set of
states with decreased autocorrelation.  See [1].  Such "thinning" is made
possible by setting `num_steps_between_results > 0`.  The chain then takes
`num_steps_between_results` extra steps between the steps that make it into
the results.  The extra steps are never materialized (in calls to `sess.run`),
and thus do not increase memory requirements.

[1]: "Statistically efficient thinning of a Markov chain sampler."
     Art B. Owen. April 2017.
     http://statweb.stanford.edu/~owen/reports/bestthinning.pdf

#### Examples:

##### Sample from a diagonal-variance Gaussian.

```python
tfd = tf.contrib.distributions

def make_likelihood(true_variances):
  return tfd.MultivariateNormalDiag(
      scale_diag=tf.sqrt(true_variances))

dims = 10
dtype = np.float32
true_variances = tf.linspace(dtype(1), dtype(3), dims)
likelihood = make_likelihood(true_variances)

states, kernel_results = hmc.sample_chain(
    num_results=1000,
    target_log_prob_fn=likelihood.log_prob,
    current_state=tf.zeros(dims),
    step_size=0.5,
    num_leapfrog_steps=2,
    num_burnin_steps=500)

# Compute sample stats.
sample_mean = tf.reduce_mean(states, axis=0)
sample_var = tf.reduce_mean(
    tf.squared_difference(states, sample_mean),
    axis=0)
```

##### Sampling from factor-analysis posteriors with known factors.

I.e.,

```none
for i=1..n:
  w[i] ~ Normal(0, eye(d))            # prior
  x[i] ~ Normal(loc=matmul(w[i], F))  # likelihood
```

where `F` denotes factors.

```python
tfd = tf.contrib.distributions

def make_prior(dims, dtype):
  return tfd.MultivariateNormalDiag(
      loc=tf.zeros(dims, dtype))

def make_likelihood(weights, factors):
  return tfd.MultivariateNormalDiag(
      loc=tf.tensordot(weights, factors, axes=[[0], [-1]]))

# Setup data.
num_weights = 10
num_factors = 4
num_chains = 100
dtype = np.float32

prior = make_prior(num_weights, dtype)
weights = prior.sample(num_chains)
factors = np.random.randn(num_factors, num_weights).astype(dtype)
x = make_likelihood(weights, factors).sample(num_chains)

def target_log_prob(w):
  # Target joint is: `f(w) = p(w, x | factors)`.
  return prior.log_prob(w) + make_likelihood(w, factors).log_prob(x)

# Get `num_results` samples from `num_chains` independent chains.
chains_states, kernels_results = hmc.sample_chain(
    num_results=1000,
    target_log_prob_fn=target_log_prob,
    current_state=tf.zeros([num_chains, dims], dtype),
    step_size=0.1,
    num_leapfrog_steps=2,
    num_burnin_steps=500)

# Compute sample stats.
sample_mean = tf.reduce_mean(chains_states, axis=[0, 1])
sample_var = tf.reduce_mean(
    tf.squared_difference(chains_states, sample_mean),
    axis=[0, 1])
```

#### Args:

* <b>`num_results`</b>: Integer number of Markov chain draws.
* <b>`target_log_prob_fn`</b>: Python callable which takes an argument like
    `current_state` (or `*current_state` if it's a list) and returns its
    (possibly unnormalized) log-density under the target distribution.
* <b>`current_state`</b>: `Tensor` or Python `list` of `Tensor`s representing the
    current state(s) of the Markov chain(s). The first `r` dimensions index
    independent chains, `r = tf.rank(target_log_prob_fn(*current_state))`.
* <b>`step_size`</b>: `Tensor` or Python `list` of `Tensor`s representing the step size
    for the leapfrog integrator. Must broadcast with the shape of
    `current_state`. Larger step sizes lead to faster progress, but too-large
    step sizes make rejection exponentially more likely. When possible, it's
    often helpful to match per-variable step sizes to the standard deviations
    of the target distribution in each variable.
* <b>`num_leapfrog_steps`</b>: Integer number of steps to run the leapfrog integrator
    for. Total progress per HMC step is roughly proportional to `step_size *
    num_leapfrog_steps`.
* <b>`num_burnin_steps`</b>: Integer number of chain steps to take before starting to
    collect results.
    Default value: 0 (i.e., no burn-in).
* <b>`num_steps_between_results`</b>: Integer number of chain steps between collecting
    a result. Only one out of every `num_steps_between_samples + 1` steps is
    included in the returned results.  The number of returned chain states is
    still equal to `num_results`.  Default value: 0 (i.e., no thinning).
* <b>`seed`</b>: Python integer to seed the random number generator.
* <b>`current_target_log_prob`</b>: (Optional) `Tensor` representing the value of
    `target_log_prob_fn` at the `current_state`. The only reason to specify
    this argument is to reduce TF graph size.
    Default value: `None` (i.e., compute as needed).
* <b>`current_grads_target_log_prob`</b>: (Optional) Python list of `Tensor`s
    representing gradient of `target_log_prob` at the `current_state` and wrt
    the `current_state`. Must have same shape as `current_state`. The only
    reason to specify this argument is to reduce TF graph size.
    Default value: `None` (i.e., compute as needed).
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.
    Default value: `None` (i.e., "hmc_sample_chain").


#### Returns:

* <b>`next_states`</b>: Tensor or Python list of `Tensor`s representing the
    state(s) of the Markov chain(s) at each result step. Has same shape as
    input `current_state` but with a prepended `num_results`-size dimension.
* <b>`kernel_results`</b>: `collections.namedtuple` of internal calculations used to
    advance the chain.