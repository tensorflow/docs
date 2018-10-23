

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.distributions.bijectors



Defined in [`tensorflow/contrib/distributions/python/ops/bijectors/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/distributions/python/ops/bijectors/__init__.py).

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

[`class Identity`](../../../tf/distributions/bijectors/Identity): Compute Y = g(X) = X.

[`class Inline`](../../../tf/contrib/distributions/bijectors/Inline): Bijector constructed from custom callables.

[`class Invert`](../../../tf/contrib/distributions/bijectors/Invert): Bijector which inverts another Bijector.

[`class PowerTransform`](../../../tf/contrib/distributions/bijectors/PowerTransform): Compute `Y = g(X) = (1 + X * c)**(1 / c), X >= -1 / c`.

[`class Sigmoid`](../../../tf/contrib/distributions/bijectors/Sigmoid): Bijector which computes `Y = g(X) = 1 / (1 + exp(-X))`.

[`class SigmoidCentered`](../../../tf/contrib/distributions/bijectors/SigmoidCentered): Bijector which computes Y = g(X) = exp([X 0]) / (1 + exp(-X)).

[`class SinhArcsinh`](../../../tf/contrib/distributions/bijectors/SinhArcsinh): Compute `Y = g(X) = Sinh( (Arcsinh(X) + skewness) * tailweight )`.

[`class SoftmaxCentered`](../../../tf/contrib/distributions/bijectors/SoftmaxCentered): Bijector which computes `Y = g(X) = exp([X 0]) / sum(exp([X 0]))`.

[`class Softplus`](../../../tf/contrib/distributions/bijectors/Softplus): Bijector which computes `Y = g(X) = Log[1 + exp(X)]`.

