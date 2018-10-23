

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.distributions.Dirichlet

## Class `Dirichlet`

Inherits From: [`Distribution`](../../tf/distributions/Distribution)

### Aliases:

* Class `tf.contrib.distributions.Dirichlet`
* Class `tf.distributions.Dirichlet`



Defined in [`tensorflow/python/ops/distributions/dirichlet.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/distributions/dirichlet.py).

See the guide: [Statistical Distributions (contrib) > Multivariate distributions](../../../../api_guides/python/contrib.distributions#Multivariate_distributions)

Dirichlet distribution.

The Dirichlet distribution is defined over the
[`(k-1)`-simplex](https://en.wikipedia.org/wiki/Simplex) using a positive,
length-`k` vector `concentration` (`k > 1`). The Dirichlet is identically the
Beta distribution when `k = 2`.

#### Mathematical Details

The Dirichlet is a distribution over the open `(k-1)`-simplex, i.e.,

```none
S^{k-1} = { (x_0, ..., x_{k-1}) in R^k : sum_j x_j = 1 and all_j x_j > 0 }.
```

The probability density function (pdf) is,

```none
pdf(x; alpha) = prod_j x_j**(alpha_j - 1) / Z
Z = prod_j Gamma(alpha_j) / Gamma(sum_j alpha_j)
```

where:

* `x in S^{k-1}`, i.e., the `(k-1)`-simplex,
* `concentration = alpha = [alpha_0, ..., alpha_{k-1}]`, `alpha_j > 0`,
* `Z` is the normalization constant aka the [multivariate beta function](
  https://en.wikipedia.org/wiki/Beta_function#Multivariate_beta_function),
  and,
* `Gamma` is the [gamma function](
  https://en.wikipedia.org/wiki/Gamma_function).

The `concentration` represents mean total counts of class occurrence, i.e.,

```none
concentration = alpha = mean * total_concentration
```

where `mean` in `S^{k-1}` and `total_concentration` is a positive real number
representing a mean total count.

Distribution parameters are automatically broadcast in all functions; see
examples for details.

#### Examples

```python
# Create a single trivariate Dirichlet, with the 3rd class being three times
# more frequent than the first. I.e., batch_shape=[], event_shape=[3].
alpha = [1., 2, 3]
dist = Dirichlet(alpha)

dist.sample([4, 5])  # shape: [4, 5, 3]

# x has one sample, one batch, three classes:
x = [.2, .3, .5]   # shape: [3]
dist.prob(x)       # shape: []

# x has two samples from one batch:
x = [[.1, .4, .5],
     [.2, .3, .5]]
dist.prob(x)         # shape: [2]

# alpha will be broadcast to shape [5, 7, 3] to match x.
x = [[...]]   # shape: [5, 7, 3]
dist.prob(x)  # shape: [5, 7]
```

```python
# Create batch_shape=[2], event_shape=[3]:
alpha = [[1., 2, 3],
         [4, 5, 6]]   # shape: [2, 3]
dist = Dirichlet(alpha)

dist.sample([4, 5])  # shape: [4, 5, 2, 3]

x = [.2, .3, .5]
# x will be broadcast as [[.2, .3, .5],
#                         [.2, .3, .5]],
# thus matching batch_shape [2, 3].
dist.prob(x)         # shape: [2]
```

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

<h3 id="concentration"><code>concentration</code></h3>

Concentration parameter; expected counts for that coordinate.

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of `Tensor`s handled by this `Distribution`.

<h3 id="event_shape"><code>event_shape</code></h3>

Shape of a single sample from a single batch as a `TensorShape`.

May be partially defined or unknown.

#### Returns:

* <b>`event_shape`</b>: `TensorShape`, possibly unknown.

<h3 id="name"><code>name</code></h3>

Name prepended to all ops created by this `Distribution`.

<h3 id="parameters"><code>parameters</code></h3>

Dictionary of parameters used to instantiate this `Distribution`.

<h3 id="reparameterization_type"><code>reparameterization_type</code></h3>

Describes how samples from the distribution are reparameterized.

Currently this is one of the static instances
`distributions.FULLY_REPARAMETERIZED`
or `distributions.NOT_REPARAMETERIZED`.

#### Returns:

  An instance of `ReparameterizationType`.

<h3 id="total_concentration"><code>total_concentration</code></h3>

Sum of last dim of concentration parameter.

<h3 id="validate_args"><code>validate_args</code></h3>

Python `bool` indicating possibly expensive checks are enabled.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    concentration,
    validate_args=False,
    allow_nan_stats=True,
    name='Dirichlet'
)
```

Initialize a batch of Dirichlet distributions.

#### Args:

* <b>`concentration`</b>: Positive floating-point `Tensor` indicating mean number
    of class occurrences; aka "alpha". Implies `self.dtype`, and
    `self.batch_shape`, `self.event_shape`, i.e., if
    `concentration.shape = [N1, N2, ..., Nm, k]` then
    `batch_shape = [N1, N2, ..., Nm]` and
    `event_shape = [k]`.
* <b>`validate_args`</b>: Python `bool`, default `False`. When `True` distribution
    parameters are checked for validity despite possibly degrading runtime
    performance. When `False` invalid inputs may silently render incorrect
    outputs.
* <b>`allow_nan_stats`</b>: Python `bool`, default `True`. When `True`, statistics
    (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
    result is undefined. When `False`, an exception is raised if one or
    more of the statistic's batch members are undefined.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this class.

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
* <b>`name`</b>: The name to give this op.


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

  **override_parameters_kwargs: String/value dictionary of initialization
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

* <b>`name`</b>: The name to give this op.


#### Returns:

* <b>`covariance`</b>: Floating-point `Tensor` with shape `[B1, ..., Bn, k', k']`
    where the first `n` dimensions are batch coordinates and
    `k' = reduce_prod(self.event_shape)`.

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

* <b>`name`</b>: The name to give this op.


#### Returns:

* <b>`is_scalar_batch`</b>: `bool` scalar `Tensor`.

<h3 id="is_scalar_event"><code>is_scalar_event</code></h3>

``` python
is_scalar_event(name='is_scalar_event')
```

Indicates that `event_shape == []`.

#### Args:

* <b>`name`</b>: The name to give this op.


#### Returns:

* <b>`is_scalar_event`</b>: `bool` scalar `Tensor`.

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
* <b>`name`</b>: The name to give this op.


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


Additional documentation from `Dirichlet`:

Note: `value` must be a non-negative tensor with
dtype `self.dtype` and be in the `(self.event_shape() - 1)`-simplex, i.e.,
`tf.reduce_sum(value, -1) = 1`. It must have a shape compatible with
`self.batch_shape() + self.event_shape()`.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.


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
* <b>`name`</b>: The name to give this op.


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

Additional documentation from `Dirichlet`:

Note: The mode is undefined when any `concentration <= 1`. If
`self.allow_nan_stats` is `True`, `NaN` is used for undefined modes. If
`self.allow_nan_stats` is `False` an exception is raised when one or more
modes are undefined.

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


Additional documentation from `Dirichlet`:

Note: `value` must be a non-negative tensor with
dtype `self.dtype` and be in the `(self.event_shape() - 1)`-simplex, i.e.,
`tf.reduce_sum(value, -1) = 1`. It must have a shape compatible with
`self.batch_shape() + self.event_shape()`.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.


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
* <b>`name`</b>: The name to give this op.


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

* <b>`name`</b>: The name to give this op.


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
* <b>`name`</b>: The name to give this op.


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

* <b>`name`</b>: The name to give this op.


#### Returns:

* <b>`variance`</b>: Floating-point `Tensor` with shape identical to
    `batch_shape + event_shape`, i.e., the same shape as `self.mean()`.



