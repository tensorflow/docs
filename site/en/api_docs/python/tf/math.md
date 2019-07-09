page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.math





Basic arithmetic operators.

See the [python/math_ops](python/math_ops) guide.

## Functions

[`abs(...)`](../tf/math/abs): Computes the absolute value of a tensor.

[`accumulate_n(...)`](../tf/math/accumulate_n): Returns the element-wise sum of a list of tensors.

[`acos(...)`](../tf/math/acos): Computes acos of x element-wise.

[`acosh(...)`](../tf/math/acosh): Computes inverse hyperbolic cosine of x element-wise.

[`add(...)`](../tf/math/add): Returns x + y element-wise.

[`add_n(...)`](../tf/math/add_n): Adds all input tensors element-wise.

[`angle(...)`](../tf/math/angle): Returns the element-wise argument of a complex (or real) tensor.

[`argmax(...)`](../tf/math/argmax): Returns the index with the largest value across axes of a tensor. (deprecated arguments)

[`argmin(...)`](../tf/math/argmin): Returns the index with the smallest value across axes of a tensor. (deprecated arguments)

[`asin(...)`](../tf/math/asin): Computes asin of x element-wise.

[`asinh(...)`](../tf/math/asinh): Computes inverse hyperbolic sine of x element-wise.

[`atan(...)`](../tf/math/atan): Computes atan of x element-wise.

[`atan2(...)`](../tf/math/atan2): Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

[`atanh(...)`](../tf/math/atanh): Computes inverse hyperbolic tangent of x element-wise.

[`bessel_i0(...)`](../tf/math/bessel_i0): Computes the Bessel i0 function of `x` element-wise.

[`bessel_i0e(...)`](../tf/math/bessel_i0e): Computes the Bessel i0e function of `x` element-wise.

[`bessel_i1(...)`](../tf/math/bessel_i1): Computes the Bessel i1 function of `x` element-wise.

[`bessel_i1e(...)`](../tf/math/bessel_i1e): Computes the Bessel i1e function of `x` element-wise.

[`betainc(...)`](../tf/math/betainc): Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

[`bincount(...)`](../tf/math/bincount): Counts the number of occurrences of each value in an integer array.

[`ceil(...)`](../tf/math/ceil): Returns element-wise smallest integer not less than x.

[`confusion_matrix(...)`](../tf/math/confusion_matrix): Computes the confusion matrix from predictions and labels.

[`conj(...)`](../tf/math/conj): Returns the complex conjugate of a complex number.

[`cos(...)`](../tf/math/cos): Computes cos of x element-wise.

[`cosh(...)`](../tf/math/cosh): Computes hyperbolic cosine of x element-wise.

[`count_nonzero(...)`](../tf/math/count_nonzero): Computes number of nonzero elements across dimensions of a tensor. (deprecated arguments)

[`cumprod(...)`](../tf/math/cumprod): Compute the cumulative product of the tensor `x` along `axis`.

[`cumsum(...)`](../tf/math/cumsum): Compute the cumulative sum of the tensor `x` along `axis`.

[`digamma(...)`](../tf/math/digamma): Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`divide(...)`](../tf/math/divide): Computes Python style division of `x` by `y`.

[`equal(...)`](../tf/math/equal): Returns the truth value of (x == y) element-wise.

[`erf(...)`](../tf/math/erf): Computes the Gauss error function of `x` element-wise.

[`erfc(...)`](../tf/math/erfc): Computes the complementary error function of `x` element-wise.

[`exp(...)`](../tf/math/exp): Computes exponential of x element-wise.  \\(y = e^x\\).

[`expm1(...)`](../tf/math/expm1): Computes exponential of x - 1 element-wise.

[`floor(...)`](../tf/math/floor): Returns element-wise largest integer not greater than x.

[`floordiv(...)`](../tf/math/floordiv): Divides `x / y` elementwise, rounding toward the most negative integer.

