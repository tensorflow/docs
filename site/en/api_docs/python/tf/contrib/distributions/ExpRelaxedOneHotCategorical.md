page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.ExpRelaxedOneHotCategorical

## Class `ExpRelaxedOneHotCategorical`

Inherits From: [`Distribution`](../../../tf/distributions/Distribution)



Defined in [`tensorflow/contrib/distributions/python/ops/relaxed_onehot_categorical.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/distributions/python/ops/relaxed_onehot_categorical.py).

ExpRelaxedOneHotCategorical distribution with temperature and logits.

An ExpRelaxedOneHotCategorical distribution is a log-transformed
RelaxedOneHotCategorical distribution. The RelaxedOneHotCategorical is a
distribution over random probability vectors, vectors of positive real
values that sum to one, which continuously approximates a OneHotCategorical.
The degree of approximation is controlled by a temperature: as the temperature
goes to 0 the RelaxedOneHotCategorical becomes discrete with a distribution
described by the logits, as the temperature goes to infinity the
RelaxedOneHotCategorical becomes the constant distribution that is identically
the constant vector of (1/event_size, ..., 1/event_size).

Because computing log-probabilities of the RelaxedOneHotCategorical can
suffer from underflow issues, this class is one solution for loss
functions that depend on log-probabilities, such as the KL Divergence found
in the variational autoencoder loss. The KL divergence between two
distributions is invariant under invertible transformations, so evaluating
KL divergences of ExpRelaxedOneHotCategorical samples, which are always
followed by a <a href="../../../tf/math/exp"><code>tf.exp</code></a> op, is equivalent to evaluating KL divergences of
RelaxedOneHotCategorical samples. See the appendix of Maddison et al., 2016
for more mathematical details, where this distribution is called the
ExpConcrete.

#### Examples

Creates a continuous distribution, whose exp approximates a 3-class one-hot
categorical distribution. The 2nd class is the most likely to be the
largest component in samples drawn from this distribution. If those samples
are followed by a <a href="../../../tf/math/exp"><code>tf.exp</code></a> op, then they are distributed as a relaxed onehot
categorical.

```python
temperature = 0.5
p = [0.1, 0.5, 0.4]
dist = ExpRelaxedOneHotCategorical(temperature, probs=p)
samples = dist.sample()
exp_samples = tf.exp(samples)
# exp_samples has the same distribution as samples from
# RelaxedOneHotCategorical(temperature, probs=p)
```

Creates a continuous distribution, whose exp approximates a 3-class one-hot
categorical distribution. The 2nd class is the most likely to be the
largest component in samples drawn from this distribution.

```python
temperature = 0.5
logits = [-2, 2, 0]
dist = ExpRelaxedOneHotCategorical(temperature, logits=logits)
samples = dist.sample()
exp_samples = tf.exp(samples)
# exp_samples has the same distribution as samples from
# RelaxedOneHotCategorical(temperature, probs=p)
```

Creates a continuous distribution, whose exp approximates a 3-class one-hot
categorical distribution. Because the temperature is very low, samples from
this distribution are almost discrete, with one component almost 0 and the
others very negative. The 2nd class is the most likely to be the largest
component in samples drawn from this distribution.

```python
temperature = 1e-5
logits = [-2, 2, 0]
dist = ExpRelaxedOneHotCategorical(temperature, logits=logits)
samples = dist.sample()
exp_samples = tf.exp(samples)
# exp_samples has the same distribution as samples from
# RelaxedOneHotCategorical(temperature, probs=p)
```

Creates a continuous distribution, whose exp approximates a 3-class one-hot
categorical distribution. Because the temperature is very high, samples from
this distribution are usually close to the (-log(3), -log(3), -log(3)) vector.
The 2nd class is still the most likely to be the largest component
in samples drawn from this distribution.

```python
temperature = 10
logits = [-2, 2, 0]
dist = ExpRelaxedOneHotCategorical(temperature, logits=logits)
samples = dist.sample()
exp_samples = tf.exp(samples)
# exp_samples has the same distribution as samples from
# RelaxedOneHotCategorical(temperature, probs=p)
```

Chris J. Maddison, Andriy Mnih, and Yee Whye Teh. The Concrete Distribution:
A Continuous Relaxation of Discrete Random Variables. 2016.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    temperature,
    logits=None,
    probs=None,
    dtype=None,
    validate_args=False,
    allow_nan_stats=True,
    name='ExpRelaxedOneHotCategorical'
)
```

Initialize ExpRelaxedOneHotCategorical using class log-probabilities. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-10-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of <a href="../../../tf/contrib/distributions"><code>tf.contrib.distributions</code></a>.

#### Args:

* <b>`temperature`</b>: An 0-D `Tensor`, representing the temperature
    of a set of ExpRelaxedCategorical distributions. The temperature should
    be positive.
* <b>`logits`</b>: An N-D `Tensor`, `N >= 1`, representing the log probabilities
    of a set of ExpRelaxedCategorical distributions. The first
    `N - 1` dimensions index into a batch of independent distributions and
    the last dimension represents a vector of logits for each class. Only
    one of `logits` or `probs` should be passed in.
* <b>`probs`</b>: An N-D `Tensor`, `N >= 1`, representing the probabilities
    of a set of ExpRelaxedCategorical distributions. The first
    `N - 1` dimensions index into a batch of independent distributions and
    the last dimension represents a vector of probabilities for each
    class. Only one of `logits` or `probs` should be passed in.
* <b>`dtype`</b>: The type of the event samples (default: inferred from
    logits/probs).
* <b>`validate_args`</b>: Python `bool`, default `False`. When `True` distribution
    parameters are checked for validity despite possibly degrading runtime
    performance. When `False` invalid inputs may silently render incorrect
    outputs.
* <b>`allow_nan_stats`</b>: Python `bool`, default `True`. When `True`, statistics
    (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
    result is undefined. When `False`, an exception is raised if one or
    more of the statistic's batch members are undefined.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this class.



## Properties

<h3 id="allow_nan_stats"><code>allow_nan_stats</code></h3>

Python `bool` describing behavior when a stat is undefined.

Stats return +/- infinity when it makes sense. E.g., the variance of a
Cauchy distribution is infinity. However, sometimes the statistic is
undefined, e.g., if a distribution's pdf does not achieve a maximum within
the support of the distribution, the mode is undefined. If the mean is
undefined, then by definition the variance is undefined. E.g. the mean for
Student's T for df = 1 is undefined (no clear way to say it is either + or -
infinity), so the variance = E[(X - mean)**2] is also undefined.

#### Returns:

* <b>`allow_nan_stats`</b>: Python `bool`.

<h3 id="batch_shape"><code>batch_shape</code></h3>

Shape of a single sample from a single event index as a `TensorShape`.

May be partially defined or unknown.

The batch dimensions are indexes into independent, non-identical
parameterizations of this distribution.

#### Returns:

* <b>`batch_shape`</b>: `TensorShape`, possibly unknown.

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of `Tensor`s handled by this `Distribution`.

<h3 id="event_shape"><code>event_shape</code></h3>

Shape of a single sample from a single batch as a `TensorShape`.

May be partially defined or unknown.

#### Returns:

* <b>`event_shape`</b>: `TensorShape`, possibly unknown.

<h3 id="event_size"><code>event_size</code></h3>

Scalar `int32` tensor: the number of classes.

<h3 id="logits"><code>logits</code></h3>

Vector of coordinatewise logits.

<h3 id="name"><code>name</code></h3>

Name prepended to all ops created by this `Distribution`.

<h3 id="parameters"><code>parameters</code></h3>

Dictionary of parameters used to instantiate this `Distribution`.

<h3 id="probs"><code>probs</code></h3>

Vector of probabilities summing to one.

<h3 id="reparameterization_type"><code>reparameterization_type</code></h3>

Describes how samples from the distribution are reparameterized.

Currently this is one of the static instances
`distributions.FULLY_REPARAMETERIZED`
or `distributions.NOT_REPARAMETERIZED`.

#### Returns:

An instance of `ReparameterizationType`.

<h3 id="temperature"><code>temperature</code></h3>

Batchwise temperature tensor of a RelaxedCategorical.

<h3 id="validate_args"><code>validate_args</code></h3>

Python `bool` indicating possibly expensive checks are enabled.



## Methods

<h3 id="batch_shape_tensor"><code>batch_shape_tensor</code></h3>

``` python
batch_shape_tensor(name='batch_shape_tensor')
```

Shape of a single sample from a single event index as a 1-D `Tensor`.

The batch dimensions are indexes into independent, non-identical
parameterizations of this distribution.

#### Args:

* <b>`name`</b>: name to give to the op


#### Returns:

* <b>`batch_shape`</b>: `Tensor`.

<h3 id="cdf"><code>cdf</code></h3>

``` python
cdf(
    value,
    name='cdf'
)
```

Cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

```none
cdf(x) := P[X <= x]
```

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`cdf`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="copy"><code>copy</code></h3>

``` python
copy(**override_parameters_kwargs)
```

Creates a deep copy of the distribution.

Note: the copy distribution may continue to depend on the original
initialization arguments.

#### Args:

* <b>`**override_parameters_kwargs`</b>: String/value dictionary of initialization
    arguments to override with new values.


#### Returns:

* <b>`distribution`</b>: A new instance of `type(self)` initialized from the union
    of self.parameters and override_parameters_kwargs, i.e.,
    `dict(self.parameters, **override_parameters_kwargs)`.

<h3 id="covariance"><code>covariance</code></h3>

``` python
covariance(name='covariance')
```

Covariance.

Covariance is (possibly) defined only for non-scalar-event distributions.

For example, for a length-`k`, vector-valued distribution, it is calculated
as,

```none
Cov[i, j] = Covariance(X_i, X_j) = E[(X_i - E[X_i]) (X_j - E[X_j])]
```

where `Cov` is a (batch of) `k x k` matrix, `0 <= (i, j) < k`, and `E`
denotes expectation.

Alternatively, for non-vector, multivariate distributions (e.g.,
matrix-valued, Wishart), `Covariance` shall return a (batch of) matrices
under some vectorization of the events, i.e.,

```none
Cov[i, j] = Covariance(Vec(X)_i, Vec(X)_j) = [as above]
```

where `Cov` is a (batch of) `k' x k'` matrices,
`0 <= (i, j) < k' = reduce_prod(event_shape)`, and `Vec` is some function
mapping indices of this distribution's event dimensions to indices of a
length-`k'` vector.

#### Args:

* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`covariance`</b>: Floating-point `Tensor` with shape `[B1, ..., Bn, k', k']`
    where the first `n` dimensions are batch coordinates and
    `k' = reduce_prod(self.event_shape)`.

<h3 id="cross_entropy"><code>cross_entropy</code></h3>

``` python
cross_entropy(
    other,
    name='cross_entropy'
)
```

Computes the (Shannon) cross entropy.

Denote this distribution (`self`) by `P` and the `other` distribution by
`Q`. Assuming `P, Q` are absolutely continuous with respect to
one another and permit densities `p(x) dr(x)` and `q(x) dr(x)`, (Shanon)
cross entropy is defined as:

```none
H[P, Q] = E_p[-log q(X)] = -int_F p(x) log q(x) dr(x)
```

where `F` denotes the support of the random variable `X ~ P`.

#### Args:

* <b>`other`</b>: `tfp.distributions.Distribution` instance.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`cross_entropy`</b>: `self.dtype` `Tensor` with shape `[B1, ..., Bn]`
    representing `n` different calculations of (Shanon) cross entropy.

<h3 id="entropy"><code>entropy</code></h3>

``` python
entropy(name='entropy')
```

Shannon entropy in nats.

<h3 id="event_shape_tensor"><code>event_shape_tensor</code></h3>

``` python
event_shape_tensor(name='event_shape_tensor')
```

Shape of a single sample from a single batch as a 1-D int32 `Tensor`.

#### Args:

* <b>`name`</b>: name to give to the op


#### Returns:

* <b>`event_shape`</b>: `Tensor`.

<h3 id="is_scalar_batch"><code>is_scalar_batch</code></h3>

``` python
is_scalar_batch(name='is_scalar_batch')
```

Indicates that `batch_shape == []`.

#### Args:

* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`is_scalar_batch`</b>: `bool` scalar `Tensor`.

<h3 id="is_scalar_event"><code>is_scalar_event</code></h3>

``` python
is_scalar_event(name='is_scalar_event')
```

Indicates that `event_shape == []`.

#### Args:

* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`is_scalar_event`</b>: `bool` scalar `Tensor`.

<h3 id="kl_divergence"><code>kl_divergence</code></h3>

``` python
kl_divergence(
    other,
    name='kl_divergence'
)
```

Computes the Kullback--Leibler divergence.

Denote this distribution (`self`) by `p` and the `other` distribution by
`q`. Assuming `p, q` are absolutely continuous with respect to reference
measure `r`, the KL divergence is defined as:

```none
KL[p, q] = E_p[log(p(X)/q(X))]
         = -int_F p(x) log q(x) dr(x) + int_F p(x) log p(x) dr(x)
         = H[p, q] - H[p]
```

where `F` denotes the support of the random variable `X ~ p`, `H[., .]`
denotes (Shanon) cross entropy, and `H[.]` denotes (Shanon) entropy.

#### Args:

* <b>`other`</b>: `tfp.distributions.Distribution` instance.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`kl_divergence`</b>: `self.dtype` `Tensor` with shape `[B1, ..., Bn]`
    representing `n` different calculations of the Kullback-Leibler
    divergence.

<h3 id="log_cdf"><code>log_cdf</code></h3>

``` python
log_cdf(
    value,
    name='log_cdf'
)
```

Log cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

```none
log_cdf(x) := Log[ P[X <= x] ]
```

Often, a numerical approximation can be used for `log_cdf(x)` that yields
a more accurate answer than simply taking the logarithm of the `cdf` when
`x << -1`.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`logcdf`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="log_prob"><code>log_prob</code></h3>

``` python
log_prob(
    value,
    name='log_prob'
)
```

Log probability density/mass function.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`log_prob`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="log_survival_function"><code>log_survival_function</code></h3>

``` python
log_survival_function(
    value,
    name='log_survival_function'
)
```

Log survival function.

Given random variable `X`, the survival function is defined:

```none
log_survival_function(x) = Log[ P[X > x] ]
                         = Log[ 1 - P[X <= x] ]
                         = Log[ 1 - cdf(x) ]
```

Typically, different numerical approximations can be used for the log
survival function, which are more accurate than `1 - cdf(x)` when `x >> 1`.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

`Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type
  `self.dtype`.

<h3 id="mean"><code>mean</code></h3>

``` python
mean(name='mean')
```

Mean.

<h3 id="mode"><code>mode</code></h3>

``` python
mode(name='mode')
```

Mode.

<h3 id="param_shapes"><code>param_shapes</code></h3>

``` python
param_shapes(
    cls,
    sample_shape,
    name='DistributionParamShapes'
)
```

Shapes of parameters given the desired shape of a call to `sample()`.

This is a class method that describes what key/value arguments are required
to instantiate the given `Distribution` so that a particular shape is
returned for that instance's call to `sample()`.

Subclasses should override class method `_param_shapes`.

#### Args:

* <b>`sample_shape`</b>: `Tensor` or python list/tuple. Desired shape of a call to
    `sample()`.
* <b>`name`</b>: name to prepend ops with.


#### Returns:

`dict` of parameter name to `Tensor` shapes.

<h3 id="param_static_shapes"><code>param_static_shapes</code></h3>

``` python
param_static_shapes(
    cls,
    sample_shape
)
```

param_shapes with static (i.e. `TensorShape`) shapes.

This is a class method that describes what key/value arguments are required
to instantiate the given `Distribution` so that a particular shape is
returned for that instance's call to `sample()`. Assumes that the sample's
shape is known statically.

Subclasses should override class method `_param_shapes` to return
constant-valued tensors when constant values are fed.

#### Args:

* <b>`sample_shape`</b>: `TensorShape` or python list/tuple. Desired shape of a call
    to `sample()`.


#### Returns:

`dict` of parameter name to `TensorShape`.


#### Raises:

* <b>`ValueError`</b>: if `sample_shape` is a `TensorShape` and is not fully defined.

<h3 id="prob"><code>prob</code></h3>

``` python
prob(
    value,
    name='prob'
)
```

Probability density/mass function.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`prob`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="quantile"><code>quantile</code></h3>

``` python
quantile(
    value,
    name='quantile'
)
```

Quantile function. Aka "inverse cdf" or "percent point function".

Given random variable `X` and `p in [0, 1]`, the `quantile` is:

```none
quantile(p) := x such that P[X <= x] == p
```

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`quantile`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="sample"><code>sample</code></h3>

``` python
sample(
    sample_shape=(),
    seed=None,
    name='sample'
)
```

Generate samples of the specified shape.

Note that a call to `sample()` without arguments will generate a single
sample.

#### Args:

* <b>`sample_shape`</b>: 0D or 1D `int32` `Tensor`. Shape of the generated samples.
* <b>`seed`</b>: Python integer seed for RNG
* <b>`name`</b>: name to give to the op.


#### Returns:

* <b>`samples`</b>: a `Tensor` with prepended dimensions `sample_shape`.

<h3 id="stddev"><code>stddev</code></h3>

``` python
stddev(name='stddev')
```

Standard deviation.

Standard deviation is defined as,

```none
stddev = E[(X - E[X])**2]**0.5
```

where `X` is the random variable associated with this distribution, `E`
denotes expectation, and `stddev.shape = batch_shape + event_shape`.

#### Args:

* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`stddev`</b>: Floating-point `Tensor` with shape identical to
    `batch_shape + event_shape`, i.e., the same shape as `self.mean()`.

<h3 id="survival_function"><code>survival_function</code></h3>

``` python
survival_function(
    value,
    name='survival_function'
)
```

Survival function.

Given random variable `X`, the survival function is defined:

```none
survival_function(x) = P[X > x]
                     = 1 - P[X <= x]
                     = 1 - cdf(x).
```

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

`Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type
  `self.dtype`.

<h3 id="variance"><code>variance</code></h3>

``` python
variance(name='variance')
```

Variance.

Variance is defined as,

```none
Var = E[(X - E[X])**2]
```

where `X` is the random variable associated with this distribution, `E`
denotes expectation, and `Var.shape = batch_shape + event_shape`.

#### Args:

* <b>`name`</b>: Python `str` prepended to names of ops created by this function.


#### Returns:

* <b>`variance`</b>: Floating-point `Tensor` with shape identical to
    `batch_shape + event_shape`, i.e., the same shape as `self.mean()`.



