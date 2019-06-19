page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.gradients_function

``` python
tf.contrib.eager.gradients_function(
    f,
    params=None
)
```



Defined in [`tensorflow/python/eager/backprop.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/eager/backprop.py).

Returns a function which differentiates f with respect to params.

Example:

```python
# f(x, y) = (x ^ 3) * y - x * (y ^ 2)
# Therefore, the 1st order derivatives are:
#   df / dx = 3 * (x ^ 2) * y - y ^ 2
#   df / dy = x ^ 3 - 2 * x * y
# The 2nd order derivatives with respect to x is:
#   d^2 f / (dx)^2 = 6 * x * y
def f(x, y):
  return x * x * x * y - x * y * y

# Obtain a function that returns 1st order gradients.
grad_fn = tfe.gradients_function(f)

x = 2.0
y = 3.0

# Invoke the 1st order gradient function.
x_grad, y_grad = grad_fn(x, y)
assert x_grad.numpy() == 3 * (2 ** 2) * 3 - 3 ** 2
assert y_grad.numpy() == (2 ** 3) - 2 * 2 * 3

# Obtain a function that returns the 2nd order gradient with respect to x.
gradgrad_fn = tfe.gradients_function(lambda x, y: grad_fn(x, y)[0])

# Invoke the 2nd order gradient function.
x_gradgrad = gradgrad_fn(x, y)[0]
assert x_gradgrad.numpy() == 6 * 2 * 3

# To obtain a callable that returns the gradient(s) of `f` with respect to a
# subset of its inputs, use the `params` keyword argument with
# `gradients_function()`.
ygrad_fn = tfe.gradients_function(f, params=[1])

(y_grad,) = ygrad_fn(x, y)
assert y_grad.numpy() == (2 ** 3) - 2 * 2 * 3
```

Note that only tensors with real or complex dtypes are differentiable.

#### Args:

f: function to be differentiated. If `f` returns a scalar, this scalar will
  be differentiated. If `f` returns a tensor or list of tensors, by default
  a scalar will be computed by adding all their values to produce a single
  scalar. If desired, the tensors can be elementwise multiplied by the
  tensors passed as the `dy` keyword argument to the returned gradient
  function.
params: list of parameter names of f or list of integers indexing the
  parameters with respect to which we'll differentiate. Passing None
  differentiates with respect to all parameters.


#### Returns:

function which, when called, returns the value of f and the gradient
of f with respect to all of `params`. The function takes an extra optional
keyword argument "dy". Setting it allows computation of vector jacobian
products for vectors other than the vector of ones.


#### Raises:

ValueError: if the params are not all strings or all integers.