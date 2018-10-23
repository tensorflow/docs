

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.contrib.distributions

### Module `tf.contrib.distributions`



Defined in [`tensorflow/contrib/distributions/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/distributions/__init__.py).

Classes representing statistical distributions and ops for working with them.

See the [Statistical Distributions (contrib)](../../../../api_guides/python/contrib.distributions) guide.

## Distribution Object

## Individual Distributions






## Kullback-Leibler Divergence

## Helper Functions

## Classes

[`class Bernoulli`](../../tf/contrib/distributions/Bernoulli): Bernoulli distribution.

[`class BernoulliWithSigmoidProbs`](../../tf/contrib/distributions/BernoulliWithSigmoidProbs): Bernoulli with `probs = nn.sigmoid(logits)`.

[`class Beta`](../../tf/contrib/distributions/Beta): Beta distribution.

[`class BetaWithSoftplusConcentration`](../../tf/contrib/distributions/BetaWithSoftplusConcentration): Beta with softplus transform of `concentration1` and `concentration0`.

[`class Binomial`](../../tf/contrib/distributions/Binomial): Binomial distribution.

[`class Categorical`](../../tf/contrib/distributions/Categorical): Categorical distribution.

[`class Chi2`](../../tf/contrib/distributions/Chi2): Chi2 distribution.

[`class Chi2WithAbsDf`](../../tf/contrib/distributions/Chi2WithAbsDf): Chi2 with parameter transform `df = floor(abs(df))`.

[`class ConditionalDistribution`](../../tf/contrib/distributions/ConditionalDistribution): Distribution that supports intrinsic parameters (local latents).

[`class ConditionalTransformedDistribution`](../../tf/contrib/distributions/ConditionalTransformedDistribution): A TransformedDistribution that allows intrinsic conditioning.

[`class Deterministic`](../../tf/contrib/distributions/Deterministic): Scalar `Deterministic` distribution on the real line.

[`class Dirichlet`](../../tf/contrib/distributions/Dirichlet): Dirichlet distribution.

[`class DirichletMultinomial`](../../tf/contrib/distributions/DirichletMultinomial): Dirichlet-Multinomial compound distribution.

[`class Distribution`](../../tf/contrib/distributions/Distribution): A generic probability distribution base class.

[`class ExpRelaxedOneHotCategorical`](../../tf/contrib/distributions/ExpRelaxedOneHotCategorical): ExpRelaxedOneHotCategorical distribution with temperature and logits.

[`class Exponential`](../../tf/contrib/distributions/Exponential): Exponential distribution.

[`class ExponentialWithSoftplusRate`](../../tf/contrib/distributions/ExponentialWithSoftplusRate): Exponential with softplus transform on `rate`.

[`class Gamma`](../../tf/contrib/distributions/Gamma): Gamma distribution.

[`class GammaWithSoftplusConcentrationRate`](../../tf/contrib/distributions/GammaWithSoftplusConcentrationRate): `Gamma` with softplus of `concentration` and `rate`.

[`class Geometric`](../../tf/contrib/distributions/Geometric): Geometric distribution.

[`class InverseGamma`](../../tf/contrib/distributions/InverseGamma): InverseGamma distribution.

[`class InverseGammaWithSoftplusConcentrationRate`](../../tf/contrib/distributions/InverseGammaWithSoftplusConcentrationRate): `InverseGamma` with softplus of `concentration` and `rate`.

[`class Laplace`](../../tf/contrib/distributions/Laplace): The Laplace distribution with location `loc` and `scale` parameters.

[`class LaplaceWithSoftplusScale`](../../tf/contrib/distributions/LaplaceWithSoftplusScale): Laplace with softplus applied to `scale`.

[`class Logistic`](../../tf/contrib/distributions/Logistic): The Logistic distribution with location `loc` and `scale` parameters.

[`class Mixture`](../../tf/contrib/distributions/Mixture): Mixture distribution.

[`class Multinomial`](../../tf/contrib/distributions/Multinomial): Multinomial distribution.

[`class MultivariateNormalDiag`](../../tf/contrib/distributions/MultivariateNormalDiag): The multivariate normal distribution on `R^k`.

[`class MultivariateNormalDiagPlusLowRank`](../../tf/contrib/distributions/MultivariateNormalDiagPlusLowRank): The multivariate normal distribution on `R^k`.

[`class MultivariateNormalDiagWithSoftplusScale`](../../tf/contrib/distributions/MultivariateNormalDiagWithSoftplusScale): MultivariateNormalDiag with `diag_stddev = softplus(diag_stddev)`.

[`class MultivariateNormalTriL`](../../tf/contrib/distributions/MultivariateNormalTriL): The multivariate normal distribution on `R^k`.

[`class NegativeBinomial`](../../tf/contrib/distributions/NegativeBinomial): NegativeBinomial distribution.

[`class Normal`](../../tf/contrib/distributions/Normal): The Normal distribution with location `loc` and `scale` parameters.

[`class NormalWithSoftplusScale`](../../tf/contrib/distributions/NormalWithSoftplusScale): Normal with softplus applied to `scale`.

[`class OneHotCategorical`](../../tf/contrib/distributions/OneHotCategorical): OneHotCategorical distribution.

[`class Poisson`](../../tf/contrib/distributions/Poisson): Poisson distribution.

[`class QuantizedDistribution`](../../tf/contrib/distributions/QuantizedDistribution): Distribution representing the quantization `Y = ceiling(X)`.

[`class RegisterKL`](../../tf/contrib/distributions/RegisterKL): Decorator to register a KL divergence implementation function.

[`class RelaxedBernoulli`](../../tf/contrib/distributions/RelaxedBernoulli): RelaxedBernoulli distribution with temperature and logits parameters.

[`class RelaxedOneHotCategorical`](../../tf/contrib/distributions/RelaxedOneHotCategorical): RelaxedOneHotCategorical distribution with temperature and logits.

[`class ReparameterizationType`](../../tf/contrib/distributions/ReparameterizationType): Instances of this class represent how sampling is reparameterized.

[`class StudentT`](../../tf/contrib/distributions/StudentT): Student's t-distribution with degree of freedom `df`, location `loc`, and `scale` parameters.

[`class StudentTWithAbsDfSoftplusScale`](../../tf/contrib/distributions/StudentTWithAbsDfSoftplusScale): StudentT with `df = floor(abs(df))` and `scale = softplus(scale)`.

[`class TransformedDistribution`](../../tf/contrib/distributions/TransformedDistribution): A Transformed Distribution.

[`class Uniform`](../../tf/contrib/distributions/Uniform): Uniform distribution with `low` and `high` parameters.

[`class VectorDeterministic`](../../tf/contrib/distributions/VectorDeterministic): Vector `Deterministic` distribution on `R^k`.

[`class WishartCholesky`](../../tf/contrib/distributions/WishartCholesky): The matrix Wishart distribution on positive definite matrices.

[`class WishartFull`](../../tf/contrib/distributions/WishartFull): The matrix Wishart distribution on positive definite matrices.

## Functions

[`kl(...)`](../../tf/contrib/distributions/kl): Get the KL-divergence KL(dist_a || dist_b).

[`matrix_diag_transform(...)`](../../tf/contrib/distributions/matrix_diag_transform): Transform diagonal of [batch-]matrix, leave rest of matrix unchanged.

[`normal_conjugates_known_scale_posterior(...)`](../../tf/contrib/distributions/normal_conjugates_known_scale_posterior): Posterior Normal distribution with conjugate prior on the mean.

[`normal_conjugates_known_scale_predictive(...)`](../../tf/contrib/distributions/normal_conjugates_known_scale_predictive): Posterior predictive Normal distribution w. conjugate prior on the mean.

[`softplus_inverse(...)`](../../tf/contrib/distributions/softplus_inverse): Computes the inverse softplus, i.e., x = softplus_inverse(softplus(x)).

## Other Members

`FULLY_REPARAMETERIZED`

`NOT_REPARAMETERIZED`

