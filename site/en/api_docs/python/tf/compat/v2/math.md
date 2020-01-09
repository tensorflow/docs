page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.math


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Math Operations.

<!-- Placeholder for "Used in" -->

Note: Functions taking `Tensor` arguments can also take anything accepted by
<a href="../../../tf/convert_to_tensor"><code>tf.convert_to_tensor</code></a>.

Note: Elementwise binary operations in TensorFlow follow [numpy-style
broadcasting](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

TensorFlow provides a variety of math functions including:

* Basic arithmetic operators and trigonometric functions.
* Special math functions (like: <a href="../../../tf/math/igamma"><code>tf.math.igamma</code></a> and <a href="../../../tf/math/zeta"><code>tf.math.zeta</code></a>)
* Complex number functions (like: <a href="../../../tf/math/imag"><code>tf.math.imag</code></a> and <a href="../../../tf/math/angle"><code>tf.math.angle</code></a>)
* Reductions and scans (like: <a href="../../../tf/math/reduce_mean"><code>tf.math.reduce_mean</code></a> and <a href="../../../tf/math/cumsum"><code>tf.math.cumsum</code></a>)
* Segment functions (like: <a href="../../../tf/math/segment_sum"><code>tf.math.segment_sum</code></a>)

See: <a href="../../../tf/linalg"><code>tf.linalg</code></a> for matrix and tensor functions.

<a id=Segmentation></a>

## About Segmentation

TensorFlow provides several operations that you can use to perform common
math computations on tensor segments.
Here a segmentation is a partitioning of a tensor along
the first dimension, i.e. it  defines a mapping from the first dimension onto
`segment_ids`. The `segment_ids` tensor should be the size of
the first dimension, `d0`, with consecutive IDs in the range `0` to `k`,
where `k<d0`.
In particular, a segmentation of a matrix tensor is a mapping of rows to
segments.

#### For example:



```python
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])
tf.math.segment_sum(c, tf.constant([0, 0, 1]))
#  ==>  [[0 0 0 0]
#        [5 6 7 8]]
```

The standard `segment_*` functions assert that the segment indices are sorted.
If you have unsorted indices use the equivalent `unsorted_segment_` function.
Thses functions take an additional argument `num_segments` so that the output
tensor can be efficiently allocated.

``` python
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])
tf.math.unsorted_segment_sum(c, tf.constant([0, 1, 0]), num_segments=2)
# ==> [[ 6,  8, 10, 12],
#       [-1, -2, -3, -4]]
```

## Functions

[`abs(...)`](../../../tf/math/abs): Computes the absolute value of a tensor.

[`accumulate_n(...)`](../../../tf/math/accumulate_n): Returns the element-wise sum of a list of tensors.

[`acos(...)`](../../../tf/math/acos): Computes acos of x element-wise.

[`acosh(...)`](../../../tf/math/acosh): Computes inverse hyperbolic cosine of x element-wise.

[`add(...)`](../../../tf/math/add): Returns x + y element-wise.

[`add_n(...)`](../../../tf/math/add_n): Adds all input tensors element-wise.

[`angle(...)`](../../../tf/math/angle): Returns the element-wise argument of a complex (or real) tensor.

[`argmax(...)`](../../../tf/math/argmax): Returns the index with the largest value across axes of a tensor.

[`argmin(...)`](../../../tf/math/argmin): Returns the index with the smallest value across axes of a tensor.

[`asin(...)`](../../../tf/math/asin): Computes the trignometric inverse sine of x element-wise.

[`asinh(...)`](../../../tf/math/asinh): Computes inverse hyperbolic sine of x element-wise.

[`atan(...)`](../../../tf/math/atan): Computes the trignometric inverse tangent of x element-wise.

[`atan2(...)`](../../../tf/math/atan2): Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

[`atanh(...)`](../../../tf/math/atanh): Computes inverse hyperbolic tangent of x element-wise.

[`bessel_i0(...)`](../../../tf/math/bessel_i0): Computes the Bessel i0 function of `x` element-wise.

[`bessel_i0e(...)`](../../../tf/math/bessel_i0e): Computes the Bessel i0e function of `x` element-wise.

[`bessel_i1(...)`](../../../tf/math/bessel_i1): Computes the Bessel i1 function of `x` element-wise.

[`bessel_i1e(...)`](../../../tf/math/bessel_i1e): Computes the Bessel i1e function of `x` element-wise.

[`betainc(...)`](../../../tf/math/betainc): Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

[`bincount(...)`](../../../tf/math/bincount): Counts the number of occurrences of each value in an integer array.

[`ceil(...)`](../../../tf/math/ceil): Returns element-wise smallest integer not less than x.

[`confusion_matrix(...)`](../../../tf/math/confusion_matrix): Computes the confusion matrix from predictions and labels.

[`conj(...)`](../../../tf/math/conj): Returns the complex conjugate of a complex number.

[`cos(...)`](../../../tf/math/cos): Computes cos of x element-wise.

[`cosh(...)`](../../../tf/math/cosh): Computes hyperbolic cosine of x element-wise.

[`count_nonzero(...)`](../../../tf/math/count_nonzero): Computes number of nonzero elements across dimensions of a tensor.

[`cumprod(...)`](../../../tf/math/cumprod): Compute the cumulative product of the tensor `x` along `axis`.

[`cumsum(...)`](../../../tf/math/cumsum): Compute the cumulative sum of the tensor `x` along `axis`.

[`cumulative_logsumexp(...)`](../../../tf/math/cumulative_logsumexp): Compute the cumulative log-sum-exp of the tensor `x` along `axis`.

[`digamma(...)`](../../../tf/math/digamma): Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`divide(...)`](../../../tf/math/divide): Computes Python style division of `x` by `y`.

