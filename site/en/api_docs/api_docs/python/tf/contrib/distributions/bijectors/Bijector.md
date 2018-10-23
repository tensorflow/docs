

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.bijectors.Bijector

## Class `Bijector`





Defined in [`tensorflow/python/ops/distributions/bijector_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/distributions/bijector_impl.py).

Interface for transformations of a `Distribution` sample.

Bijectors can be used to represent any differentiable and injective
(one to one) function defined on an open subset of `R^n`.  Some non-injective
transformations are also supported (see "Non Injective Transforms" below).

#### Mathematical Details

A `Bijector` implements a [smooth covering map](
https://en.wikipedia.org/wiki/Local_diffeomorphism), i.e., a local
diffeomorphism such that every point in the target has a neighborhood evenly
covered by a map ([see also](
https://en.wikipedia.org/wiki/Covering_space#Covering_of_a_manifold)).
A `Bijector` is used by `TransformedDistribution` but can be generally used
for transforming a `Distribution` generated `Tensor`. A `Bijector` is
characterized by three operations:

1. Forward

   Useful for turning one random outcome into another random outcome from a
   different distribution.

2. Inverse

   Useful for "reversing" a transformation to compute one probability in
   terms of another.

3. `log_det_jacobian(x)`

   "The log of the absolute value of the determinant of the matrix of all
   first-order partial derivatives of the inverse function."

   Useful for inverting a transformation to compute one probability in terms
   of another. Geometrically, the Jacobian determinant is the volume of the
   transformation and is used to scale the probability.

   We take the absolute value of the determinant before log to avoid NaN
   values.  Geometrically, a negative determinant corresponds to an
   orientation-reversing transformation.  It is ok for us to discard the sign
   of the determinant because we only integrate everywhere-nonnegative
   functions (probability densities) and the correct orientation is always the
   one that produces a nonnegative integrand.

By convention, transformations of random variables are named in terms of the
forward transformation. The forward transformation creates samples, the
inverse is useful for computing probabilities.

#### Example Uses

- Basic properties:

```python
x = ...  # A tensor.
# Evaluate forward transformation.
fwd_x = my_bijector.forward(x)
x == my_bijector.inverse(fwd_x)
x != my_bijector.forward(fwd_x)  # Not equal because x != g(g(x)).
```

- Computing a log-likelihood:

```python
def transformed_log_prob(bijector, log_prob, x):
  return (bijector.inverse_log_det_jacobian(x, event_ndims=0) +
          log_prob(bijector.inverse(x)))
```

- Transforming a random outcome:

```python
def transformed_sample(bijector, x):
  return bijector.forward(x)
```

#### Example Bijectors

- "Exponential"

>     Y = g(X) = exp(X)
>     X ~ Normal(0, 1)  # Univariate.

  Implies:

>       g^{-1}(Y) = log(Y)
>       |Jacobian(g^{-1})(y)| = 1 / y
>       Y ~ LogNormal(0, 1), i.e.,
>       prob(Y=y) = |Jacobian(g^{-1})(y)| * prob(X=g^{-1}(y))
>                 = (1 / y) Normal(log(y); 0, 1)

  Here is an example of how one might implement the `Exp` bijector:

>       class Exp(Bijector):
>     
>         def __init__(self, validate_args=False, name="exp"):
>           super(Exp, self).__init__(
>               validate_args=validate_args,
>               forward_min_event_ndims=0,
>               name=name)
>     
>         def _forward(self, x):
>           return math_ops.exp(x)
>     
>         def _inverse(self, y):
>           return math_ops.log(y)
>     
>         def _inverse_log_det_jacobian(self, y):
>           return -self._forward_log_det_jacobian(self._inverse(y))
>     
>         def _forward_log_det_jacobian(self, x):
>           # Notice that we needn't do any reducing, even when`event_ndims > 0`.
>           # The base Bijector class will handle reducing for us; it knows how
>           # to do so because we called `super` `__init__` with
>           # `forward_min_event_ndims = 0`.
>           return x
>       ```
>     
>     "Affine"
>     
  Y = g(X) = sqrtSigma * X + mu
  X ~ MultivariateNormal(0, I_d)
>     
>     Implies:
>     
    g^{-1}(Y) = inv(sqrtSigma) * (Y - mu)
    |Jacobian(g^{-1})(y)| = det(inv(sqrtSigma))
    Y ~ MultivariateNormal(mu, sqrtSigma) , i.e.,
    prob(Y=y) = |Jacobian(g^{-1})(y)| * prob(X=g^{-1}(y))
              = det(sqrtSigma)^(-d) *
                MultivariateNormal(inv(sqrtSigma) * (y - mu); 0, I_d)
    ```

#### Min_event_ndims and Naming

Bijectors are named for the dimensionality of data they act on (i.e. without
broadcasting). We can think of bijectors having an intrinsic `min_event_ndims`
, which is the minimum number of dimensions for the bijector act on. For
instance, a Cholesky decomposition requires a matrix, and hence
`min_event_ndims=2`.

Some examples:

`AffineScalar:  min_event_ndims=0`
`Affine:  min_event_ndims=1`
`Cholesky:  min_event_ndims=2`
`Exp:  min_event_ndims=0`
`Sigmoid:  min_event_ndims=0`
`SoftmaxCentered:  min_event_ndims=1`

Note the difference between `Affine` and `AffineScalar`. `AffineScalar`
operates on scalar events, whereas `Affine` operates on vector-valued events.

More generally, there is a `forward_min_event_ndims` and an
`inverse_min_event_ndims`. In most cases, these will be the same.
However, for some shape changing bijectors, these will be different
(e.g. a bijector which pads an extra dimension at the end, might have
`forward_min_event_ndims=0` and `inverse_min_event_ndims=1`.


#### Jacobian Determinant

The Jacobian determinant is a reduction over `event_ndims - min_event_ndims`
(`forward_min_event_ndims` for `forward_log_det_jacobian` and
`inverse_min_event_ndims` for `inverse_log_det_jacobian`).
To see this, consider the `Exp` `Bijector` applied to a `Tensor` which has
sample, batch, and event (S, B, E) shape semantics. Suppose the `Tensor`'s
partitioned-shape is `(S=[4], B=[2], E=[3, 3])`. The shape of the `Tensor`
returned by `forward` and `inverse` is unchanged, i.e., `[4, 2, 3, 3]`.
However the shape returned by `inverse_log_det_jacobian` is `[4, 2]` because
the Jacobian determinant is a reduction over the event dimensions.

Another example is the `Affine` `Bijector`. Because `min_event_ndims = 1`, the
Jacobian determinant reduction is over `event_ndims - 1`.

It is sometimes useful to implement the inverse Jacobian determinant as the
negative forward Jacobian determinant. For example,

```python
def _inverse_log_det_jacobian(self, y):
   return -self._forward_log_det_jac(self._inverse(y))  # Note negation.
```

The correctness of this approach can be seen from the following claim.

- Claim:

    Assume `Y = g(X)` is a bijection whose derivative exists and is nonzero
    for its domain, i.e., `dY/dX = d/dX g(X) != 0`. Then:

    ```none
    (log o det o jacobian o g^{-1})(Y) = -(log o det o jacobian o g)(X)
    ```

- Proof:

    From the bijective, nonzero differentiability of `g`, the
    [inverse function theorem](
        https://en.wikipedia.org/wiki/Inverse_function_theorem)
    implies `g^{-1}` is differentiable in the image of `g`.
    Applying the chain rule to `y = g(x) = g(g^{-1}(y))` yields
    `I = g'(g^{-1}(y))*g^{-1}'(y)`.
    The same theorem also implies `g^{-1}'` is non-singular therefore:
    `inv[ g'(g^{-1}(y)) ] = g^{-1}'(y)`.
    The claim follows from [properties of determinant](
https://en.wikipedia.org/wiki/Determinant#Multiplicativity_and_matrix_groups).

Generally its preferable to directly implement the inverse Jacobian
determinant.  This should have superior numerical stability and will often
share subgraphs with the `_inverse` implementation.

#### Is_constant_jacobian

Certain bijectors will have constant jacobian matrices. For instance, the
`Affine` bijector encodes multiplication by a matrix plus a shift, with
jacobian matrix, the same aforementioned matrix.

`is_constant_jacobian` encodes the fact that the jacobian matrix is constant.
The semantics of this argument are the following:

  * Repeated calls to "log_det_jacobian" functions with the same
    `event_ndims` (but not necessarily same input), will return the first
    computed jacobian (because the matrix is constant, and hence is input
    independent).
  * `log_det_jacobian` implementations are merely broadcastable to the true
    `log_det_jacobian` (because, again, the jacobian matrix is input
    independent). Specifically, `log_det_jacobian` is implemented as the
    log jacobian determinant for a single input.

    ```python
    class Identity(Bijector):

      def __init__(self, validate_args=False, name="identity"):
        super(Identity, self).__init__(
            is_constant_jacobian=True,
            validate_args=validate_args,
            forward_min_event_ndims=0,
            name=name)

      def _forward(self, x):
        return x

      def _inverse(self, y):
        return y

      def _inverse_log_det_jacobian(self, y):
        return -self._forward_log_det_jacobian(self._inverse(y))

      def _forward_log_det_jacobian(self, x):
        # The full log jacobian determinant would be array_ops.zero_like(x).
        # However, we circumvent materializing that, since the jacobian
        # calculation is input independent, and we specify it for one input.
        return constant_op.constant(0., x.dtype.base_dtype)

    ```

#### Subclass Requirements

- Subclasses typically implement:

    - `_forward`,
    - `_inverse`,
    - `_inverse_log_det_jacobian`,
    - `_forward_log_det_jacobian` (optional).

  The `_forward_log_det_jacobian` is called when the bijector is inverted via
  the `Invert` bijector. If undefined, a slightly less efficiently
  calculation, `-1 * _inverse_log_det_jacobian`, is used.

  If the bijector changes the shape of the input, you must also implement:

    - _forward_event_shape_tensor,
    - _forward_event_shape (optional),
    - _inverse_event_shape_tensor,
    - _inverse_event_shape (optional).

  By default the event-shape is assumed unchanged from input.

- If the `Bijector`'s use is limited to `TransformedDistribution` (or friends
  like `QuantizedDistribution`) then depending on your use, you may not need
  to implement all of `_forward` and `_inverse` functions.

  Examples:

    1. Sampling (e.g., `sample`) only requires `_forward`.
    2. Probability functions (e.g., `prob`, `cdf`, `survival`) only require
       `_inverse` (and related).
    3. Only calling probability functions on the output of `sample` means
      `_inverse` can be implemented as a cache lookup.

  See "Example Uses" [above] which shows how these functions are used to
  transform a distribution. (Note: `_forward` could theoretically be
  implemented as a cache lookup but this would require controlling the
  underlying sample generation mechanism.)

#### Non Injective Transforms

**WARNING** Handing of non-injective transforms is subject to change.

Non injective maps `g` are supported, provided their domain `D` can be
partitioned into `k` disjoint subsets, `Union{D1, ..., Dk}`, such that,
ignoring sets of measure zero, the restriction of `g` to each subset is a
differentiable bijection onto `g(D)`.  In particular, this imples that for
`y in g(D)`, the set inverse, i.e. `g^{-1}(y) = {x in D : g(x) = y}`, always
contains exactly `k` distinct points.

The property, `_is_injective` is set to `False` to indicate that the bijector
is not injective, yet satisfies the above condition.

The usual bijector API is modified in the case `_is_injective is False` (see
method docstrings for specifics).  Here we show by example the `AbsoluteValue`
bijector.  In this case, the domain `D = (-inf, inf)`, can be partitioned
into `D1 = (-inf, 0)`, `D2 = {0}`, and `D3 = (0, inf)`.  Let `gi` be the
restriction of `g` to `Di`, then both `g1` and `g3` are bijections onto
`(0, inf)`, with `g1^{-1}(y) = -y`, and `g3^{-1}(y) = y`.  We will use
`g1` and `g3` to define bijector methods over `D1` and `D3`.  `D2 = {0}` is
an oddball in that `g2` is one to one, and the derivative is not well defined.
Fortunately, when considering transformations of probability densities
(e.g. in `TransformedDistribution`), sets of measure zero have no effect in
theory, and only a small effect in 32 or 64 bit precision.  For that reason,
we define `inverse(0)` and `inverse_log_det_jacobian(0)` both as `[0, 0]`,
which is convenient and results in a left-semicontinuous pdf.


```python
abs = tf.contrib.distributions.bijectors.AbsoluteValue()

abs.forward(-1.)
==> 1.

abs.forward(1.)
==> 1.

abs.inverse(1.)
==> (-1., 1.)

# The |dX/dY| is constant, == 1.  So Log|dX/dY| == 0.
abs.inverse_log_det_jacobian(1., event_ndims=0)
==> (0., 0.)

# Special case handling of 0.
abs.inverse(0.)
==> (0., 0.)

abs.inverse_log_det_jacobian(0., event_ndims=0)
==> (0., 0.)
```

## Properties

<h3 id="dtype"><code>dtype</code></h3>

dtype of `Tensor`s transformable by this distribution.

<h3 id="forward_min_event_ndims"><code>forward_min_event_ndims</code></h3>

Returns the minimal number of dimensions bijector.forward operates on.

<h3 id="graph_parents"><code>graph_parents</code></h3>

Returns this `Bijector`'s graph_parents as a Python list.

<h3 id="inverse_min_event_ndims"><code>inverse_min_event_ndims</code></h3>

Returns the minimal number of dimensions bijector.inverse operates on.

<h3 id="is_constant_jacobian"><code>is_constant_jacobian</code></h3>

Returns true iff the Jacobian matrix is not a function of x.

Note: Jacobian matrix is either constant for both forward and inverse or
neither.

#### Returns:

* <b>`is_constant_jacobian`</b>: Python `bool`.

<h3 id="name"><code>name</code></h3>

Returns the string name of this `Bijector`.

<h3 id="validate_args"><code>validate_args</code></h3>

Returns True if Tensor arguments will be validated.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    graph_parents=None,
    is_constant_jacobian=False,
    validate_args=False,
    dtype=None,
    forward_min_event_ndims=None,
    inverse_min_event_ndims=None,
    name=None
)
```

Constructs Bijector.

A `Bijector` transforms random variables into new random variables.

Examples:

```python
# Create the Y = g(X) = X transform.
identity = Identity()

