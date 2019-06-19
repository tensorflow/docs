page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.distributions.bijectors



Defined in [`tensorflow/contrib/distributions/python/ops/bijectors/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/distributions/python/ops/bijectors/__init__.py).

Bijector Ops.



## Classes

[`class AbsoluteValue`](../../../tf/contrib/distributions/bijectors/AbsoluteValue): Computes `Y = g(X) = Abs(X)`, element-wise.

[`class Affine`](../../../tf/contrib/distributions/bijectors/Affine): Compute `Y = g(X; shift, scale) = scale @ X + shift`.

[`class AffineLinearOperator`](../../../tf/contrib/distributions/bijectors/AffineLinearOperator): Compute `Y = g(X; shift, scale) = scale @ X + shift`.

[`class AffineScalar`](../../../tf/contrib/distributions/bijectors/AffineScalar): Compute `Y = g(X; shift, scale) = scale * X + shift`.

[`class BatchNormalization`](../../../tf/contrib/distributions/bijectors/BatchNormalization): Compute `Y = g(X) s.t. X = g^-1(Y) = (Y - mean(Y)) / std(Y)`.

[`class Bijector`](../../../tf/contrib/distributions/bijectors/Bijector): Interface for transformations of a `Distribution` sample.

[`class Chain`](../../../tf/contrib/distributions/bijectors/Chain): Bijector which applies a sequence of bijectors.

[`class CholeskyOuterProduct`](../../../tf/contrib/distributions/bijectors/CholeskyOuterProduct): Compute `g(X) = X @ X.T`; X is lower-triangular, positive-diagonal matrix.

[`class ConditionalBijector`](../../../tf/contrib/distributions/bijectors/ConditionalBijector): Conditional Bijector is a Bijector that allows intrinsic conditioning.

[`class Exp`](../../../tf/contrib/distributions/bijectors/Exp): Compute `Y = g(X) = exp(X)`.

[`class Gumbel`](../../../tf/contrib/distributions/bijectors/Gumbel): Compute `Y = g(X) = exp(-exp(-(X - loc) / scale))`.

[`class Identity`](../../../tf/contrib/distributions/bijectors/Identity): Compute Y = g(X) = X.

[`class Inline`](../../../tf/contrib/distributions/bijectors/Inline): Bijector constructed from custom callables.

[`class Invert`](../../../tf/contrib/distributions/bijectors/Invert): Bijector which inverts another Bijector.

[`class Kumaraswamy`](../../../tf/contrib/distributions/bijectors/Kumaraswamy): Compute `Y = g(X) = (1 - (1 - X)**(1 / b))**(1 / a), X in [0, 1]`.

[`class MaskedAutoregressiveFlow`](../../../tf/contrib/distributions/bijectors/MaskedAutoregressiveFlow): Affine MaskedAutoregressiveFlow bijector for vector-valued events.

[`class MatrixInverseTriL`](../../../tf/contrib/distributions/bijectors/MatrixInverseTriL): Computes `g(L) = inv(L)`, where `L` is a lower-triangular matrix.

[`class Ordered`](../../../tf/contrib/distributions/bijectors/Ordered): Bijector which maps a tensor x_k that has increasing elements in the last

[`class Permute`](../../../tf/contrib/distributions/bijectors/Permute): Permutes the rightmost dimension of a `Tensor`.

[`class PowerTransform`](../../../tf/contrib/distributions/bijectors/PowerTransform): Compute `Y = g(X) = (1 + X * c)**(1 / c), X >= -1 / c`.

[`class RealNVP`](../../../tf/contrib/distributions/bijectors/RealNVP): RealNVP "affine coupling layer" for vector-valued events.

[`class Reshape`](../../../tf/contrib/distributions/bijectors/Reshape): Reshapes the `event_shape` of a `Tensor`.

[`class Sigmoid`](../../../tf/contrib/distributions/bijectors/Sigmoid): Bijector which computes `Y = g(X) = 1 / (1 + exp(-X))`.

[`class SinhArcsinh`](../../../tf/contrib/distributions/bijectors/SinhArcsinh): Compute `Y = g(X) = Sinh( (Arcsinh(X) + skewness) * tailweight )`.

[`class SoftmaxCentered`](../../../tf/contrib/distributions/bijectors/SoftmaxCentered): Bijector which computes `Y = g(X) = exp([X 0]) / sum(exp([X 0]))`.

[`class Softplus`](../../../tf/contrib/distributions/bijectors/Softplus): Bijector which computes `Y = g(X) = Log[1 + exp(X)]`.

[`class Softsign`](../../../tf/contrib/distributions/bijectors/Softsign): Bijector which computes `Y = g(X) = X / (1 + |X|)`.

[`class Square`](../../../tf/contrib/distributions/bijectors/Square): Compute `g(X) = X^2`; X is a positive real number.

## Functions

[`masked_autoregressive_default_template(...)`](../../../tf/contrib/distributions/bijectors/masked_autoregressive_default_template): Build the Masked Autoregressive Density Estimator (Germain et al., 2015).

[`masked_dense(...)`](../../../tf/contrib/distributions/bijectors/masked_dense): A autoregressively masked dense layer. Analogous to <a href="../../../tf/layers/dense"><code>tf.layers.dense</code></a>.

[`real_nvp_default_template(...)`](../../../tf/contrib/distributions/bijectors/real_nvp_default_template): Build a scale-and-shift function using a multi-layer neural network.