[`divide_no_nan(...)`](../../../tf/math/divide_no_nan): Computes an unsafe divide which returns 0 if the y is zero.

[`equal(...)`](../../../tf/math/equal): Returns the truth value of (x == y) element-wise.

[`erf(...)`](../../../tf/math/erf): Computes the Gauss error function of `x` element-wise.

[`erfc(...)`](../../../tf/math/erfc): Computes the complementary error function of `x` element-wise.

[`exp(...)`](../../../tf/math/exp): Computes exponential of x element-wise.  \\(y = e^x\\).

[`expm1(...)`](../../../tf/math/expm1): Computes `exp(x) - 1` element-wise.

[`floor(...)`](../../../tf/math/floor): Returns element-wise largest integer not greater than x.

[`floordiv(...)`](../../../tf/math/floordiv): Divides `x / y` elementwise, rounding toward the most negative integer.

[`floormod(...)`](../../../tf/math/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`greater(...)`](../../../tf/math/greater): Returns the truth value of (x > y) element-wise.

[`greater_equal(...)`](../../../tf/math/greater_equal): Returns the truth value of (x >= y) element-wise.

[`igamma(...)`](../../../tf/math/igamma): Compute the lower regularized incomplete Gamma function `P(a, x)`.

[`igammac(...)`](../../../tf/math/igammac): Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`imag(...)`](../../../tf/math/imag): Returns the imaginary part of a complex (or real) tensor.

[`in_top_k(...)`](../../../tf/math/in_top_k): Says whether the targets are in the top `K` predictions.

[`invert_permutation(...)`](../../../tf/math/invert_permutation): Computes the inverse permutation of a tensor.

[`is_finite(...)`](../../../tf/math/is_finite): Returns which elements of x are finite.

[`is_inf(...)`](../../../tf/math/is_inf): Returns which elements of x are Inf.

[`is_nan(...)`](../../../tf/math/is_nan): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](../../../tf/math/is_non_decreasing): Returns `True` if `x` is non-decreasing.

[`is_strictly_increasing(...)`](../../../tf/math/is_strictly_increasing): Returns `True` if `x` is strictly increasing.