# Create the Y = g(X) = exp(X) transform.
exp = Exp()
```

See `Bijector` subclass docstring for more details and specific examples.

#### Args:

* <b>`graph_parents`</b>: Python list of graph prerequisites of this `Bijector`.
* <b>`is_constant_jacobian`</b>: Python `bool` indicating that the Jacobian matrix is
    not a function of the input.
* <b>`validate_args`</b>: Python `bool`, default `False`. Whether to validate input
    with asserts. If `validate_args` is `False`, and the inputs are invalid,
    correct behavior is not guaranteed.
* <b>`dtype`</b>: `tf.dtype` supported by this `Bijector`. `None` means dtype is not
    enforced.
* <b>`forward_min_event_ndims`</b>: Python `integer` indicating the minimum number of
    dimensions `forward` operates on.
* <b>`inverse_min_event_ndims`</b>: Python `integer` indicating the minimum number of
    dimensions `inverse` operates on. Will be set to
    `forward_min_event_ndims` by default, if no value is provided.
* <b>`name`</b>: The name to give Ops created by the initializer.


#### Raises:

* <b>`ValueError`</b>:  If neither `forward_min_event_ndims` and
    `inverse_min_event_ndims` are specified, or if either of them is
    negative.
* <b>`ValueError`</b>:  If a member of `graph_parents` is not a `Tensor`.

<h3 id="forward"><code>forward</code></h3>

``` python
forward(
    x,
    name='forward'
)
```

Returns the forward `Bijector` evaluation, i.e., X = g(Y).

#### Args:

* <b>`x`</b>: `Tensor`. The input to the "forward" evaluation.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`.


