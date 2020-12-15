description: Beta distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distributions.Beta" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="batch_shape_tensor"/>
<meta itemprop="property" content="cdf"/>
<meta itemprop="property" content="copy"/>
<meta itemprop="property" content="covariance"/>
<meta itemprop="property" content="cross_entropy"/>
<meta itemprop="property" content="entropy"/>
<meta itemprop="property" content="event_shape_tensor"/>
<meta itemprop="property" content="is_scalar_batch"/>
<meta itemprop="property" content="is_scalar_event"/>
<meta itemprop="property" content="kl_divergence"/>
<meta itemprop="property" content="log_cdf"/>
<meta itemprop="property" content="log_prob"/>
<meta itemprop="property" content="log_survival_function"/>
<meta itemprop="property" content="mean"/>
<meta itemprop="property" content="mode"/>
<meta itemprop="property" content="param_shapes"/>
<meta itemprop="property" content="param_static_shapes"/>
<meta itemprop="property" content="prob"/>
<meta itemprop="property" content="quantile"/>
<meta itemprop="property" content="sample"/>
<meta itemprop="property" content="stddev"/>
<meta itemprop="property" content="survival_function"/>
<meta itemprop="property" content="variance"/>
</div>

# tf.compat.v1.distributions.Beta

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/beta.py#L51-L351">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Beta distribution.

Inherits From: [`Distribution`](../../../../tf/compat/v1/distributions/Distribution.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.distributions.Beta(
    concentration1=None, concentration0=None, validate_args=(False),
    allow_nan_stats=(True), name='Beta'
)
</code></pre>



<!-- Placeholder for "Used in" -->

The Beta distribution is defined over the `(0, 1)` interval using parameters
`concentration1` (aka "alpha") and `concentration0` (aka "beta").

#### Mathematical Details

The probability density function (pdf) is,

```none
pdf(x; alpha, beta) = x**(alpha - 1) (1 - x)**(beta - 1) / Z
Z = Gamma(alpha) Gamma(beta) / Gamma(alpha + beta)
```

where:

* `concentration1 = alpha`,
* `concentration0 = beta`,
* `Z` is the normalization constant, and,
* `Gamma` is the [gamma function](
  https://en.wikipedia.org/wiki/Gamma_function).

The concentration parameters represent mean total counts of a `1` or a `0`,
i.e.,

```none
concentration1 = alpha = mean * total_concentration
concentration0 = beta  = (1. - mean) * total_concentration
```

where `mean` in `(0, 1)` and `total_concentration` is a positive real number
representing a mean `total_count = concentration1 + concentration0`.

Distribution parameters are automatically broadcast in all functions; see
examples for details.

Warning: The samples can be zero due to finite precision.
This happens more often when some of the concentrations are very small.
Make sure to round the samples to `np.finfo(dtype).tiny` before computing the
density.

Samples of this distribution are reparameterized (pathwise differentiable).
The derivatives are computed using the approach described in
(Figurnov et al., 2018).

#### Examples

```python
import tensorflow_probability as tfp
tfd = tfp.distributions

# Create a batch of three Beta distributions.
alpha = [1, 2, 3]
beta = [1, 2, 3]
dist = tfd.Beta(alpha, beta)

dist.sample([4, 5])  # Shape [4, 5, 3]

# `x` has three batch entries, each with two samples.
x = [[.1, .4, .5],
     [.2, .3, .5]]
# Calculate the probability of each pair of samples under the corresponding
# distribution in `dist`.
dist.prob(x)         # Shape [2, 3]
```

```python
# Create batch_shape=[2, 3] via parameter broadcast:
alpha = [[1.], [2]]      # Shape [2, 1]
beta = [3., 4, 5]        # Shape [3]
dist = tfd.Beta(alpha, beta)

# alpha broadcast as: [[1., 1, 1,],
#                      [2, 2, 2]]
# beta broadcast as:  [[3., 4, 5],
#                      [3, 4, 5]]
# batch_Shape [2, 3]
dist.sample([4, 5])  # Shape [4, 5, 2, 3]

x = [.2, .3, .5]
# x will be broadcast as [[.2, .3, .5],
#                         [.2, .3, .5]],
# thus matching batch_shape [2, 3].
dist.prob(x)         # Shape [2, 3]
```

Compute the gradients of samples w.r.t. the parameters:

```python
alpha = tf.constant(1.0)
beta = tf.constant(2.0)
dist = tfd.Beta(alpha, beta)
samples = dist.sample(5)  # Shape [5]
loss = tf.reduce_mean(tf.square(samples))  # Arbitrary loss function
# Unbiased stochastic gradients of the loss function
grads = tf.gradients(loss, [alpha, beta])
```

#### References:

Implicit Reparameterization Gradients:
  [Figurnov et al., 2018]
  (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients)
  ([pdf]
  (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients.pdf))


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`concentration1`
</td>
<td>
Positive floating-point `Tensor` indicating mean
number of successes; aka "alpha". Implies `self.dtype` and
`self.batch_shape`, i.e.,
`concentration1.shape = [N1, N2, ..., Nm] = self.batch_shape`.
</td>
</tr><tr>
<td>
`concentration0`
</td>
<td>
Positive floating-point `Tensor` indicating mean
number of failures; aka "beta". Otherwise has same semantics as
`concentration1`.
</td>
</tr><tr>
<td>
`validate_args`
</td>
<td>
Python `bool`, default `False`. When `True` distribution
parameters are checked for validity despite possibly degrading runtime
performance. When `False` invalid inputs may silently render incorrect
outputs.
</td>
</tr><tr>
<td>
`allow_nan_stats`
</td>
<td>
Python `bool`, default `True`. When `True`, statistics
(e.g., mean, mode, variance) use the value "`NaN`" to indicate the
result is undefined. When `False`, an exception is raised if one or
more of the statistic's batch members are undefined.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` name prefixed to Ops created by this class.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`allow_nan_stats`
</td>
<td>
Python `bool` describing behavior when a stat is undefined.

Stats return +/- infinity when it makes sense. E.g., the variance of a
Cauchy distribution is infinity. However, sometimes the statistic is
undefined, e.g., if a distribution's pdf does not achieve a maximum within
the support of the distribution, the mode is undefined. If the mean is
undefined, then by definition the variance is undefined. E.g. the mean for
Student's T for df = 1 is undefined (no clear way to say it is either + or -
infinity), so the variance = E[(X - mean)**2] is also undefined.
</td>
</tr><tr>
<td>
`batch_shape`
</td>
<td>
Shape of a single sample from a single event index as a `TensorShape`.

May be partially defined or unknown.

The batch dimensions are indexes into independent, non-identical
parameterizations of this distribution.
</td>
</tr><tr>
<td>
`concentration0`
</td>
<td>
Concentration parameter associated with a `0` outcome.
</td>
</tr><tr>
<td>
`concentration1`
</td>
<td>
Concentration parameter associated with a `1` outcome.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The `DType` of `Tensor`s handled by this `Distribution`.
</td>
</tr><tr>
<td>
`event_shape`
</td>
<td>
Shape of a single sample from a single batch as a `TensorShape`.

May be partially defined or unknown.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name prepended to all ops created by this `Distribution`.
</td>
</tr><tr>
<td>
`parameters`
</td>
<td>
Dictionary of parameters used to instantiate this `Distribution`.
</td>
</tr><tr>
<td>
`reparameterization_type`
</td>
<td>
Describes how samples from the distribution are reparameterized.

Currently this is one of the static instances
`distributions.FULLY_REPARAMETERIZED`
or `distributions.NOT_REPARAMETERIZED`.
</td>
</tr><tr>
<td>
`total_concentration`
</td>
<td>
Sum of concentration parameters.
</td>
</tr><tr>
<td>
`validate_args`
</td>
<td>
Python `bool` indicating possibly expensive checks are enabled.
</td>
</tr>
</table>



## Methods

<h3 id="batch_shape_tensor"><code>batch_shape_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L637-L654">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_shape_tensor(
    name='batch_shape_tensor'
)
</code></pre>

