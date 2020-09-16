description: Decorator to define a function with a custom gradient.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.custom_gradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.custom_gradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/custom_gradient.py#L87-L216">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Decorator to define a function with a custom gradient.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.custom_gradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.custom_gradient(
    f=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This decorator allows fine grained control over the gradients of a sequence
for operations.  This may be useful for multiple reasons, including providing
a more efficient or numerically stable gradient for a sequence of operations.

For example, consider the following function that commonly occurs in the
computation of cross entropy and log likelihoods:

```python
def log1pexp(x):
  return tf.math.log(1 + tf.exp(x))
```

Due to numerical instability, the gradient of this function evaluated at x=100
is NaN.  For example:

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
  return tf.math.log(1 + e), grad
```

With this definition, the gradient at x=100 will be correctly evaluated as
1.0.

Nesting custom gradients can lead to unintuitive results. The default
behavior does not correspond to n-th order derivatives. For example

```python
@tf.custom_gradient
def op(x):
  y = op1(x)
  @tf.custom_gradient
  def grad_fn(dy):
    gdy = op2(x, y, dy)
    def grad_grad_fn(ddy):  # Not the 2nd order gradient of op w.r.t. x.
      return op3(x, y, dy, ddy)
    return gdy, grad_grad_fn
  return y, grad_fn
```

The function `grad_grad_fn` will be calculating the first order gradient
of `grad_fn` with respect to `dy`, which is used to generate forward-mode
gradient graphs from backward-mode gradient graphs, but is not the same as
the second order gradient of `op` with respect to `x`.

Instead, wrap nested `@tf.custom_gradients` in another function:

```python
@tf.custom_gradient
def op_with_fused_backprop(x):
  y, x_grad = fused_op(x)
  def first_order_gradient(dy):
    @tf.custom_gradient
    def first_order_custom(unused_x):
      def second_order_and_transpose(ddy):
        return second_order_for_x(...), gradient_wrt_dy(...)
      return x_grad, second_order_and_transpose
    return dy * first_order_custom(x)
  return y, first_order_gradient
```

Additional arguments to the inner `@tf.custom_gradient`-decorated function
control the expected return values of the innermost function.

See also <a href="../tf/RegisterGradient.md"><code>tf.RegisterGradient</code></a> which registers a gradient function for a
primitive TensorFlow operation. <a href="../tf/custom_gradient.md"><code>tf.custom_gradient</code></a> on the other hand allows
for fine grained control over the gradient computation of a sequence of
operations.

Note that if the decorated function uses `Variable`s, the enclosing variable
scope must be using `ResourceVariable`s.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`f`
</td>
<td>
function `f(*x)` that returns a tuple `(y, grad_fn)` where:
- `x` is a sequence of `Tensor` inputs to the function.
- `y` is a `Tensor` or sequence of `Tensor` outputs of applying
TensorFlow operations in `f` to `x`.
- `grad_fn` is a function with the signature `g(*grad_ys)` which returns
a list of `Tensor`s - the derivatives of `Tensor`s in `y` with respect
to the `Tensor`s in `x`.  `grad_ys` is a `Tensor` or sequence of
`Tensor`s the same size as `y` holding the initial value gradients for
each `Tensor` in `y`. In a pure mathematical sense, a vector-argument
vector-valued function `f`'s derivatives should be its Jacobian matrix
`J`. Here we are expressing the Jacobian `J` as a function `grad_fn`
which defines how `J` will transform a vector `grad_ys` when
left-multiplied with it (`grad_ys * J`). This functional representation
of a matrix is convenient to use for chain-rule calculation
(in e.g. the back-propagation algorithm).

If `f` uses `Variable`s (that are not part of the
inputs), i.e. through `get_variable`, then `grad_fn` should have
signature `g(*grad_ys, variables=None)`, where `variables` is a list of
the `Variable`s, and return a 2-tuple `(grad_xs, grad_vars)`, where
`grad_xs` is the same as above, and `grad_vars` is a `list<Tensor>`
with the derivatives of `Tensor`s in `y` with respect to the variables
(that is, grad_vars has one Tensor per variable in variables).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A function `h(x)` which returns the same value as `f(x)[0]` and whose
gradient (as calculated by <a href="../tf/gradients.md"><code>tf.gradients</code></a>) is determined by `f(x)[1]`.
</td>
</tr>

</table>