#### Raises:

* <b>`TypeError`</b>: if `self.dtype` is specified and `x.dtype` is not
    `self.dtype`.
* <b>`NotImplementedError`</b>: if `_forward` is not implemented.

<h3 id="forward_event_shape"><code>forward_event_shape</code></h3>

``` python
forward_event_shape(input_shape)
```

Shape of a single sample from a single batch as a `TensorShape`.

Same meaning as `forward_event_shape_tensor`. May be only partially defined.

#### Args:

* <b>`input_shape`</b>: `TensorShape` indicating event-portion shape passed into
    `forward` function.


#### Returns:

* <b>`forward_event_shape_tensor`</b>: `TensorShape` indicating event-portion shape
    after applying `forward`. Possibly unknown.

<h3 id="forward_event_shape_tensor"><code>forward_event_shape_tensor</code></h3>

``` python
forward_event_shape_tensor(
    input_shape,
    name='forward_event_shape_tensor'
)
```

Shape of a single sample from a single batch as an `int32` 1D `Tensor`.

#### Args:

* <b>`input_shape`</b>: `Tensor`, `int32` vector indicating event-portion shape
    passed into `forward` function.
* <b>`name`</b>: name to give to the op


#### Returns:

* <b>`forward_event_shape_tensor`</b>: `Tensor`, `int32` vector indicating
    event-portion shape after applying `forward`.