[`greater(...)`](../tf/math/greater): Returns the truth value of (x > y) element-wise.

[`greater_equal(...)`](../tf/math/greater_equal): Returns the truth value of (x >= y) element-wise.

[`igamma(...)`](../tf/math/igamma): Compute the lower regularized incomplete Gamma function `P(a, x)`.

[`igammac(...)`](../tf/math/igammac): Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`imag(...)`](../tf/math/imag): Returns the imaginary part of a complex (or real) tensor.

[`in_top_k(...)`](../tf/math/in_top_k): Says whether the targets are in the top `K` predictions.

[`invert_permutation(...)`](../tf/math/invert_permutation): Computes the inverse permutation of a tensor.

[`is_finite(...)`](../tf/math/is_finite): Returns which elements of x are finite.

[`is_inf(...)`](../tf/math/is_inf): Returns which elements of x are Inf.

[`is_nan(...)`](../tf/math/is_nan): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](../tf/math/is_non_decreasing): Returns `True` if `x` is non-decreasing.

[`is_strictly_increasing(...)`](../tf/math/is_strictly_increasing): Returns `True` if `x` is strictly increasing.

[`l2_normalize(...)`](../tf/math/l2_normalize): Normalizes along dimension `axis` using an L2 norm. (deprecated arguments)

[`lbeta(...)`](../tf/math/lbeta): Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

[`less(...)`](../tf/math/less): Returns the truth value of (x < y) element-wise.

[`less_equal(...)`](../tf/math/less_equal): Returns the truth value of (x <= y) element-wise.

[`lgamma(...)`](../tf/math/lgamma): Computes the log of the absolute value of `Gamma(x)` element-wise.

[`log(...)`](../tf/math/log): Computes natural logarithm of x element-wise.

[`log1p(...)`](../tf/math/log1p): Computes natural logarithm of (1 + x) element-wise.

[`log_sigmoid(...)`](../tf/math/log_sigmoid): Computes log sigmoid of `x` element-wise.

[`log_softmax(...)`](../tf/nn/log_softmax): Computes log softmax activations. (deprecated arguments)

[`logical_and(...)`](../tf/math/logical_and): Returns the truth value of x AND y element-wise.

[`logical_not(...)`](../tf/math/logical_not): Returns the truth value of NOT x element-wise.

[`logical_or(...)`](../tf/math/logical_or): Returns the truth value of x OR y element-wise.

[`logical_xor(...)`](../tf/math/logical_xor): x ^ y = (x | y) & ~(x & y).

[`maximum(...)`](../tf/math/maximum): Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`minimum(...)`](../tf/math/minimum): Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`multiply(...)`](../tf/math/multiply): Returns x * y element-wise.

[`negative(...)`](../tf/math/negative): Computes numerical negative value element-wise.

[`not_equal(...)`](../tf/math/not_equal): Returns the truth value of (x != y) element-wise.

[`polygamma(...)`](../tf/math/polygamma): Compute the polygamma function \\(\psi^{(n)} (x)\\).

[`polyval(...)`](../tf/math/polyval): Computes the elementwise value of a polynomial.

[`pow(...)`](../tf/math/pow): Computes the power of one value to another.

[`real(...)`](../tf/math/real): Returns the real part of a complex (or real) tensor.

[`reciprocal(...)`](../tf/math/reciprocal): Computes the reciprocal of x element-wise.

[`reduce_all(...)`](../tf/math/reduce_all): Computes the "logical and" of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_any(...)`](../tf/math/reduce_any): Computes the "logical or" of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_logsumexp(...)`](../tf/math/reduce_logsumexp): Computes log(sum(exp(elements across dimensions of a tensor))). (deprecated arguments)