Shape of a single sample from a single event index as a 1-D `Tensor`.

The batch dimensions are indexes into independent, non-identical
parameterizations of this distribution.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
name to give to the op
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`batch_shape`
</td>
<td>
`Tensor`.
</td>
</tr>
</table>



<h3 id="cdf"><code>cdf</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L881-L898">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cdf(
    value, name='cdf'
)
</code></pre>

Cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

```none
cdf(x) := P[X <= x]
```


Additional documentation from `Beta`:

Note: `x` must have dtype `self.dtype` and be in
`[0, 1].` It must have a shape compatible with `self.batch_shape()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
`float` or `double` `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`cdf`
</td>
<td>
a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
values of type `self.dtype`.
</td>
</tr>
</table>



<h3 id="copy"><code>copy</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L615-L631">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>copy(
    **override_parameters_kwargs
)
</code></pre>

Creates a deep copy of the distribution.

Note: the copy distribution may continue to depend on the original
initialization arguments.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`**override_parameters_kwargs`
</td>
<td>
String/value dictionary of initialization
arguments to override with new values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`distribution`
</td>
<td>
A new instance of `type(self)` initialized from the union
of self.parameters and override_parameters_kwargs, i.e.,
`dict(self.parameters, **override_parameters_kwargs)`.
</td>
</tr>
</table>



