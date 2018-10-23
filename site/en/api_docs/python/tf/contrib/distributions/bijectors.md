

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.distributions.bijectors



Defined in [`tensorflow/contrib/distributions/python/ops/bijectors/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/distributions/python/ops/bijectors/__init__.py).

Bijector Ops.



## Classes

[`class AbsoluteValue`](../../../tf/contrib/distributions/bijectors/AbsoluteValue): Computes `Y = g(X) = Abs(X)`, element-wise.

[`class Affine`](../../../tf/contrib/distributions/bijectors/Affine): Compute `Y = g(X; shift, scale) = scale @ X + shift`.

[`class AffineLinearOperator`](../../../tf/contrib/distributions/bijectors/AffineLinearOperator): Compute `Y = g(X; shift, scale) = scale @ X + shift`.

[`class Bijector`](../../../tf/distributions/bijectors/Bijector): Interface for transformations of a `Distribution` sample.

[`class Chain`](../../../tf/contrib/distributions/bijectors/Chain): Bijector which applies a sequence of bijectors.

[`class CholeskyOuterProduct`](../../../tf/contrib/distributions/bijectors/CholeskyOuterProduct): Compute `g(X) = X @ X.T`; X is lower-triangular, positive-diagonal matrix.

[`class ConditionalBijector`](../../../tf/contrib/distributions/bijectors/ConditionalBijector): Conditional Bijector is a Bijector that allows intrinsic conditioning.

[`class Exp`](../../../tf/contrib/distributions/bijectors/Exp): Compute `Y = g(X) = exp(X)`.

[`class Gumbel`](../../../tf/contrib/distributions/bijectors/Gumbel): Compute `Y = g(X) = exp(-exp(-(X - loc) / scale))`.

[`class Identity`](../../../tf/distributions/bijectors/Identity): Compute Y = g(X) = X.

[`class Inline`](../../../tf/contrib/distributions/bijectors/Inline): Bijector constructed from custom callables.

[`class Invert`](../../../tf/contrib/distributions/bijectors/Invert): Bijector which inverts another Bijector.

[`class MaskedAutoregressiveFlow`](../../../tf/contrib/distributions/bijectors/MaskedAutoregressiveFlow): Affine MaskedAutoregressiveFlow bijector for vector-valued events.

[`class Permute`](../../../tf/contrib/distributions/bijectors/Permute): Permutes the rightmost dimension of a `Tensor`.

[`class PowerTransform`](../../../tf/contrib/distributions/bijectors/PowerTransform): Compute `Y = g(X) = (1 + X * c)**(1 / c), X >= -1 / c`.

[`class RealNVP`](../../../tf/contrib/distributions/bijectors/RealNVP): RealNVP "affine coupling layer" for vector-valued events.

[`class Reshape`](../../../tf/contrib/distributions/bijectors/Reshape): Reshapes the `event_shape` of a `Tensor`.

[`class Sigmoid`](../../../tf/contrib/distributions/bijectors/Sigmoid): Bijector which computes `Y = g(X) = 1 / (1 + exp(-X))`.

[`class SigmoidCentered`](../../../tf/contrib/distributions/bijectors/SigmoidCentered): Bijector which computes Y = g(X) = exp([X 0]) / (1 + exp(-X)).

[`class SinhArcsinh`](../../../tf/contrib/distributions/bijectors/SinhArcsinh): Compute `Y = g(X) = Sinh( (Arcsinh(X) + skewness) * tailweight )`.

[`class SoftmaxCentered`](../../../tf/contrib/distributions/bijectors/SoftmaxCentered): Bijector which computes `Y = g(X) = exp([X 0]) / sum(exp([X 0]))`.

[`class Softplus`](../../../tf/contrib/distributions/bijectors/Softplus): Bijector which computes `Y = g(X) = Log[1 + exp(X)]`.

## Functions

[`masked_autoregressive_default_template(...)`](../../../tf/contrib/distributions/bijectors/masked_autoregressive_default_template): Build the MADE Model [1].

[`masked_dense(...)`](../../../tf/contrib/distributions/bijectors/masked_dense): A autoregressively masked dense layer. Analogous to `tf.layers.dense`.

[`real_nvp_default_template(...)`](../../../tf/contrib/distributions/bijectors/real_nvp_default_template): Build a scale-and-shift function using a multi-layer neural network.

