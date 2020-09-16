description: Math Operations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.math

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Math Operations.


Note: Functions taking `Tensor` arguments can also take anything accepted by
<a href="../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>.

Note: Elementwise binary operations in TensorFlow follow [numpy-style
broadcasting](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

TensorFlow provides a variety of math functions including:

* Basic arithmetic operators and trigonometric functions.
* Special math functions (like: <a href="../tf/math/igamma.md"><code>tf.math.igamma</code></a> and <a href="../tf/math/zeta.md"><code>tf.math.zeta</code></a>)
* Complex number functions (like: <a href="../tf/math/imag.md"><code>tf.math.imag</code></a> and <a href="../tf/math/angle.md"><code>tf.math.angle</code></a>)
* Reductions and scans (like: <a href="../tf/math/reduce_mean.md"><code>tf.math.reduce_mean</code></a> and <a href="../tf/math/cumsum.md"><code>tf.math.cumsum</code></a>)
* Segment functions (like: <a href="../tf/math/segment_sum.md"><code>tf.math.segment_sum</code></a>)

See: <a href="../tf/linalg.md"><code>tf.linalg</code></a> for matrix and tensor functions.

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
These functions take an additional argument `num_segments` so that the output
tensor can be efficiently allocated.

``` python
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])
tf.math.unsorted_segment_sum(c, tf.constant([0, 1, 0]), num_segments=2)
# ==> [[ 6,  8, 10, 12],
#       [-1, -2, -3, -4]]
```

## Modules

[`special`](../tf/math/special.md) module: Public API for tf.math.special namespace.

## Functions

[`abs(...)`](../tf/math/abs.md): Computes the absolute value of a tensor.

[`accumulate_n(...)`](../tf/math/accumulate_n.md): Returns the element-wise sum of a list of tensors.

[`acos(...)`](../tf/math/acos.md): Computes acos of x element-wise.

[`acosh(...)`](../tf/math/acosh.md): Computes inverse hyperbolic cosine of x element-wise.

[`add(...)`](../tf/math/add.md): Returns x + y element-wise.

[`add_n(...)`](../tf/math/add_n.md): Adds all input tensors element-wise.

[`angle(...)`](../tf/math/angle.md): Returns the element-wise argument of a complex (or real) tensor.

[`argmax(...)`](../tf/math/argmax.md): Returns the index with the largest value across axes of a tensor.

[`argmin(...)`](../tf/math/argmin.md): Returns the index with the smallest value across axes of a tensor.

[`asin(...)`](../tf/math/asin.md): Computes the trignometric inverse sine of x element-wise.

[`asinh(...)`](../tf/math/asinh.md): Computes inverse hyperbolic sine of x element-wise.

[`atan(...)`](../tf/math/atan.md): Computes the trignometric inverse tangent of x element-wise.

[`atan2(...)`](../tf/math/atan2.md): Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

[`atanh(...)`](../tf/math/atanh.md): Computes inverse hyperbolic tangent of x element-wise.

[`bessel_i0(...)`](../tf/math/bessel_i0.md): Computes the Bessel i0 function of `x` element-wise.

[`bessel_i0e(...)`](../tf/math/bessel_i0e.md): Computes the Bessel i0e function of `x` element-wise.

[`bessel_i1(...)`](../tf/math/bessel_i1.md): Computes the Bessel i1 function of `x` element-wise.

[`bessel_i1e(...)`](../tf/math/bessel_i1e.md): Computes the Bessel i1e function of `x` element-wise.

[`betainc(...)`](../tf/math/betainc.md): Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

[`bincount(...)`](../tf/math/bincount.md): Counts the number of occurrences of each value in an integer array.

[`ceil(...)`](../tf/math/ceil.md): Return the ceiling of the input, element-wise.

[`confusion_matrix(...)`](../tf/math/confusion_matrix.md): Computes the confusion matrix from predictions and labels.

[`conj(...)`](../tf/math/conj.md): Returns the complex conjugate of a complex number.

[`cos(...)`](../tf/math/cos.md): Computes cos of x element-wise.

[`cosh(...)`](../tf/math/cosh.md): Computes hyperbolic cosine of x element-wise.

[`count_nonzero(...)`](../tf/math/count_nonzero.md): Computes number of nonzero elements across dimensions of a tensor.

[`cumprod(...)`](../tf/math/cumprod.md): Compute the cumulative product of the tensor `x` along `axis`.

[`cumsum(...)`](../tf/math/cumsum.md): Compute the cumulative sum of the tensor `x` along `axis`.

[`cumulative_logsumexp(...)`](../tf/math/cumulative_logsumexp.md): Compute the cumulative log-sum-exp of the tensor `x` along `axis`.

[`digamma(...)`](../tf/math/digamma.md): Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`divide(...)`](../tf/math/divide.md): Computes Python style division of `x` by `y`.

[`divide_no_nan(...)`](../tf/math/divide_no_nan.md): Computes a safe divide which returns 0 if the y is zero.

[`equal(...)`](../tf/math/equal.md): Returns the truth value of (x == y) element-wise.

