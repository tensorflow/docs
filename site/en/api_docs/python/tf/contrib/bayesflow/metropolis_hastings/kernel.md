

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.metropolis_hastings.kernel

``` python
tf.contrib.bayesflow.metropolis_hastings.kernel(
    target_log_prob_fn,
    proposal_fn,
    current_state,
    seed=None,
    current_target_log_prob=None,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/metropolis_hastings_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/bayesflow/python/ops/metropolis_hastings_impl.py).

Runs the Metropolis-Hastings transition kernel.

This function can update multiple chains in parallel. It assumes that all
leftmost dimensions of `current_state` index independent chain states (and are
therefore updated independently). The output of `target_log_prob_fn()` should
sum log-probabilities across all event dimensions. Slices along the rightmost
dimensions may have different target distributions; for example,
`current_state[0, :]` could have a different target distribution from
`current_state[1, :]`. This is up to `target_log_prob_fn()`. (The number of
independent chains is `tf.size(target_log_prob_fn(*current_state))`.)

#### Args:

* <b>`target_log_prob_fn`</b>: Python callable which takes an argument like
    `current_state` (or `*current_state` if it's a list) and returns its
    (possibly unnormalized) log-density under the target distribution.
* <b>`proposal_fn`</b>: Python callable which takes an argument like `current_state`
    (or `*current_state` if it's a list) and returns a tuple of proposed
    states of same shape as `state`, and a log ratio `Tensor` of same shape
    as `current_target_log_prob`. The log ratio is the log-probability of
    `state` given proposed states minus the log-probability of proposed
    states given `state`. If the proposal is symmetric, set the second value
    to `None`: this enables more efficient computation than explicitly
    supplying a tensor of zeros.
* <b>`current_state`</b>: `Tensor` or Python `list` of `Tensor`s representing the
    current state(s) of the Markov chain(s). The first `r` dimensions index
    independent chains, `r = tf.rank(target_log_prob_fn(*current_state))`.
* <b>`seed`</b>: Python integer to seed the random number generator.
* <b>`current_target_log_prob`</b>: (Optional) `Tensor` representing the value of
    `target_log_prob_fn` at the `current_state`. The only reason to
    specify this argument is to reduce TF graph size.
    Default value: `None` (i.e., compute as needed).
* <b>`name`</b>: A name of the operation (optional).


#### Returns:

* <b>`next_state`</b>: Tensor or Python list of `Tensor`s representing the state(s)
    of the Markov chain(s) at each result step. Has same shape as
    `current_state`.
* <b>`kernel_results`</b>: `collections.namedtuple` of internal calculations used to
    advance the chain.

#### Examples

We illustrate Metropolis-Hastings on a Normal likelihood with
unknown mean.

```python
tfd = tf.contrib.distributions
tfp = tf.contrib.bayesflow

loc = tf.get_variable("loc", initializer=1.)
x = tf.constant([0.0] * 50)

def make_target_log_prob_fn(x):
  def target_log_prob_fn(loc):
    prior = tfd.Normal(loc=0., scale=1.)
    likelihood = tfd.Independent(
      tfd.Normal(loc=loc, scale=0.1),
      reinterpreted_batch_ndims=1)
    return prior.log_prob(loc) + likelihood.log_prob(x)
  return target_log_prob_fn

next_state, kernel_results = tfp.metropolis_hastings.kernel(
    target_log_prob_fn=make_target_log_prob_fn(x),
    proposal_fn=tfp.metropolis_hastings.proposal_normal(),
    current_state=loc)
loc_update = loc.assign(next_state)
```

We illustrate Metropolis-Hastings on a Normal likelihood with
unknown mean and variance. We apply 4 chains.

```python
tfd = tf.contrib.distributions
tfp = tf.contrib.bayesflow

num_chains = 4
loc = tf.get_variable("loc", shape=[num_chains],
                      initializer=tf.random_normal_initializer())
scale = tf.get_variable("scale", shape=[num_chains],
                        initializer=tf.ones_initializer())
x = tf.constant([0.0] * 50)

def make_target_log_prob_fn(x):
  data = tf.reshape(x, shape=[-1, 1])
  def target_log_prob_fn(loc, scale):
    prior_loc = tfd.Normal(loc=0., scale=1.)
    prior_scale = tfd.InverseGamma(concentration=1., rate=1.)
    likelihood = tfd.Independent(
      tfd.Normal(loc=loc, scale=scale),
      reinterpreted_batch_ndims=1)
    return (prior_loc.log_prob(loc) +
            prior_scale.log_prob(scale) +
            likelihood.log_prob(data))
  return target_log_prob_fn

def proposal_fn(loc, scale):
  loc_proposal = tfp.metropolis_hastings.proposal_normal()
  scale_proposal = tfp.metropolis_hastings.proposal_uniform(minval=-1.)
  proposed_loc, _ = loc_proposal(loc)
  proposed_scale, _ = scale_proposal(scale)
  proposed_scale = tf.maximum(proposed_scale, 0.01)
  return [proposed_loc, proposed_scale], None

next_state, kernel_results = tfp.metropolis_hastings.kernel(
    target_log_prob_fn=make_target_log_prob_fn(x),
    proposal_fn=proposal_fn,
    current_state=[loc, scale])
train_op = tf.group(loc.assign(next_state[0]),
                    scale.assign(next_state[1]))
```