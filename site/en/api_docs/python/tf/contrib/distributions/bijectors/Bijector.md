

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.bijectors.Bijector

### `class tf.contrib.distributions.bijectors.Bijector`



Defined in [`tensorflow/python/ops/distributions/bijector_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/distributions/bijector_impl.py).

See the guide: [Random variable transformations (contrib) > Bijectors](../../../../../../api_guides/python/contrib.distributions.bijectors#Bijectors)

Interface for invertible transformations of a `Distribution` sample.

#### Mathematical Details

A `Bijector` implements a
[diffeomorphism](https://en.wikipedia.org/wiki/Diffeomorphism), i.e., a
bijective, differentiable function. A `Bijector` is used by
`TransformedDistribution` but can be generally used for transforming a
`Distribution` generated `Tensor`. A `Bijector` is characterized by three
operations:

1. Forward Evaluation

   Useful for turning one random outcome into another random outcome from a
   different distribution.

2. Inverse Evaluation

   Useful for "reversing" a transformation to compute one probability in
   terms of another.

3. (log o det o Jacobian o inverse)(x)

   "The log of the determinant of the matrix of all first-order partial
   derivatives of the inverse function."
   Useful for inverting a transformation to compute one probability in terms
   of another. Geometrically, the det(Jacobian) is the volume of the
   transformation and is used to scale the probability.

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
x != my_bijector.forward(fwd_x)  # Not equal because g(x) != g(g(x)).
```

- Computing a log-likelihood:

```python
def transformed_log_prob(bijector, log_prob, x):
  return (bijector.inverse_log_det_jacobian(x) +
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
>         def __init__(self, event_ndims=0, validate_args=False, name="exp"):
>           super(Exp, self).__init__(
>               event_ndims=event_ndims, validate_args=validate_args, name=name)
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
>           if self.event_ndims is None:
>             raise ValueError("Jacobian requires known event_ndims.")
>           event_dims = array_ops.shape(x)[-self.event_ndims:]
>           return math_ops.reduce_sum(x, axis=event_dims)
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

#### Jacobian

The Jacobian is a reduction over event dims. To see this, consider the `Exp`
`Bijector` applied to a `Tensor` which has sample, batch, and event (S, B, E)
shape semantics. Suppose the `Tensor`'s partitioned-shape is `(S=[4], B=[2],
E=[3, 3])`. The shape of the `Tensor` returned by `forward` and `inverse` is
unchanged, i.e., `[4, 2, 3, 3]`.  However the shape returned by
`inverse_log_det_jacobian` is `[4, 2]` because the Jacobian is a reduction
over the event dimensions.

It is sometimes useful to implement the inverse Jacobian as the negative
forward Jacobian. For example,

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
    The same theorem also implies `g{-1}'` is non-singular therefore:
    `inv[ g'(g^{-1}(y)) ] = g^{-1}'(y)`.
    The claim follows from [properties of determinant](
https://en.wikipedia.org/wiki/Determinant#Multiplicativity_and_matrix_groups).

Generally its preferable to directly implement the inverse Jacobian. This
should have superior numerical stability and will often share subgraphs with
the `_inverse` implementation.

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

## Properties

<h3 id="dtype"><code>dtype</code></h3>

dtype of `Tensor`s transformable by this distribution.

<h3 id="event_ndims"><code>event_ndims</code></h3>

Returns then number of event dimensions this bijector operates on.

<h3 id="graph_parents"><code>graph_parents</code></h3>

Returns this `Bijector`'s graph_parents as a Python list.

<h3 id="is_constant_jacobian"><code>is_constant_jacobian</code></h3>

Returns true iff the Jacobian is not a function of x.

Note: Jacobian is either constant for both forward and inverse or neither.

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
    event_ndims=None,
    graph_parents=None,
    is_constant_jacobian=False,
    validate_args=False,
    dtype=None,
    name=None
)
```

Constructs Bijector.

A `Bijector` transforms random variables into new random variables.

Examples:

```python
# Create the Y = g(X) = X transform which operates on vector events.
identity = Identity(event_ndims=1)

# Create the Y = g(X) = exp(X) transform which operates on matrices.
exp = Exp(event_ndims=2)
```

See `Bijector` subclass docstring for more details and specific examples.

#### Args:

* <b>`event_ndims`</b>: number of dimensions associated with event coordinates.
* <b>`graph_parents`</b>: Python list of graph prerequisites of this `Bijector`.
* <b>`is_constant_jacobian`</b>: Python `bool` indicating that the Jacobian is not a
    function of the input.
* <b>`validate_args`</b>: Python `bool`, default `False`. Whether to validate input
    with asserts. If `validate_args` is `False`, and the inputs are invalid,
    correct behavior is not guaranteed.
* <b>`dtype`</b>: `tf.dtype` supported by this `Bijector`. `None` means dtype is not
    enforced.
* <b>`name`</b>: The name to give Ops created by the initializer.

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
    name='forward_log_det_jacobian'
)
```

Returns both the forward_log_det_jacobian.

#### Args:

* <b>`x`</b>: `Tensor`. The input to the "forward" Jacobian evaluation.
* <b>`name`</b>: The name to give this op.


#### Returns:

  `Tensor`.


#### Raises:

* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
    `self.dtype`.
* <b>`NotImplementedError`</b>: if neither `_forward_log_det_jacobian`
    nor {`_inverse`, `_inverse_log_det_jacobian`} are implemented.

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

  `Tensor`.


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
    name='inverse_log_det_jacobian'
)
```

Returns the (log o det o Jacobian o inverse)(y).

Mathematically, returns: `log(det(dX/dY))(Y)`. (Recall that: `X=g^{-1}(Y)`.)

Note that `forward_log_det_jacobian` is the negative of this function.

#### Args:

* <b>`y`</b>: `Tensor`. The input to the "inverse" Jacobian evaluation.
* <b>`name`</b>: The name to give this op.


#### Returns:

  `Tensor`.


#### Raises:

* <b>`TypeError`</b>: if `self.dtype` is specified and `y.dtype` is not
    `self.dtype`.
* <b>`NotImplementedError`</b>: if `_inverse_log_det_jacobian` is not implemented.