[`erf(...)`](../tf/math/erf.md): Computes the Gauss error function of `x` element-wise.

[`erfc(...)`](../tf/math/erfc.md): Computes the complementary error function of `x` element-wise.

[`erfinv(...)`](../tf/math/erfinv.md): Compute inverse error function.

[`exp(...)`](../tf/math/exp.md): Computes exponential of x element-wise.  \\(y = e^x\\).

[`expm1(...)`](../tf/math/expm1.md): Computes `exp(x) - 1` element-wise.

[`floor(...)`](../tf/math/floor.md): Returns element-wise largest integer not greater than x.

[`floordiv(...)`](../tf/math/floordiv.md): Divides `x / y` elementwise, rounding toward the most negative integer.

[`floormod(...)`](../tf/math/floormod.md): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`greater(...)`](../tf/math/greater.md): Returns the truth value of (x > y) element-wise.

[`greater_equal(...)`](../tf/math/greater_equal.md): Returns the truth value of (x >= y) element-wise.

[`igamma(...)`](../tf/math/igamma.md): Compute the lower regularized incomplete Gamma function `P(a, x)`.

[`igammac(...)`](../tf/math/igammac.md): Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`imag(...)`](../tf/math/imag.md): Returns the imaginary part of a complex (or real) tensor.

[`in_top_k(...)`](../tf/math/in_top_k.md): Says whether the targets are in the top `K` predictions.

[`invert_permutation(...)`](../tf/math/invert_permutation.md): Computes the inverse permutation of a tensor.

[`is_finite(...)`](../tf/math/is_finite.md): Returns which elements of x are finite.

[`is_inf(...)`](../tf/math/is_inf.md): Returns which elements of x are Inf.

[`is_nan(...)`](../tf/math/is_nan.md): Returns which elements of x are NaN.

[`is_non_decreasing(...)`](../tf/math/is_non_decreasing.md): Returns `True` if `x` is non-decreasing.

[`is_strictly_increasing(...)`](../tf/math/is_strictly_increasing.md): Returns `True` if `x` is strictly increasing.

[`l2_normalize(...)`](../tf/math/l2_normalize.md): Normalizes along dimension `axis` using an L2 norm.

[`lbeta(...)`](../tf/math/lbeta.md): Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

[`less(...)`](../tf/math/less.md): Returns the truth value of (x < y) element-wise.

[`less_equal(...)`](../tf/math/less_equal.md): Returns the truth value of (x <= y) element-wise.

[`lgamma(...)`](../tf/math/lgamma.md): Computes the log of the absolute value of `Gamma(x)` element-wise.

[`log(...)`](../tf/math/log.md): Computes natural logarithm of x element-wise.

[`log1p(...)`](../tf/math/log1p.md): Computes natural logarithm of (1 + x) element-wise.

[`log_sigmoid(...)`](../tf/math/log_sigmoid.md): Computes log sigmoid of `x` element-wise.

[`log_softmax(...)`](../tf/nn/log_softmax.md): Computes log softmax activations.

[`logical_and(...)`](../tf/math/logical_and.md): Logical AND function.

[`logical_not(...)`](../tf/math/logical_not.md): Returns the truth value of `NOT x` element-wise.

[`logical_or(...)`](../tf/math/logical_or.md): Returns the truth value of x OR y element-wise.

[`logical_xor(...)`](../tf/math/logical_xor.md): Logical XOR function.

[`maximum(...)`](../tf/math/maximum.md): Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`minimum(...)`](../tf/math/minimum.md): Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`mod(...)`](../tf/math/floormod.md): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`multiply(...)`](../tf/math/multiply.md): Returns an element-wise x * y.

[`multiply_no_nan(...)`](../tf/math/multiply_no_nan.md): Computes the product of x and y and returns 0 if the y is zero, even if x is NaN or infinite.

[`ndtri(...)`](../tf/math/ndtri.md): Compute quantile of Standard Normal.

[`negative(...)`](../tf/math/negative.md): Computes numerical negative value element-wise.

[`nextafter(...)`](../tf/math/nextafter.md): Returns the next representable value of `x1` in the direction of `x2`, element-wise.

[`not_equal(...)`](../tf/math/not_equal.md): Returns the truth value of (x != y) element-wise.

[`polygamma(...)`](../tf/math/polygamma.md): Compute the polygamma function \\(\psi^{(n)}(x)\\).

[`polyval(...)`](../tf/math/polyval.md): Computes the elementwise value of a polynomial.

[`pow(...)`](../tf/math/pow.md): Computes the power of one value to another.

[`real(...)`](../tf/math/real.md): Returns the real part of a complex (or real) tensor.

[`reciprocal(...)`](../tf/math/reciprocal.md): Computes the reciprocal of x element-wise.

[`reciprocal_no_nan(...)`](../tf/math/reciprocal_no_nan.md): Performs a safe reciprocal operation, element wise.

[`reduce_all(...)`](../tf/reduce_all.md): Computes the "logical and" of elements across dimensions of a tensor.

[`reduce_any(...)`](../tf/math/reduce_any.md): Computes the "logical or" of elements across dimensions of a tensor.

