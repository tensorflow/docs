

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.VectorDiffeomixture

## Class `VectorDiffeomixture`

Inherits From: [`Distribution`](../../../tf/distributions/Distribution)



Defined in [`tensorflow/contrib/distributions/python/ops/vector_diffeomixture.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/distributions/python/ops/vector_diffeomixture.py).

VectorDiffeomixture distribution.

The VectorDiffeomixture is an approximation to a [compound distribution](
https://en.wikipedia.org/wiki/Compound_probability_distribution), i.e.,

```none
p(x) = int_{X} q(x | v) p(v) dv
     = lim_{Q->infty} sum{ prob[i] q(x | loc=sum_k^K lambda[k;i] loc[k],
                                          scale=sum_k^K lambda[k;i] scale[k])
                          : i=0, ..., Q-1 }
```

where `q(x | v)` is a vector version of the `distribution` argument and `p(v)`
is a SoftmaxNormal parameterized by `mix_loc` and `mix_scale`. The
vector-ization of `distribution` entails an affine transformation of iid
samples from `distribution`.  The `prob` term is from quadrature and
`lambda[k] = sigmoid(mix_loc[k] + sqrt(2) mix_scale[k] grid[k])` where the
`grid` points correspond to the `prob`s.

In the non-approximation case, a draw from the mixture distribution (the
"prior") represents the convex weights for different affine transformations.
I.e., draw a mixing vector `v` (from the `K-1`-simplex) and let the final
sample be: `y = (sum_k^K v[k] scale[k]) @ x + (sum_k^K v[k] loc[k])` where `@`
denotes matrix multiplication.  However, the non-approximate distribution does
not have an analytical probability density function (pdf). Therefore the
`VectorDiffeomixture` class implements an approximation based on
[numerical quadrature](
https://en.wikipedia.org/wiki/Numerical_integration) (default:
[Gauss--Hermite quadrature](
https://en.wikipedia.org/wiki/Gauss%E2%80%93Hermite_quadrature)). I.e., in
Note: although the `VectorDiffeomixture` is approximately the
`SoftmaxNormal-Distribution` compound distribution, it is itself a valid
distribution. It possesses a `sample`, `log_prob`, `mean`, `covariance` which
are all mutually consistent.

#### Intended Use

This distribution is noteworthy because it implements a mixture of
`Vector`-ized distributions yet has samples differentiable in the
distribution's parameters (aka "reparameterized"). It has an analytical
density function with `O(dKQ)` complexity. `d` is the vector dimensionality,
`K` is the number of components, and `Q` is the number of quadrature points.
These properties make it well-suited for Bayesian Variational Inference, i.e.,
as a surrogate family for the posterior.

For large values of `mix_scale`, the `VectorDistribution` behaves increasingly
like a discrete mixture. (In most cases this limit is only achievable by also
increasing the quadrature polynomial degree, `Q`.)

The term `Vector` is consistent with similar named Tensorflow `Distribution`s.
For more details, see the "About `Vector` distributions in Tensorflow."
section.

The term `Diffeomixture` is a portmanteau of
[diffeomorphism](https://en.wikipedia.org/wiki/Diffeomorphism) and [compound
mixture](https://en.wikipedia.org/wiki/Compound_probability_distribution). For
more details, see the "About `Diffeomixture`s and reparametrization.`"
section.

#### Mathematical Details

The `VectorDiffeomixture` approximates a SoftmaxNormal-mixed ("prior")
[compound distribution](
https://en.wikipedia.org/wiki/Compound_probability_distribution).
Using variable-substitution and [numerical quadrature](
https://en.wikipedia.org/wiki/Numerical_integration) (default:
[Gauss--Hermite quadrature](
https://en.wikipedia.org/wiki/Gauss%E2%80%93Hermite_quadrature)) we can
redefine the distribution to be a parameter-less convex combination of `K`
different affine combinations of a `d` iid samples from `distribution`.

That is, defined over `R**d` this distribution is parameterized by a
(batch of) length-`K` `mix_loc` and `mix_scale` vectors, a length-`K` list of
(a batch of) length-`d` `loc` vectors, and a length-`K` list of `scale`
`LinearOperator`s each operating on a (batch of) length-`d` vector space.
Finally, a `distribution` parameter specifies the underlying base distribution
which is "lifted" to become multivariate ("lifting" is the same concept as in
`TransformedDistribution`).

The probability density function (pdf) is,

```none
pdf(y; mix_loc, mix_scale, loc, scale, phi)
  = sum{ prob[i] phi(f_inverse(x; i)) / abs(det(interp_scale[i]))
        : i=0, ..., Q-1 }
```

where, `phi` is the base distribution pdf, and,

```none
f_inverse(x; i) = inv(interp_scale[i]) @ (x - interp_loc[i])
interp_loc[i]   = sum{ lambda[k; i] loc[k]   : k=0, ..., K-1 }
interp_scale[i] = sum{ lambda[k; i] scale[k] : k=0, ..., K-1 }
```

and,

```none
grid, weight = np.polynomial.hermite.hermgauss(quadrature_size)
prob[k]   = weight[k] / sqrt(pi)
lambda[k; i] = sigmoid(mix_loc[k] + sqrt(2) mix_scale[k] grid[i])
```

The distribution corresponding to `phi` must be a scalar-batch, scalar-event
distribution. Typically it is reparameterized. If not, it must be a function
of non-trainable parameters.

WARNING: If you backprop through a VectorDiffeomixture sample and the "base"
distribution is both: not `FULLY_REPARAMETERIZED` and a function of trainable
variables, then the gradient is not guaranteed correct!

#### About `Vector` distributions in TensorFlow.

The `VectorDiffeomixture` is a non-standard distribution that has properties
particularly useful in [variational Bayesian
methods](https://en.wikipedia.org/wiki/Variational_Bayesian_methods).

Conditioned on a draw from the SoftmaxNormal, `Y|v` is a vector whose
components are linear combinations of affine transformations, thus is itself
an affine transformation. Therefore `Y|v` lives in the vector space generated
by vectors of affine-transformed distributions.

Note: The marginals `Y_1|v, ..., Y_d|v` are *not* generally identical to some
parameterization of `distribution`.  This is due to the fact that the sum of
draws from `distribution` are not generally itself the same `distribution`.

#### About `Diffeomixture`s and reparameterization.

The `VectorDiffeomixture` is designed to be reparameterized, i.e., its
parameters are only used to transform samples from a distribution which has no
trainable parameters. This property is important because backprop stops at
sources of stochasticity. That is, as long as the parameters are used *after*
the underlying source of stochasticity, the computed gradient is accurate.

Reparametrization means that we can use gradient-descent (via backprop) to
optimize Monte-Carlo objectives. Such objectives are a finite-sample
approximation of an expectation and arise throughout scientific computing.

#### Examples

```python
tfd = tf.contrib.distributions

# Create two batches of VectorDiffeomixtures, one with mix_loc=[0.] and
# another with mix_loc=[1]. In both cases, `K=2` and the affine
# transformations involve:
# k=0: loc=zeros(dims)  scale=LinearOperatorScaledIdentity
# k=1: loc=[2.]*dims    scale=LinOpDiag
dims = 5
vdm = tfd.VectorDiffeomixture(
    mix_loc=[[0.], [1]],
    mix_scale=[1.],
    distribution=tfd.Normal(loc=0., scale=1.),
    loc=[
        None,  # Equivalent to `np.zeros(dims, dtype=np.float32)`.
        np.float32([2.]*dims),
    ],
    scale=[
        tf.linalg.LinearOperatorScaledIdentity(
          num_rows=dims,
          multiplier=np.float32(1.1),
          is_positive_definite=True),
        tf.linalg.LinearOperatorDiag(
          diag=np.linspace(2.5, 3.5, dims, dtype=np.float32),
          is_positive_definite=True),
    ],
    validate_args=True)

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

<h3 id="distribution"><code>distribution</code></h3>

Base scalar-event, scalar-batch distribution.

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of `Tensor`s handled by this `Distribution`.

<h3 id="endpoint_affine"><code>endpoint_affine</code></h3>

Affine transformation for each of `K` components.

<h3 id="event_shape"><code>event_shape</code></h3>

Shape of a single sample from a single batch as a `TensorShape`.

May be partially defined or unknown.

#### Returns:

* <b>`event_shape`</b>: `TensorShape`, possibly unknown.

<h3 id="interpolate_weight"><code>interpolate_weight</code></h3>

Grid of mixing probabilities, one for each grid point.

<h3 id="interpolated_affine"><code>interpolated_affine</code></h3>

Affine transformation for each convex combination of `K` components.

<h3 id="mixture_distribution"><code>mixture_distribution</code></h3>

Distribution used to select a convex combination of affine transforms.

<h3 id="name"><code>name</code></h3>

Name prepended to all ops created by this `Distribution`.

<h3 id="parameters"><code>parameters</code></h3>

Dictionary of parameters used to instantiate this `Distribution`.

<h3 id="quadrature_grid"><code>quadrature_grid</code></h3>

Quadrature grid points.

<h3 id="quadrature_probs"><code>quadrature_probs</code></h3>

Quadrature normalized weights.

<h3 id="reparameterization_type"><code>reparameterization_type</code></h3>

Describes how samples from the distribution are reparameterized.

Currently this is one of the static instances
`distributions.FULLY_REPARAMETERIZED`
or `distributions.NOT_REPARAMETERIZED`.

#### Returns:

An instance of `ReparameterizationType`.

<h3 id="validate_args"><code>validate_args</code></h3>

Python `bool` indicating possibly expensive checks are enabled.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    mix_loc,
    mix_scale,
    distribution,
    loc=None,
    scale=None,
    quadrature_grid_and_probs=None,
    validate_args=False,
    allow_nan_stats=True,
    name='VectorDiffeomixture'
)
```

Constructs the VectorDiffeomixture on `R**k`.

#### Args:

* <b>`mix_loc`</b>: `float`-like `Tensor`. Represents the `location` parameter of the
    SoftmaxNormal used for selecting one of the `K` affine transformations.
* <b>`mix_scale`</b>: `float`-like `Tensor`. Represents the `scale` parameter of the
    SoftmaxNormal used for selecting one of the `K` affine transformations.
* <b>`distribution`</b>: `tf.Distribution`-like instance. Distribution from which `d`
    iid samples are used as input to the selected affine transformation.
    Must be a scalar-batch, scalar-event distribution.  Typically
    `distribution.reparameterization_type = FULLY_REPARAMETERIZED` or it is
    a function of non-trainable parameters. WARNING: If you backprop through
    a VectorDiffeomixture sample and the `distribution` is not
    `FULLY_REPARAMETERIZED` yet is a function of trainable variables, then
    the gradient will be incorrect!
* <b>`loc`</b>: Length-`K` list of `float`-type `Tensor`s. The `k`-th element
    represents the `shift` used for the `k`-th affine transformation.  If
    the `k`-th item is `None`, `loc` is implicitly `0`.  When specified,
    must have shape `[B1, ..., Bb, d]` where `b >= 0` and `d` is the event
    size.
* <b>`scale`</b>: Length-`K` list of `LinearOperator`s. Each should be
    positive-definite and operate on a `d`-dimensional vector space. The
    `k`-th element represents the `scale` used for the `k`-th affine
    transformation. `LinearOperator`s must have shape `[B1, ..., Bb, d, d]`,
    `b >= 0`, i.e., characterizes `b`-batches of `d x d` matrices
* <b>`quadrature_grid_and_probs`</b>: Python pair of `float`-like `Tensor`s
    representing the sample points and the corresponding (possibly
    normalized) weight.  When `None`, defaults to:
    `np.polynomial.hermite.hermgauss(deg=8)`.
* <b>`validate_args`</b>: Python `bool`, default `False`. When `True` distribution
    parameters are checked for validity despite possibly degrading runtime
    performance. When `False` invalid inputs may silently render incorrect
    outputs.
* <b>`allow_nan_stats`</b>: Python `bool`, default `True`. When `True`,
    statistics (e.g., mean, mode, variance) use the value "`NaN`" to
    indicate the result is undefined. When `False`, an exception is raised
    if one or more of the statistic's batch members are undefined.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this class.


#### Raises:

* <b>`ValueError`</b>: if `not scale or len(scale) < 2`.
* <b>`ValueError`</b>: if `len(loc) != len(scale)`
* <b>`ValueError`</b>: if `quadrature_grid_and_probs is not None` and
    `len(quadrature_grid_and_probs[0]) != len(quadrature_grid_and_probs[1])`
* <b>`ValueError`</b>: if `validate_args` and any not scale.is_positive_definite.
* <b>`TypeError`</b>: if any scale.dtype != scale[0].dtype.
* <b>`TypeError`</b>: if any loc.dtype != scale[0].dtype.
* <b>`NotImplementedError`</b>: if `len(scale) != 2`.
* <b>`ValueError`</b>: if `not distribution.is_scalar_batch`.
* <b>`ValueError`</b>: if `not distribution.is_scalar_event`.

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

* <b>`other`</b>: `tf.distributions.Distribution` instance.
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
measure `r`, (Shanon) cross entropy is defined as:

```none
KL[p, q] = E_p[log(p(X)/q(X))]
         = -int_F p(x) log q(x) dr(x) + int_F p(x) log p(x) dr(x)
         = H[p, q] - H[p]
```

where `F` denotes the support of the random variable `X ~ p`, `H[., .]`
denotes (Shanon) cross entropy, and `H[.]` denotes (Shanon) entropy.

#### Args:

* <b>`other`</b>: `tf.distributions.Distribution` instance.
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