<h3 id="forward_log_det_jacobian"><code>forward_log_det_jacobian</code></h3>

``` python
forward_log_det_jacobian(
    x,
    event_ndims,
    name='forward_log_det_jacobian'
)
```

Returns both the forward_log_det_jacobian.

#### Args:

* <b>`x`</b>: `Tensor`. The input to the "forward" Jacobian determinant evaluation.
* <b>`event_ndims`</b>: Number of dimensions in the probabilistic events being
    transformed. Must be greater than or equal to
    `self.forward_min_event_ndims`. The result is summed over the final
    dimensions to produce a scalar Jacobian determinant for each event,
    i.e. it has shape `x.shape.ndims - event_ndims` dimensions.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`, if this bijector is injective.
  If not injective this is not implemented.


#### Raises:

* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
    `self.dtype`.
* <b>`NotImplementedError`</b>: if neither `_forward_log_det_jacobian`
    nor {`_inverse`, `_inverse_log_det_jacobian`} are implemented, or
    this is a non-injective bijector.

<h3 id="inverse"><code>inverse</code></h3>

``` python
inverse(
    y,
    name='inverse'
)
```

Returns the inverse `Bijector` evaluation, i.e., X = g^{-1}(Y).

#### Args:

* <b>`y`</b>: `Tensor`. The input to the "inverse" evaluation.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`, if this bijector is injective.
  If not injective, returns the k-tuple containing the unique
  `k` points `(x1, ..., xk)` such that `g(xi) = y`.