[`l2_normalize(...)`](../../../tf/math/l2_normalize): Normalizes along dimension `axis` using an L2 norm.

[`lbeta(...)`](../../../tf/math/lbeta): Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

[`less(...)`](../../../tf/math/less): Returns the truth value of (x < y) element-wise.

[`less_equal(...)`](../../../tf/math/less_equal): Returns the truth value of (x <= y) element-wise.

[`lgamma(...)`](../../../tf/math/lgamma): Computes the log of the absolute value of `Gamma(x)` element-wise.

[`log(...)`](../../../tf/math/log): Computes natural logarithm of x element-wise.

[`log1p(...)`](../../../tf/math/log1p): Computes natural logarithm of (1 + x) element-wise.

[`log_sigmoid(...)`](../../../tf/math/log_sigmoid): Computes log sigmoid of `x` element-wise.

[`log_softmax(...)`](../../../tf/nn/log_softmax): Computes log softmax activations.

[`logical_and(...)`](../../../tf/math/logical_and): Returns the truth value of x AND y element-wise.

[`logical_not(...)`](../../../tf/math/logical_not): Returns the truth value of NOT x element-wise.

[`logical_or(...)`](../../../tf/math/logical_or): Returns the truth value of x OR y element-wise.

[`logical_xor(...)`](../../../tf/math/logical_xor): Logical XOR function.

[`maximum(...)`](../../../tf/math/maximum): Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`minimum(...)`](../../../tf/math/minimum): Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`mod(...)`](../../../tf/math/floormod): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`multiply(...)`](../../../tf/math/multiply): Returns x * y element-wise.

[`multiply_no_nan(...)`](../../../tf/math/multiply_no_nan): Computes the product of x and y and returns 0 if the y is zero, even if x is NaN or infinite.

[`negative(...)`](../../../tf/math/negative): Computes numerical negative value element-wise.

[`nextafter(...)`](../../../tf/math/nextafter): Returns the next representable value of `x1` in the direction of `x2`, element-wise.

[`not_equal(...)`](../../../tf/math/not_equal): Returns the truth value of (x != y) element-wise.

[`polygamma(...)`](../../../tf/math/polygamma): Compute the polygamma function \\(\psi^{(n)}(x)\\).

[`polyval(...)`](../../../tf/math/polyval): Computes the elementwise value of a polynomial.

[`pow(...)`](../../../tf/math/pow): Computes the power of one value to another.

[`real(...)`](../../../tf/math/real): Returns the real part of a complex (or real) tensor.

[`reciprocal(...)`](../../../tf/math/reciprocal): Computes the reciprocal of x element-wise.

[`reciprocal_no_nan(...)`](../../../tf/math/reciprocal_no_nan): Performs a safe reciprocal operation, element wise.

[`reduce_all(...)`](../../../tf/reduce_all): Computes the "logical and" of elements across dimensions of a tensor.

[`reduce_any(...)`](../../../tf/math/reduce_any): Computes the "logical or" of elements across dimensions of a tensor.

[`reduce_euclidean_norm(...)`](../../../tf/math/reduce_euclidean_norm): Computes the Euclidean norm of elements across dimensions of a tensor.

[`reduce_logsumexp(...)`](../../../tf/math/reduce_logsumexp): Computes log(sum(exp(elements across dimensions of a tensor))).

[`reduce_max(...)`](../../../tf/math/reduce_max): Computes the maximum of elements across dimensions of a tensor.

[`reduce_mean(...)`](../../../tf/math/reduce_mean): Computes the mean of elements across dimensions of a tensor.

[`reduce_min(...)`](../../../tf/math/reduce_min): Computes the minimum of elements across dimensions of a tensor.

[`reduce_prod(...)`](../../../tf/math/reduce_prod): Computes the product of elements across dimensions of a tensor.

[`reduce_std(...)`](../../../tf/math/reduce_std): Computes the standard deviation of elements across dimensions of a tensor.

