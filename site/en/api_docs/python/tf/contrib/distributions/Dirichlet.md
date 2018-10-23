


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.distributions.Dirichlet

### `class tf.contrib.distributions.Dirichlet`

See the guide: [Statistical Distributions (contrib) > Multivariate distributions](../../../../../api_guides/python/contrib.distributions#Multivariate_distributions)

Dirichlet distribution.

This distribution is parameterized by a vector `alpha` of concentration
parameters for `k` classes.

#### Mathematical details

The Dirichlet is a distribution over the standard n-simplex, where the
standard n-simplex is defined by:
```{ (x_1, ..., x_n) in R^(n+1) | sum_j x_j = 1 and x_j >= 0 for all j }```.
The distribution has hyperparameters `alpha = (alpha_1,...,alpha_k)`,
and probability mass function (prob):

```prob(x) = 1 / Beta(alpha) * prod_j x_j^(alpha_j - 1)```

where `Beta(x) = prod_j Gamma(x_j) / Gamma(sum_j x_j)` is the multivariate
beta function.


This class provides methods to create indexed batches of Dirichlet
distributions.  If the provided `alpha` is rank 2 or higher, for
every fixed set of leading dimensions, the last dimension represents one
single Dirichlet distribution.  When calling distribution
functions (e.g. `dist.prob(x)`), `alpha` and `x` are broadcast to the
same shape (if possible).  In all cases, the last dimension of alpha/x
represents single Dirichlet distributions.

#### Examples

```python
alpha = [1, 2, 3]
dist = Dirichlet(alpha)
```

Creates a 3-class distribution, with the 3rd class is most likely to be drawn.
The distribution functions can be evaluated on x.

```python
# x same shape as alpha.
x = [.2, .3, .5]
dist.prob(x)  # Shape []

# alpha will be broadcast to [[1, 2, 3], [1, 2, 3]] to match x.
x = [[.1, .4, .5], [.2, .3, .5]]
dist.prob(x)  # Shape [2]

# alpha will be broadcast to shape [5, 7, 3] to match x.
x = [[...]]  # Shape [5, 7, 3]
dist.prob(x)  # Shape [5, 7]
```

Creates a 2-batch of 3-class distributions.

```python
alpha = [[1, 2, 3], [4, 5, 6]]  # Shape [2, 3]
dist = Dirichlet(alpha)

# x will be broadcast to [[2, 1, 0], [2, 1, 0]] to match alpha.
x = [.2, .3, .5]
dist.prob(x)  # Shape [2]
```

## Properties

<h3 id="allow_nan_stats"><code>allow_nan_stats</code></h3>

Python boolean describing behavior when a stat is undefined.

Stats return +/- infinity when it makes sense.  E.g., the variance
of a Cauchy distribution is infinity.  However, sometimes the
statistic is undefined, e.g., if a distribution's pdf does not achieve a
maximum within the support of the distribution, the mode is undefined.
If the mean is undefined, then by definition the variance is undefined.
E.g. the mean for Student's T for df = 1 is undefined (no clear way to say
it is either + or - infinity), so the variance = E[(X - mean)^2] is also
undefined.

#### Returns:

* <b>`allow_nan_stats`</b>: Python boolean.

<h3 id="alpha"><code>alpha</code></h3>

Shape parameter.

<h3 id="alpha_sum"><code>alpha_sum</code></h3>

Sum of shape parameter.

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of `Tensor`s handled by this `Distribution`.

<h3 id="is_continuous"><code>is_continuous</code></h3>



<h3 id="is_reparameterized"><code>is_reparameterized</code></h3>



<h3 id="name"><code>name</code></h3>

Name prepended to all ops created by this `Distribution`.

<h3 id="parameters"><code>parameters</code></h3>

Dictionary of parameters used to instantiate this `Distribution`.

<h3 id="validate_args"><code>validate_args</code></h3>

Python boolean indicated possibly expensive checks are enabled.



## Methods

<h3 id="__init__"><code>__init__(alpha, validate_args=False, allow_nan_stats=True, name='Dirichlet')</code></h3>

Initialize a batch of Dirichlet distributions.

#### Args:

* <b>`alpha`</b>:  Positive floating point tensor with shape broadcastable to
    `[N1,..., Nm, k]` `m >= 0`.  Defines this as a batch of `N1 x ... x Nm`
     different `k` class Dirichlet distributions.
* <b>`validate_args`</b>: `Boolean`, default `False`.  Whether to assert valid values
    for parameters `alpha` and `x` in `prob` and `log_prob`.  If `False`,
    correct behavior is not guaranteed.