<h3 id="covariance"><code>covariance</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L1094-L1131">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>covariance(
    name='covariance'
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`covariance`
</td>
<td>
Floating-point `Tensor` with shape `[B1, ..., Bn, k', k']`
where the first `n` dimensions are batch coordinates and
`k' = reduce_prod(self.event_shape)`.
</td>
</tr>
</table>



<h3 id="cross_entropy"><code>cross_entropy</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L1146-L1169">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cross_entropy(
    other, name='cross_entropy'
)
</code></pre>

Computes the (Shannon) cross entropy.

Denote this distribution (`self`) by `P` and the `other` distribution by
`Q`. Assuming `P, Q` are absolutely continuous with respect to
one another and permit densities `p(x) dr(x)` and `q(x) dr(x)`, (Shanon)
cross entropy is defined as:

```none
H[P, Q] = E_p[-log q(X)] = -int_F p(x) log q(x) dr(x)
```

where `F` denotes the support of the random variable `X ~ P`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`other`
</td>
<td>
`tfp.distributions.Distribution` instance.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`cross_entropy`
</td>
<td>
`self.dtype` `Tensor` with shape `[B1, ..., Bn]`
representing `n` different calculations of (Shanon) cross entropy.
</td>
</tr>
</table>



<h3 id="entropy"><code>entropy</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L982-L985">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>entropy(
    name='entropy'
)
</code></pre>

Shannon entropy in nats.


<h3 id="event_shape_tensor"><code>event_shape_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L677-L691">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>event_shape_tensor(
    name='event_shape_tensor'
)
</code></pre>

Shape of a single sample from a single batch as a 1-D int32 `Tensor`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
name to give to the op
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`event_shape`
</td>
<td>
`Tensor`.
</td>
</tr>
</table>



<h3 id="is_scalar_batch"><code>is_scalar_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L721-L733">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_scalar_batch(
    name='is_scalar_batch'
)
</code></pre>

Indicates that `batch_shape == []`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`is_scalar_batch`
</td>
<td>
`bool` scalar `Tensor`.
</td>
</tr>
</table>



<h3 id="is_scalar_event"><code>is_scalar_event</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L707-L719">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_scalar_event(
    name='is_scalar_event'
)
</code></pre>

Indicates that `event_shape == []`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`is_scalar_event`
</td>
<td>
`bool` scalar `Tensor`.
</td>
</tr>
</table>



<h3 id="kl_divergence"><code>kl_divergence</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L1175-L1201">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>kl_divergence(
    other, name='kl_divergence'
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`other`
</td>
<td>
`tfp.distributions.Distribution` instance.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`kl_divergence`
</td>
<td>
`self.dtype` `Tensor` with shape `[B1, ..., Bn]`
representing `n` different calculations of the Kullback-Leibler
divergence.
</td>
</tr>
</table>



<h3 id="log_cdf"><code>log_cdf</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L842-L863">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>log_cdf(
    value, name='log_cdf'
)
</code></pre>

Log cumulative distribution function.

Given random variable `X`, the cumulative distribution function `cdf` is:

```none
log_cdf(x) := Log[ P[X <= x] ]
```

Often, a numerical approximation can be used for `log_cdf(x)` that yields
a more accurate answer than simply taking the logarithm of the `cdf` when
`x << -1`.


Additional documentation from `Beta`:

Note: `x` must have dtype `self.dtype` and be in
`[0, 1].` It must have a shape compatible with `self.batch_shape()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
`float` or `double` `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`logcdf`
</td>
<td>
a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
values of type `self.dtype`.
</td>
</tr>
</table>



<h3 id="log_prob"><code>log_prob</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L784-L795">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>log_prob(
    value, name='log_prob'
)
</code></pre>

Log probability density/mass function.


Additional documentation from `Beta`:

Note: `x` must have dtype `self.dtype` and be in
`[0, 1].` It must have a shape compatible with `self.batch_shape()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
`float` or `double` `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`log_prob`
</td>
<td>
a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
values of type `self.dtype`.
</td>
</tr>
</table>



<h3 id="log_survival_function"><code>log_survival_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L917-L939">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>log_survival_function(
    value, name='log_survival_function'
)
</code></pre>

Log survival function.

Given random variable `X`, the survival function is defined:

```none
log_survival_function(x) = Log[ P[X > x] ]
                         = Log[ 1 - P[X <= x] ]
                         = Log[ 1 - cdf(x) ]
```