[`reduce_sum(...)`](../../../tf/math/reduce_sum): Computes the sum of elements across dimensions of a tensor.

[`reduce_variance(...)`](../../../tf/math/reduce_variance): Computes the variance of elements across dimensions of a tensor.

[`rint(...)`](../../../tf/math/rint): Returns element-wise integer closest to x.

[`round(...)`](../../../tf/math/round): Rounds the values of a tensor to the nearest integer, element-wise.

[`rsqrt(...)`](../../../tf/math/rsqrt): Computes reciprocal of square root of x element-wise.

[`scalar_mul(...)`](../../../tf/math/scalar_mul): Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

[`segment_max(...)`](../../../tf/math/segment_max): Computes the maximum along segments of a tensor.

[`segment_mean(...)`](../../../tf/math/segment_mean): Computes the mean along segments of a tensor.

[`segment_min(...)`](../../../tf/math/segment_min): Computes the minimum along segments of a tensor.

[`segment_prod(...)`](../../../tf/math/segment_prod): Computes the product along segments of a tensor.

[`segment_sum(...)`](../../../tf/math/segment_sum): Computes the sum along segments of a tensor.

[`sigmoid(...)`](../../../tf/math/sigmoid): Computes sigmoid of `x` element-wise.

[`sign(...)`](../../../tf/math/sign): Returns an element-wise indication of the sign of a number.

[`sin(...)`](../../../tf/math/sin): Computes sine of x element-wise.

[`sinh(...)`](../../../tf/math/sinh): Computes hyperbolic sine of x element-wise.

[`softmax(...)`](../../../tf/nn/softmax): Computes softmax activations.

[`softplus(...)`](../../../tf/math/softplus): Computes softplus: `log(exp(features) + 1)`.

[`softsign(...)`](../../../tf/nn/softsign): Computes softsign: `features / (abs(features) + 1)`.

[`sqrt(...)`](../../../tf/math/sqrt): Computes square root of x element-wise.

[`square(...)`](../../../tf/math/square): Computes square of x element-wise.

[`squared_difference(...)`](../../../tf/math/squared_difference): Returns (x - y)(x - y) element-wise.

[`subtract(...)`](../../../tf/math/subtract): Returns x - y element-wise.

[`tan(...)`](../../../tf/math/tan): Computes tan of x element-wise.

[`tanh(...)`](../../../tf/math/tanh): Computes hyperbolic tangent of `x` element-wise.

[`top_k(...)`](../../../tf/math/top_k): Finds values and indices of the `k` largest entries for the last dimension.

[`truediv(...)`](../../../tf/math/truediv): Divides x / y elementwise (using Python 3 division operator semantics).

[`unsorted_segment_max(...)`](../../../tf/math/unsorted_segment_max): Computes the maximum along segments of a tensor.

[`unsorted_segment_mean(...)`](../../../tf/math/unsorted_segment_mean): Computes the mean along segments of a tensor.

[`unsorted_segment_min(...)`](../../../tf/math/unsorted_segment_min): Computes the minimum along segments of a tensor.

[`unsorted_segment_prod(...)`](../../../tf/math/unsorted_segment_prod): Computes the product along segments of a tensor.

[`unsorted_segment_sqrt_n(...)`](../../../tf/math/unsorted_segment_sqrt_n): Computes the sum along segments of a tensor divided by the sqrt(N).

[`unsorted_segment_sum(...)`](../../../tf/math/unsorted_segment_sum): Computes the sum along segments of a tensor.

[`xdivy(...)`](../../../tf/math/xdivy): Returns 0 if x == 0, and x / y otherwise, elementwise.

[`xlogy(...)`](../../../tf/math/xlogy): Returns 0 if x == 0, and x * log(y) otherwise, elementwise.

[`zero_fraction(...)`](../../../tf/math/zero_fraction): Returns the fraction of zeros in `value`.

[`zeta(...)`](../../../tf/math/zeta): Compute the Hurwitz zeta function \\(\zeta(x, q)\\).