[`reduce_euclidean_norm(...)`](../tf/math/reduce_euclidean_norm.md): Computes the Euclidean norm of elements across dimensions of a tensor.

[`reduce_logsumexp(...)`](../tf/math/reduce_logsumexp.md): Computes log(sum(exp(elements across dimensions of a tensor))).

[`reduce_max(...)`](../tf/math/reduce_max.md): Computes the maximum of elements across dimensions of a tensor.

[`reduce_mean(...)`](../tf/math/reduce_mean.md): Computes the mean of elements across dimensions of a tensor.

[`reduce_min(...)`](../tf/math/reduce_min.md): Computes the minimum of elements across dimensions of a tensor.

[`reduce_prod(...)`](../tf/math/reduce_prod.md): Computes the product of elements across dimensions of a tensor.

[`reduce_std(...)`](../tf/math/reduce_std.md): Computes the standard deviation of elements across dimensions of a tensor.

[`reduce_sum(...)`](../tf/math/reduce_sum.md): Computes the sum of elements across dimensions of a tensor.

[`reduce_variance(...)`](../tf/math/reduce_variance.md): Computes the variance of elements across dimensions of a tensor.

[`rint(...)`](../tf/math/rint.md): Returns element-wise integer closest to x.

[`round(...)`](../tf/math/round.md): Rounds the values of a tensor to the nearest integer, element-wise.

[`rsqrt(...)`](../tf/math/rsqrt.md): Computes reciprocal of square root of x element-wise.

[`scalar_mul(...)`](../tf/math/scalar_mul.md): Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

[`segment_max(...)`](../tf/math/segment_max.md): Computes the maximum along segments of a tensor.

[`segment_mean(...)`](../tf/math/segment_mean.md): Computes the mean along segments of a tensor.

[`segment_min(...)`](../tf/math/segment_min.md): Computes the minimum along segments of a tensor.

[`segment_prod(...)`](../tf/math/segment_prod.md): Computes the product along segments of a tensor.

[`segment_sum(...)`](../tf/math/segment_sum.md): Computes the sum along segments of a tensor.

[`sigmoid(...)`](../tf/math/sigmoid.md): Computes sigmoid of `x` element-wise.

[`sign(...)`](../tf/math/sign.md): Returns an element-wise indication of the sign of a number.

[`sin(...)`](../tf/math/sin.md): Computes sine of x element-wise.

[`sinh(...)`](../tf/math/sinh.md): Computes hyperbolic sine of x element-wise.

[`sobol_sample(...)`](../tf/math/sobol_sample.md): Generates points from the Sobol sequence.

[`softmax(...)`](../tf/nn/softmax.md): Computes softmax activations.

[`softplus(...)`](../tf/math/softplus.md): Computes softplus: `log(exp(features) + 1)`.

[`softsign(...)`](../tf/nn/softsign.md): Computes softsign: `features / (abs(features) + 1)`.

[`sqrt(...)`](../tf/math/sqrt.md): Computes element-wise square root of the input tensor.

[`square(...)`](../tf/math/square.md): Computes square of x element-wise.

[`squared_difference(...)`](../tf/math/squared_difference.md): Returns (x - y)(x - y) element-wise.

[`subtract(...)`](../tf/math/subtract.md): Returns x - y element-wise.

[`tan(...)`](../tf/math/tan.md): Computes tan of x element-wise.

[`tanh(...)`](../tf/math/tanh.md): Computes hyperbolic tangent of `x` element-wise.

[`top_k(...)`](../tf/math/top_k.md): Finds values and indices of the `k` largest entries for the last dimension.

[`truediv(...)`](../tf/math/truediv.md): Divides x / y elementwise (using Python 3 division operator semantics).

[`unsorted_segment_max(...)`](../tf/math/unsorted_segment_max.md): Computes the maximum along segments of a tensor.

[`unsorted_segment_mean(...)`](../tf/math/unsorted_segment_mean.md): Computes the mean along segments of a tensor.

[`unsorted_segment_min(...)`](../tf/math/unsorted_segment_min.md): Computes the minimum along segments of a tensor.

[`unsorted_segment_prod(...)`](../tf/math/unsorted_segment_prod.md): Computes the product along segments of a tensor.

[`unsorted_segment_sqrt_n(...)`](../tf/math/unsorted_segment_sqrt_n.md): Computes the sum along segments of a tensor divided by the sqrt(N).

[`unsorted_segment_sum(...)`](../tf/math/unsorted_segment_sum.md): Computes the sum along segments of a tensor.

[`xdivy(...)`](../tf/math/xdivy.md): Returns 0 if x == 0, and x / y otherwise, elementwise.

[`xlog1py(...)`](../tf/math/xlog1py.md): Compute x * log1p(y).

[`xlogy(...)`](../tf/math/xlogy.md): Returns 0 if x == 0, and x * log(y) otherwise, elementwise.

[`zero_fraction(...)`](../tf/math/zero_fraction.md): Returns the fraction of zeros in `value`.

[`zeta(...)`](../tf/math/zeta.md): Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