[`reduce_max(...)`](../tf/math/reduce_max): Computes the maximum of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_mean(...)`](../tf/math/reduce_mean): Computes the mean of elements across dimensions of a tensor.

[`reduce_min(...)`](../tf/math/reduce_min): Computes the minimum of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_prod(...)`](../tf/math/reduce_prod): Computes the product of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_std(...)`](../tf/math/reduce_std): Computes the standard deviation of elements across dimensions of a tensor.

[`reduce_sum(...)`](../tf/math/reduce_sum): Computes the sum of elements across dimensions of a tensor. (deprecated arguments)

[`reduce_variance(...)`](../tf/math/reduce_variance): Computes the variance of elements across dimensions of a tensor.

[`rint(...)`](../tf/math/rint): Returns element-wise integer closest to x.

[`round(...)`](../tf/math/round): Rounds the values of a tensor to the nearest integer, element-wise.

[`rsqrt(...)`](../tf/math/rsqrt): Computes reciprocal of square root of x element-wise.

[`scalar_mul(...)`](../tf/math/scalar_mul): Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

[`segment_max(...)`](../tf/math/segment_max): Computes the maximum along segments of a tensor.

[`segment_mean(...)`](../tf/math/segment_mean): Computes the mean along segments of a tensor.

[`segment_min(...)`](../tf/math/segment_min): Computes the minimum along segments of a tensor.

[`segment_prod(...)`](../tf/math/segment_prod): Computes the product along segments of a tensor.

[`segment_sum(...)`](../tf/math/segment_sum): Computes the sum along segments of a tensor.

[`sigmoid(...)`](../tf/math/sigmoid): Computes sigmoid of `x` element-wise.

[`sign(...)`](../tf/math/sign): Returns an element-wise indication of the sign of a number.

[`sin(...)`](../tf/math/sin): Computes sin of x element-wise.

[`sinh(...)`](../tf/math/sinh): Computes hyperbolic sine of x element-wise.

[`softmax(...)`](../tf/nn/softmax): Computes softmax activations. (deprecated arguments)

[`softplus(...)`](../tf/math/softplus): Computes softplus: `log(exp(features) + 1)`.

[`softsign(...)`](../tf/nn/softsign): Computes softsign: `features / (abs(features) + 1)`.

[`sqrt(...)`](../tf/math/sqrt): Computes square root of x element-wise.

[`square(...)`](../tf/math/square): Computes square of x element-wise.

[`squared_difference(...)`](../tf/math/squared_difference): Returns (x - y)(x - y) element-wise.

[`subtract(...)`](../tf/math/subtract): Returns x - y element-wise.

[`tan(...)`](../tf/math/tan): Computes tan of x element-wise.

[`tanh(...)`](../tf/math/tanh): Computes hyperbolic tangent of `x` element-wise.

[`top_k(...)`](../tf/math/top_k): Finds values and indices of the `k` largest entries for the last dimension.

[`truediv(...)`](../tf/math/truediv): Divides x / y elementwise (using Python 3 division operator semantics).

[`unsorted_segment_max(...)`](../tf/math/unsorted_segment_max): Computes the maximum along segments of a tensor.

[`unsorted_segment_mean(...)`](../tf/math/unsorted_segment_mean): Computes the mean along segments of a tensor.

[`unsorted_segment_min(...)`](../tf/math/unsorted_segment_min): Computes the minimum along segments of a tensor.

[`unsorted_segment_prod(...)`](../tf/math/unsorted_segment_prod): Computes the product along segments of a tensor.

[`unsorted_segment_sqrt_n(...)`](../tf/math/unsorted_segment_sqrt_n): Computes the sum along segments of a tensor divided by the sqrt(N).

[`unsorted_segment_sum(...)`](../tf/math/unsorted_segment_sum): Computes the sum along segments of a tensor.

[`xdivy(...)`](../tf/math/xdivy): Returns 0 if x == 0, and x / y otherwise, elementwise.

[`xlogy(...)`](../tf/math/xlogy): Returns 0 if x == 0, and x * log(y) otherwise, elementwise.

[`zero_fraction(...)`](../tf/math/zero_fraction): Returns the fraction of zeros in `value`.

[`zeta(...)`](../tf/math/zeta): Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

