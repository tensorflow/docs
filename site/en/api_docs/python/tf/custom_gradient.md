page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.custom_gradient

### Aliases:

* `tf.contrib.eager.custom_gradient`
* `tf.custom_gradient`

``` python
tf.custom_gradient(f)
```



Defined in [`tensorflow/python/ops/custom_gradient.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/custom_gradient.py).

Decorator to define a function with a custom gradient.

This decorator allows fine grained control over the gradients of a sequence
for operations.  This may be useful for multiple reasons, including providing
a more efficient or numerically stable gradient for a sequence of operations.

For example, consider the following function that commonly occurs in the
computation of cross entropy and log likelihoods:

```python
def log1pexp(x):
  return tf.log(1 + tf.exp(x))
```

Due to numerical instability, the gradient this function evaluated at x=100 is
NaN.  For example:

```python
x = tf.constant(100.)
y = log1pexp(x)
dy = tf.gradients(y, x) # Will be NaN when evaluated.
```

The gradient expression can be analytically simplified to provide numerical
stability:

```python
@tf.custom_gradient
def log1pexp(x):
  e = tf.exp(x)
  def grad(dy):
    return dy * (1 - 1 / (1 + e))
  return tf.log(1 + e), grad
```

With this definition, the gradient at x=100 will be correctly evaluated as
1.0.

See also <a href="../tf/RegisterGradient"><code>tf.RegisterGradient</code></a> which registers a gradient function for a
primitive TensorFlow operation. <a href="../tf/custom_gradient"><code>tf.custom_gradient</code></a> on the other hand allows
for fine grained control over the gradient computation of a sequence of
operations.

Note that if the decorated function uses `Variable`s, the enclosing variable
scope must be using `ResourceVariable`s.

#### Args:

* <b>`f`</b>: function `f(x)` that returns a tuple `(y, grad_fn)` where:
     - `x` is a `Tensor` or sequence of `Tensor` inputs to the function.
     - `y` is a `Tensor` or sequence of `Tensor` outputs of applying
       TensorFlow
       operations in `f` to `x`.
     - `grad_fn` is a function with the signature `g(*grad_ys)` which returns
       a list of `Tensor`s - the derivatives of `Tensor`s in `y` with respect
       to the `Tensor`s in `x`.  `grad_ys` is a `Tensor` or sequence of
       `Tensor`s the same size as `y` holding the initial value gradients for
       each `Tensor` in `y`. If `f` uses `Variable`s (that are not part of the
       inputs), i.e. through `get_variable`, then `grad_fn` should have
       signature `g(*grad_ys, variables=None)`, where `variables` is a list of
       the `Variable`s, and return a 2-tuple `(grad_xs, grad_vars)`, where
       `grad_xs` is the same as above, and `grad_vars` is a `list<Tensor>`
       with the derivatives of `Tensor`s in `y` with respect to the variables.


#### Returns:

A function `h(x)` which returns the same value as `f(x)[0]` and whose
gradient (as calculated by <a href="../tf/gradients"><code>tf.gradients</code></a>) is determined by `f(x)[1]`.