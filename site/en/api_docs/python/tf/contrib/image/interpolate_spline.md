page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.interpolate_spline

``` python
tf.contrib.image.interpolate_spline(
    train_points,
    train_values,
    query_points,
    order,
    regularization_weight=0.0,
    name='interpolate_spline'
)
```



Defined in [`tensorflow/contrib/image/python/ops/interpolate_spline.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/image/python/ops/interpolate_spline.py).

Interpolate signal using polyharmonic interpolation.

The interpolant has the form
<div> $$f(x) = \sum_{i = 1}^n w_i \phi(||x - c_i||) + v^T x + b.$$ </div>

This is a sum of two terms: (1) a weighted sum of radial basis function (RBF)
terms, with the centers \\(c_1, ... c_n\\), and (2) a linear term with a bias.
The \\(c_i\\) vectors are 'training' points. In the code, b is absorbed into v
by appending 1 as a final dimension to x. The coefficients w and v are
estimated such that the interpolant exactly fits the value of the function at
the \\(c_i\\) points, the vector w is orthogonal to each \\(c_i\\), and the
vector w sums to 0. With these constraints, the coefficients can be obtained
by solving a linear system.

\\(\phi\\) is an RBF, parametrized by an interpolation
order. Using order=2 produces the well-known thin-plate spline.

We also provide the option to perform regularized interpolation. Here, the
interpolant is selected to trade off between the squared loss on the training
data and a certain measure of its curvature
([details](https://en.wikipedia.org/wiki/Polyharmonic_spline)).
Using a regularization weight greater than zero has the effect that the
interpolant will no longer exactly fit the training data. However, it may be
less vulnerable to overfitting, particularly for high-order interpolation.

Note the interpolation procedure is differentiable with respect to all inputs
besides the order parameter.

#### Args:

* <b>`train_points`</b>: `[batch_size, n, d]` float `Tensor` of n d-dimensional
    locations. These do not need to be regularly-spaced.
* <b>`train_values`</b>: `[batch_size, n, k]` float `Tensor` of n c-dimensional values
    evaluated at train_points.
* <b>`query_points`</b>: `[batch_size, m, d]` `Tensor` of m d-dimensional locations
    where we will output the interpolant's values.
* <b>`order`</b>: order of the interpolation. Common values are 1 for
    \\(\phi(r) = r\\), 2 for \\(\phi(r) = r^2 * log(r)\\) (thin-plate spline),
     or 3 for \\(\phi(r) = r^3\\).
* <b>`regularization_weight`</b>: weight placed on the regularization term.
    This will depend substantially on the problem, and it should always be
    tuned. For many problems, it is reasonable to use no regularization.
    If using a non-zero value, we recommend a small value like 0.001.
* <b>`name`</b>: name prefix for ops created by this function


#### Returns:

`[b, m, k]` float `Tensor` of query values. We use train_points and
train_values to perform polyharmonic interpolation. The query values are
the values of the interpolant evaluated at the locations specified in
query_points.