#### Raises:

* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
    `self.dtype`.
* <b>`NotImplementedError`</b>: if `_inverse` is not implemented.

<h3 id="inverse_event_shape"><code>inverse_event_shape</code></h3>

``` python
inverse_event_shape(output_shape)
```

Shape of a single sample from a single batch as a `TensorShape`.

Same meaning as `inverse_event_shape_tensor`. May be only partially defined.

#### Args:

* <b>`output_shape`</b>: `TensorShape` indicating event-portion shape passed into
    `inverse` function.


#### Returns:

* <b>`inverse_event_shape_tensor`</b>: `TensorShape` indicating event-portion shape
    after applying `inverse`. Possibly unknown.

<h3 id="inverse_event_shape_tensor"><code>inverse_event_shape_tensor</code></h3>

``` python
inverse_event_shape_tensor(
    output_shape,
    name='inverse_event_shape_tensor'
)
```

Shape of a single sample from a single batch as an `int32` 1D `Tensor`.

#### Args:

* <b>`output_shape`</b>: `Tensor`, `int32` vector indicating event-portion shape
    passed into `inverse` function.
* <b>`name`</b>: name to give to the op


#### Returns:

* <b>`inverse_event_shape_tensor`</b>: `Tensor`, `int32` vector indicating
    event-portion shape after applying `inverse`.

<h3 id="inverse_log_det_jacobian"><code>inverse_log_det_jacobian</code></h3>

``` python
inverse_log_det_jacobian(
    y,
    event_ndims,
    name='inverse_log_det_jacobian'
)
```

Returns the (log o det o Jacobian o inverse)(y).

Mathematically, returns: `log(det(dX/dY))(Y)`. (Recall that: `X=g^{-1}(Y)`.)

Note that `forward_log_det_jacobian` is the negative of this function,
evaluated at `g^{-1}(y)`.

#### Args:

* <b>`y`</b>: `Tensor`. The input to the "inverse" Jacobian determinant evaluation.
* <b>`event_ndims`</b>: Number of dimensions in the probabilistic events being
    transformed. Must be greater than or equal to
    `self.inverse_min_event_ndims`. The result is summed over the final
    dimensions to produce a scalar Jacobian determinant for each event,
    i.e. it has shape `y.shape.ndims - event_ndims` dimensions.
* <b>`name`</b>: The name to give this op.


#### Returns:

`Tensor`, if this bijector is injective.
  If not injective, returns the tuple of local log det
  Jacobians, `log(det(Dg_i^{-1}(y)))`, where `g_i` is the restriction
  of `g` to the `ith` partition `Di`.


#### Raises:

* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
    `self.dtype`.
* <b>`NotImplementedError`</b>: if `_inverse_log_det_jacobian` is not implemented.