* <b>`allow_nan_stats`</b>: `Boolean`, default `True`.  If `False`, raise an
    exception if a statistic (e.g. mean/mode/etc...) is undefined for any
    batch member.  If `True`, batch members with valid parameters leading to
    undefined statistics will return NaN for this statistic.
* <b>`name`</b>: The name to prefix Ops created by this distribution class.

Examples:

```python
# Define 1-batch of 2-class Dirichlet distributions,
# also known as a Beta distribution.
dist = Dirichlet([1.1, 2.0])

# Define a 2-batch of 3-class distributions.
dist = Dirichlet([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
```

<h3 id="batch_shape"><code>batch_shape(name='batch_shape')</code></h3>

Shape of a single sample from a single event index as a 1-D `Tensor`.

The product of the dimensions of the `batch_shape` is the number of
independent distributions of this kind the instance represents.

#### Args:

* <b>`name`</b>: name to give to the op


#### Returns:

* <b>`batch_shape`</b>: `Tensor`.

<h3 id="cdf"><code>cdf(value, name='cdf', **condition_kwargs)</code></h3>

Cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

```
cdf(x) := P[X <= x]
```

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`cdf`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="copy"><code>copy(**override_parameters_kwargs)</code></h3>

Creates a deep copy of the distribution.

Note: the copy distribution may continue to depend on the original
intialization arguments.

#### Args:

  **override_parameters_kwargs: String/value dictionary of initialization
    arguments to override with new values.


#### Returns:

* <b>`distribution`</b>: A new instance of `type(self)` intitialized from the union
    of self.parameters and override_parameters_kwargs, i.e.,
    `dict(self.parameters, **override_parameters_kwargs)`.

<h3 id="entropy"><code>entropy(name='entropy')</code></h3>

Shannon entropy in nats.

<h3 id="event_shape"><code>event_shape(name='event_shape')</code></h3>

Shape of a single sample from a single batch as a 1-D int32 `Tensor`.

#### Args:

* <b>`name`</b>: name to give to the op


#### Returns:

* <b>`event_shape`</b>: `Tensor`.

<h3 id="get_batch_shape"><code>get_batch_shape()</code></h3>

Shape of a single sample from a single event index as a `TensorShape`.

Same meaning as `batch_shape`. May be only partially defined.

#### Returns:

* <b>`batch_shape`</b>: `TensorShape`, possibly unknown.

<h3 id="get_event_shape"><code>get_event_shape()</code></h3>

Shape of a single sample from a single batch as a `TensorShape`.

Same meaning as `event_shape`. May be only partially defined.

#### Returns:

* <b>`event_shape`</b>: `TensorShape`, possibly unknown.

<h3 id="is_scalar_batch"><code>is_scalar_batch(name='is_scalar_batch')</code></h3>

Indicates that `batch_shape == []`.

#### Args:

* <b>`name`</b>: The name to give this op.


#### Returns:

* <b>`is_scalar_batch`</b>: `Boolean` `scalar` `Tensor`.

<h3 id="is_scalar_event"><code>is_scalar_event(name='is_scalar_event')</code></h3>

Indicates that `event_shape == []`.

#### Args:

* <b>`name`</b>: The name to give this op.


#### Returns:

* <b>`is_scalar_event`</b>: `Boolean` `scalar` `Tensor`.

<h3 id="log_cdf"><code>log_cdf(value, name='log_cdf', **condition_kwargs)</code></h3>

Log cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

```
log_cdf(x) := Log[ P[X <= x] ]
```

Often, a numerical approximation can be used for `log_cdf(x)` that yields
a more accurate answer than simply taking the logarithm of the `cdf` when
`x << -1`.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`logcdf`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="log_pdf"><code>log_pdf(value, name='log_pdf', **condition_kwargs)</code></h3>

Log probability density function.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`log_prob`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.


#### Raises:

* <b>`TypeError`</b>: if not `is_continuous`.

<h3 id="log_pmf"><code>log_pmf(value, name='log_pmf', **condition_kwargs)</code></h3>

Log probability mass function.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`log_pmf`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.


#### Raises:

* <b>`TypeError`</b>: if `is_continuous`.

<h3 id="log_prob"><code>log_prob(value, name='log_prob', **condition_kwargs)</code></h3>

Log probability density/mass function (depending on `is_continuous`).


Additional documentation from `Dirichlet`:

Note that the input must be a non-negative tensor with dtype `dtype` and whose
shape can be broadcast with `self.alpha`.  For fixed leading dimensions, the
last dimension represents counts for the corresponding Dirichlet distribution
in `self.alpha`. `x` is only legal if it sums up to one.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`log_prob`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="log_survival_function"><code>log_survival_function(value, name='log_survival_function', **condition_kwargs)</code></h3>

Log survival function.

Given random variable `X`, the survival function is defined:

```
log_survival_function(x) = Log[ P[X > x] ]
                         = Log[ 1 - P[X <= x] ]
                         = Log[ 1 - cdf(x) ]
```

Typically, different numerical approximations can be used for the log
survival function, which are more accurate than `1 - cdf(x)` when `x >> 1`.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

  `Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type
    `self.dtype`.

<h3 id="mean"><code>mean(name='mean')</code></h3>

Mean.

<h3 id="mode"><code>mode(name='mode')</code></h3>

Mode.

Additional documentation from `Dirichlet`:

Note that the mode for the Dirichlet distribution is only defined
when `alpha > 1`. This returns the mode when `alpha > 1`,
and NaN otherwise. If `self.allow_nan_stats` is `False`, an exception
will be raised rather than returning `NaN`.

<h3 id="param_shapes"><code>param_shapes(cls, sample_shape, name='DistributionParamShapes')</code></h3>

Shapes of parameters given the desired shape of a call to `sample()`.

Subclasses should override static method `_param_shapes`.

#### Args:

* <b>`sample_shape`</b>: `Tensor` or python list/tuple. Desired shape of a call to
    `sample()`.
* <b>`name`</b>: name to prepend ops with.


#### Returns:

  `dict` of parameter name to `Tensor` shapes.

<h3 id="param_static_shapes"><code>param_static_shapes(cls, sample_shape)</code></h3>

param_shapes with static (i.e. TensorShape) shapes.

#### Args:

* <b>`sample_shape`</b>: `TensorShape` or python list/tuple. Desired shape of a call
    to `sample()`.


#### Returns:

  `dict` of parameter name to `TensorShape`.


#### Raises:

* <b>`ValueError`</b>: if `sample_shape` is a `TensorShape` and is not fully defined.

<h3 id="pdf"><code>pdf(value, name='pdf', **condition_kwargs)</code></h3>

Probability density function.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`prob`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.


#### Raises:

* <b>`TypeError`</b>: if not `is_continuous`.

<h3 id="pmf"><code>pmf(value, name='pmf', **condition_kwargs)</code></h3>

Probability mass function.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`pmf`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.


#### Raises:

* <b>`TypeError`</b>: if `is_continuous`.

<h3 id="prob"><code>prob(value, name='prob', **condition_kwargs)</code></h3>

Probability density/mass function (depending on `is_continuous`).


Additional documentation from `Dirichlet`:

Note that the input must be a non-negative tensor with dtype `dtype` and whose
shape can be broadcast with `self.alpha`.  For fixed leading dimensions, the
last dimension represents counts for the corresponding Dirichlet distribution
in `self.alpha`. `x` is only legal if it sums up to one.

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`prob`</b>: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
    values of type `self.dtype`.

<h3 id="sample"><code>sample(sample_shape=(), seed=None, name='sample', **condition_kwargs)</code></h3>

Generate samples of the specified shape.

Note that a call to `sample()` without arguments will generate a single
sample.

#### Args:

* <b>`sample_shape`</b>: 0D or 1D `int32` `Tensor`. Shape of the generated samples.
* <b>`seed`</b>: Python integer seed for RNG
* <b>`name`</b>: name to give to the op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

* <b>`samples`</b>: a `Tensor` with prepended dimensions `sample_shape`.

<h3 id="std"><code>std(name='std')</code></h3>

Standard deviation.

<h3 id="survival_function"><code>survival_function(value, name='survival_function', **condition_kwargs)</code></h3>

Survival function.

Given random variable `X`, the survival function is defined:

```
survival_function(x) = P[X > x]
                     = 1 - P[X <= x]
                     = 1 - cdf(x).
```

#### Args:

* <b>`value`</b>: `float` or `double` `Tensor`.
* <b>`name`</b>: The name to give this op.
  **condition_kwargs: Named arguments forwarded to subclass implementation.


#### Returns:

  Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type
    `self.dtype`.

<h3 id="variance"><code>variance(name='variance')</code></h3>

Variance.





Defined in [`tensorflow/contrib/distributions/python/ops/dirichlet.py`](https://www.tensorflow.org/code/tensorflow/contrib/distributions/python/ops/dirichlet.py).