Typically, different numerical approximations can be used for the log
survival function, which are more accurate than `1 - cdf(x)` when `x >> 1`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
`float` or `double` `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type
`self.dtype`.
</td>
</tr>

</table>



<h3 id="mean"><code>mean</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L991-L994">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>mean(
    name='mean'
)
</code></pre>

Mean.


<h3 id="mode"><code>mode</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L1137-L1140">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>mode(
    name='mode'
)
</code></pre>

Mode.

Additional documentation from `Beta`:

Note: The mode is undefined when `concentration1 <= 1` or
`concentration0 <= 1`. If `self.allow_nan_stats` is `True`, `NaN`
is used for undefined modes. If `self.allow_nan_stats` is `False` an
exception is raised when one or more modes are undefined.

<h3 id="param_shapes"><code>param_shapes</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L497-L516">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>param_shapes(
    sample_shape, name='DistributionParamShapes'
)
</code></pre>

Shapes of parameters given the desired shape of a call to `sample()`.

This is a class method that describes what key/value arguments are required
to instantiate the given `Distribution` so that a particular shape is
returned for that instance's call to `sample()`.

Subclasses should override class method `_param_shapes`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sample_shape`
</td>
<td>
`Tensor` or python list/tuple. Desired shape of a call to
`sample()`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
name to prepend ops with.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`dict` of parameter name to `Tensor` shapes.
</td>
</tr>

</table>



<h3 id="param_static_shapes"><code>param_static_shapes</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L518-L555">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>param_static_shapes(
    sample_shape
)
</code></pre>

param_shapes with static (i.e. `TensorShape`) shapes.

This is a class method that describes what key/value arguments are required
to instantiate the given `Distribution` so that a particular shape is
returned for that instance's call to `sample()`. Assumes that the sample's
shape is known statically.

Subclasses should override class method `_param_shapes` to return
constant-valued tensors when constant values are fed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sample_shape`
</td>
<td>
`TensorShape` or python list/tuple. Desired shape of a call
to `sample()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`dict` of parameter name to `TensorShape`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `sample_shape` is a `TensorShape` and is not fully defined.
</td>
</tr>
</table>



<h3 id="prob"><code>prob</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L813-L824">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>prob(
    value, name='prob'
)
</code></pre>

Probability density/mass function.


Additional documentation from `Beta`:

Note: `x` must have dtype `self.dtype` and be in
`[0, 1].` It must have a shape compatible with `self.batch_shape()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
`float` or `double` `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`prob`
</td>
<td>
a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
values of type `self.dtype`.
</td>
</tr>
</table>



<h3 id="quantile"><code>quantile</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L1006-L1023">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>quantile(
    value, name='quantile'
)
</code></pre>

Quantile function. Aka "inverse cdf" or "percent point function".

Given random variable `X` and `p in [0, 1]`, the `quantile` is:

```none
quantile(p) := x such that P[X <= x] == p
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
`float` or `double` `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`quantile`
</td>
<td>
a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
values of type `self.dtype`.
</td>
</tr>
</table>



<h3 id="sample"><code>sample</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L752-L766">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>sample(
    sample_shape=(), seed=None, name='sample'
)
</code></pre>

Generate samples of the specified shape.

Note that a call to `sample()` without arguments will generate a single
sample.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sample_shape`
</td>
<td>
0D or 1D `int32` `Tensor`. Shape of the generated samples.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Python integer seed for RNG
</td>
</tr><tr>
<td>
`name`
</td>
<td>
name to give to the op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`samples`
</td>
<td>
a `Tensor` with prepended dimensions `sample_shape`.
</td>
</tr>
</table>



<h3 id="stddev"><code>stddev</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L1061-L1088">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stddev(
    name='stddev'
)
</code></pre>

Standard deviation.

Standard deviation is defined as,

```none
stddev = E[(X - E[X])**2]**0.5
```

where `X` is the random variable associated with this distribution, `E`
denotes expectation, and `stddev.shape = batch_shape + event_shape`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`stddev`
</td>
<td>
Floating-point `Tensor` with shape identical to
`batch_shape + event_shape`, i.e., the same shape as `self.mean()`.
</td>
</tr>
</table>



<h3 id="survival_function"><code>survival_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L957-L976">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>survival_function(
    value, name='survival_function'
)
</code></pre>

Survival function.

Given random variable `X`, the survival function is defined:

```none
survival_function(x) = P[X > x]
                     = 1 - P[X <= x]
                     = 1 - cdf(x).
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
`float` or `double` `Tensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`Tensor` of shape `sample_shape(x) + self.batch_shape` with values of type
`self.dtype`.
</td>
</tr>

</table>



<h3 id="variance"><code>variance</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/distributions/distribution.py#L1029-L1055">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>variance(
    name='variance'
)
</code></pre>

Variance.

Variance is defined as,

```none
Var = E[(X - E[X])**2]
```

where `X` is the random variable associated with this distribution, `E`
denotes expectation, and `Var.shape = batch_shape + event_shape`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Python `str` prepended to names of ops created by this function.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`variance`
</td>
<td>
Floating-point `Tensor` with shape identical to
`batch_shape + event_shape`, i.e., the same shape as `self.mean()`.
</td>
</tr>
</table>





