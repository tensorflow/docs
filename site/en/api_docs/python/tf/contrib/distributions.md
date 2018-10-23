


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.contrib.distributions

### Module `tf.contrib.distributions`

Classes representing statistical distributions and ops for working with them.

See the [Statistical Distributions (contrib)](../../../../api_guides/python/contrib.distributions) guide.












## Members

[`class Bernoulli`](../../tf/contrib/distributions/Bernoulli): Bernoulli distribution.

[`class BernoulliWithSigmoidP`](../../tf/contrib/distributions/BernoulliWithSigmoidP): Bernoulli with `p = sigmoid(p)`.

[`class Beta`](../../tf/contrib/distributions/Beta): Beta distribution.

[`class BetaWithSoftplusAB`](../../tf/contrib/distributions/BetaWithSoftplusAB): Beta with softplus transform on `a` and `b`.

[`class Binomial`](../../tf/contrib/distributions/Binomial): Binomial distribution.

[`class Categorical`](../../tf/contrib/distributions/Categorical): Categorical distribution.

[`class Chi2`](../../tf/contrib/distributions/Chi2): The Chi2 distribution with degrees of freedom df.

[`class Chi2WithAbsDf`](../../tf/contrib/distributions/Chi2WithAbsDf): Chi2 with parameter transform `df = floor(abs(df))`.

[`class Dirichlet`](../../tf/contrib/distributions/Dirichlet): Dirichlet distribution.

[`class DirichletMultinomial`](../../tf/contrib/distributions/DirichletMultinomial): DirichletMultinomial mixture distribution.

[`class Distribution`](../../tf/contrib/distributions/Distribution): A generic probability distribution base class.

[`class Exponential`](../../tf/contrib/distributions/Exponential): The Exponential distribution with rate parameter lam.

[`class ExponentialWithSoftplusLam`](../../tf/contrib/distributions/ExponentialWithSoftplusLam): Exponential with softplus transform on `lam`.

[`class Gamma`](../../tf/contrib/distributions/Gamma): The `Gamma` distribution with parameter alpha and beta.

[`class GammaWithSoftplusAlphaBeta`](../../tf/contrib/distributions/GammaWithSoftplusAlphaBeta): Gamma with softplus transform on `alpha` and `beta`.

[`class InverseGamma`](../../tf/contrib/distributions/InverseGamma): The `InverseGamma` distribution with parameter alpha and beta.

[`class InverseGammaWithSoftplusAlphaBeta`](../../tf/contrib/distributions/InverseGammaWithSoftplusAlphaBeta): Inverse Gamma with softplus applied to `alpha` and `beta`.

[`class Laplace`](../../tf/contrib/distributions/Laplace): The Laplace distribution with location and scale > 0 parameters.

[`class LaplaceWithSoftplusScale`](../../tf/contrib/distributions/LaplaceWithSoftplusScale): Laplace with softplus applied to `scale`.

[`class Mixture`](../../tf/contrib/distributions/Mixture): Mixture distribution.

[`class Multinomial`](../../tf/contrib/distributions/Multinomial): Multinomial distribution.

[`class MultivariateNormalCholesky`](../../tf/contrib/distributions/MultivariateNormalCholesky): The multivariate normal distribution on `R^k`.

[`class MultivariateNormalDiag`](../../tf/contrib/distributions/MultivariateNormalDiag): The multivariate normal distribution on `R^k`.

[`class MultivariateNormalDiagPlusVDVT`](../../tf/contrib/distributions/MultivariateNormalDiagPlusVDVT): The multivariate normal distribution on `R^k`.

[`class MultivariateNormalDiagWithSoftplusStDev`](../../tf/contrib/distributions/MultivariateNormalDiagWithSoftplusStDev): MultivariateNormalDiag with `diag_stddev = softplus(diag_stddev)`.

[`class MultivariateNormalFull`](../../tf/contrib/distributions/MultivariateNormalFull): The multivariate normal distribution on `R^k`.

[`class Normal`](../../tf/contrib/distributions/Normal): The scalar Normal distribution with mean and stddev parameters mu, sigma.

[`class NormalWithSoftplusSigma`](../../tf/contrib/distributions/NormalWithSoftplusSigma): Normal with softplus applied to `sigma`.

[`class Poisson`](../../tf/contrib/distributions/Poisson): Poisson distribution.

[`class QuantizedDistribution`](../../tf/contrib/distributions/QuantizedDistribution): Distribution representing the quantization `Y = ceiling(X)`.

[`class RegisterKL`](../../tf/contrib/distributions/RegisterKL): Decorator to register a KL divergence implementation function.

[`class StudentT`](../../tf/contrib/distributions/StudentT): Student's t distribution with degree-of-freedom parameter df.

[`class StudentTWithAbsDfSoftplusSigma`](../../tf/contrib/distributions/StudentTWithAbsDfSoftplusSigma): StudentT with `df = floor(abs(df))` and `sigma = softplus(sigma)`.

[`class TransformedDistribution`](../../tf/contrib/distributions/TransformedDistribution): A Transformed Distribution.

[`class Uniform`](../../tf/contrib/distributions/Uniform): Uniform distribution with `a` and `b` parameters.

[`class WishartCholesky`](../../tf/contrib/distributions/WishartCholesky): The matrix Wishart distribution on positive definite matrices.

[`class WishartFull`](../../tf/contrib/distributions/WishartFull): The matrix Wishart distribution on positive definite matrices.

[`bijector`](../../tf/contrib/distributions/bijector) module: Bijector Ops. See the [Random variable transformations (contrib)](../../../../api_guides/python/contrib.distributions.bijector) guide.

[`kl(...)`](../../tf/contrib/distributions/kl): Get the KL-divergence KL(dist_a || dist_b).

[`matrix_diag_transform(...)`](../../tf/contrib/distributions/matrix_diag_transform): Transform diagonal of [batch-]matrix, leave rest of matrix unchanged.

[`normal_conjugates_known_sigma_posterior(...)`](../../tf/contrib/distributions/normal_conjugates_known_sigma_posterior): Posterior Normal distribution with conjugate prior on the mean.

[`normal_conjugates_known_sigma_predictive(...)`](../../tf/contrib/distributions/normal_conjugates_known_sigma_predictive): Posterior predictive Normal distribution w. conjugate prior on the mean.

[`softplus_inverse(...)`](../../tf/contrib/distributions/softplus_inverse): Computes the inverse softplus, i.e., x = softplus_inverse(softplus(x)).

Defined in [`tensorflow/contrib/distributions/__init__.py`](https://www.tensorflow.org/code/tensorflow/contrib/distributions/__init__.py).

