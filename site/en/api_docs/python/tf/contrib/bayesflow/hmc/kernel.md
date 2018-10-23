

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.hmc.kernel

``` python
tf.contrib.bayesflow.hmc.kernel(
    target_log_prob_fn,
    current_state,
    step_size,
    num_leapfrog_steps,
    seed=None,
    current_target_log_prob=None,
    current_grads_target_log_prob=None,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/hmc_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/bayesflow/python/ops/hmc_impl.py).

Runs one iteration of Hamiltonian Monte Carlo.

Hamiltonian Monte Carlo (HMC) is a Markov chain Monte Carlo (MCMC)
algorithm that takes a series of gradient-informed steps to produce
a Metropolis proposal. This function applies one step of HMC to
randomly update the variable `x`.

This function can update multiple chains in parallel. It assumes that all
leftmost dimensions of `current_state` index independent chain states (and are
therefore updated independently). The output of `target_log_prob_fn()` should
sum log-probabilities across all event dimensions. Slices along the rightmost
dimensions may have different target distributions; for example,
`current_state[0, :]` could have a different target distribution from
`current_state[1, :]`. This is up to `target_log_prob_fn()`. (The number of
independent chains is `tf.size(target_log_prob_fn(*current_state))`.)

#### Examples:

##### Simple chain with warm-up.

```python
tfd = tf.contrib.distributions

# Tuning acceptance rates:
dtype = np.float32
target_accept_rate = 0.631
num_warmup_iter = 500
num_chain_iter = 500

x = tf.get_variable(name="x", initializer=dtype(1))
step_size = tf.get_variable(name="step_size", initializer=dtype(1))

target = tfd.Normal(loc=dtype(0), scale=dtype(1))

next_x, other_results = hmc.kernel(
    target_log_prob_fn=target.log_prob,
    current_state=x,
    step_size=step_size,
    num_leapfrog_steps=3)[:4]

x_update = x.assign(next_x)

step_size_update = step_size.assign_add(
    step_size * tf.where(
        tf.exp(tf.minimum(other_results.log_accept_ratio), 0.) >
            target_accept_rate,
        0.01, -0.01))

warmup = tf.group([x_update, step_size_update])

tf.global_variables_initializer().run()

sess.graph.finalize()  # No more graph building.

# Warm up the sampler and adapt the step size
for _ in xrange(num_warmup_iter):
  sess.run(warmup)

# Collect samples without adapting step size
samples = np.zeros([num_chain_iter])
for i in xrange(num_chain_iter):
  _, x_, target_log_prob_, grad_ = sess.run([
      x_update,
      x,
      other_results.target_log_prob,
      other_results.grads_target_log_prob])
  samples[i] = x_

print(samples.mean(), samples.std())
```

##### Sample from more complicated posterior.

I.e.,

```none
  W ~ MVN(loc=0, scale=sigma * eye(dims))
  for i=1...num_samples:
      X[i] ~ MVN(loc=0, scale=eye(dims))
    eps[i] ~ Normal(loc=0, scale=1)
      Y[i] = X[i].T * W + eps[i]
```

```python
tfd = tf.contrib.distributions

def make_training_data(num_samples, dims, sigma):
  dt = np.asarray(sigma).dtype
  zeros = tf.zeros(dims, dtype=dt)
  x = tfd.MultivariateNormalDiag(
      loc=zeros).sample(num_samples, seed=1)
  w = tfd.MultivariateNormalDiag(
      loc=zeros,
      scale_identity_multiplier=sigma).sample(seed=2)
  noise = tfd.Normal(
      loc=dt(0),
      scale=dt(1)).sample(num_samples, seed=3)
  y = tf.tensordot(x, w, axes=[[1], [0]]) + noise
  return y, x, w

def make_prior(sigma, dims):
  # p(w | sigma)
  return tfd.MultivariateNormalDiag(
      loc=tf.zeros([dims], dtype=sigma.dtype),
      scale_identity_multiplier=sigma)

def make_likelihood(x, w):
  # p(y | x, w)
  return tfd.MultivariateNormalDiag(
      loc=tf.tensordot(x, w, axes=[[1], [0]]))

# Setup assumptions.
dtype = np.float32
num_samples = 150
dims = 10
num_iters = int(5e3)

true_sigma = dtype(0.5)
y, x, true_weights = make_training_data(num_samples, dims, true_sigma)

# Estimate of `log(true_sigma)`.
log_sigma = tf.get_variable(name="log_sigma", initializer=dtype(0))
sigma = tf.exp(log_sigma)

# State of the Markov chain.
weights = tf.get_variable(
    name="weights",
    initializer=np.random.randn(dims).astype(dtype))

prior = make_prior(sigma, dims)

def joint_log_prob_fn(w):
  # f(w) = log p(w, y | x)
  return prior.log_prob(w) + make_likelihood(x, w).log_prob(y)

weights_update = weights.assign(
    hmc.kernel(target_log_prob_fn=joint_log_prob,
               current_state=weights,
               step_size=0.1,
               num_leapfrog_steps=5)[0])

with tf.control_dependencies([weights_update]):
  loss = -prior.log_prob(weights)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
log_sigma_update = optimizer.minimize(loss, var_list=[log_sigma])

sess.graph.finalize()  # No more graph building.

tf.global_variables_initializer().run()

sigma_history = np.zeros(num_iters, dtype)
weights_history = np.zeros([num_iters, dims], dtype)

for i in xrange(num_iters):
  _, sigma_, weights_, _ = sess.run([log_sigma_update, sigma, weights])
  weights_history[i, :] = weights_
  sigma_history[i] = sigma_

true_weights_ = sess.run(true_weights)

# Should converge to something close to true_sigma.
plt.plot(sigma_history);
plt.ylabel("sigma");
plt.xlabel("iteration");
```

#### Args:

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
* <b>`seed`</b>: Python integer to seed the random number generator.
* <b>`current_target_log_prob`</b>: (Optional) `Tensor` representing the value of
    `target_log_prob_fn` at the `current_state`. The only reason to
    specify this argument is to reduce TF graph size.
    Default value: `None` (i.e., compute as needed).
* <b>`current_grads_target_log_prob`</b>: (Optional) Python list of `Tensor`s
    representing gradient of `current_target_log_prob` at the `current_state`
    and wrt the `current_state`. Must have same shape as `current_state`. The
    only reason to specify this argument is to reduce TF graph size.
    Default value: `None` (i.e., compute as needed).
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.
    Default value: `None` (i.e., "hmc_kernel").


#### Returns:

* <b>`next_state`</b>: Tensor or Python list of `Tensor`s representing the state(s)
    of the Markov chain(s) at each result step. Has same shape as
    `current_state`.
* <b>`kernel_results`</b>: `collections.namedtuple` of internal calculations used to
    advance the chain.


#### Raises:

* <b>`ValueError`</b>: if there isn't one `step_size` or a list with same length as
    `current_state`.