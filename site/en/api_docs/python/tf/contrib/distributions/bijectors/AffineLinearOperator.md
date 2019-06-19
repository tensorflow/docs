

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.bijectors.AffineLinearOperator

## Class `AffineLinearOperator`

Inherits From: [`Bijector`](../../../../tf/distributions/bijectors/Bijector)



Defined in [`tensorflow/contrib/distributions/python/ops/bijectors/affine_linear_operator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/distributions/python/ops/bijectors/affine_linear_operator.py).

See the guide: [Random variable transformations (contrib) > Bijectors](../../../../../../api_guides/python/contrib.distributions.bijectors#Bijectors)

Compute `Y = g(X; shift, scale) = scale @ X + shift`.

`shift` is a numeric `Tensor` and `scale` is a `LinearOperator`.

If `X` is a scalar then the forward transformation is: `scale * X + shift`
where `*` denotes the scalar product.

Note: we don't always simply transpose `X` (but write it this way for
brevity). Actually the input `X` undergoes the following transformation
before being premultiplied by `scale`:

1. If there are no sample dims, we call `X = tf.expand_dims(X, 0)`, i.e.,
   `new_sample_shape = [1]`. Otherwise do nothing.
2. The sample shape is flattened to have one dimension, i.e.,
   `new_sample_shape = [n]` where `n = tf.reduce_prod(old_sample_shape)`.
3. The sample dim is cyclically rotated left by 1, i.e.,
   `new_shape = [B1,...,Bb, k, n]` where `n` is as above, `k` is the
   event_shape, and `B1,...,Bb` are the batch shapes for each of `b` batch
   dimensions.

(For more details see `shape.make_batch_of_event_sample_matrices`.)

The result of the above transformation is that `X` can be regarded as a batch
of matrices where each column is a draw from the distribution. After
premultiplying by `scale`, we take the inverse of this procedure. The input
`Y` also undergoes the same transformation before/after premultiplying by
`inv(scale)`.

Example Use:

```python
linalg = tf.linalg

x = [1., 2, 3]

shift = [-1., 0., 1]
diag = [1., 2, 3]
scale = linalg.LinearOperatorDiag(diag)
affine = AffineLinearOperator(shift, scale)
# In this case, `forward` is equivalent to:
# y = scale @ x + shift
y = affine.forward(x)  # [0., 4, 10]

shift = [2., 3, 1]
tril = [[1., 0, 0],
        [2, 1, 0],
        [3, 2, 1]]
scale = linalg.LinearOperatorLowerTriangular(tril)
affine = AffineLinearOperator(shift, scale)
# In this case, `forward` is equivalent to:
# np.squeeze(np.matmul(tril, np.expand_dims(x, -1)), -1) + shift
y = affine.forward(x)  # [3., 7, 11]
```

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

<h3 id="scale"><code>scale</code></h3>

The `scale` `LinearOperator` in `Y = scale @ X + shift`.

<h3 id="shift"><code>shift</code></h3>

The `shift` `Tensor` in `Y = scale @ X + shift`.

<h3 id="validate_args"><code>validate_args</code></h3>

Returns True if Tensor arguments will be validated.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    shift=None,
    scale=None,
    event_ndims=1,
    validate_args=False,
    name='affine_linear_operator'
)
```

Instantiates the `AffineLinearOperator` bijector.

#### Args:

* <b>`shift`</b>: Floating-point `Tensor`.
* <b>`scale`</b>:  Subclass of `LinearOperator`. Represents the (batch) positive
    definite matrix `M` in `R^{k x k}`.
* <b>`event_ndims`</b>: Scalar `integer` `Tensor` indicating the number of dimensions
    associated with a particular draw from the distribution. Must be 0 or 1.
* <b>`validate_args`</b>: Python `bool` indicating whether arguments should be
    checked for correctness.
* <b>`name`</b>: Python `str` name given to ops managed by this object.


#### Raises:

* <b>`ValueError`</b>: if `event_ndims` is not 0 or 1.
* <b>`TypeError`</b>: if `scale` is not a `LinearOperator`.
* <b>`TypeError`</b>: if `shift.dtype` does not match `scale.dtype`.
* <b>`ValueError`</b>: if not `scale.is_non_singular`.

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
    name='inverse_log_det_jacobian'
)
```

Returns the (log o det o Jacobian o inverse)(y).

Mathematically, returns: `log(det(dX/dY))(Y)`. (Recall that: `X=g^{-1}(Y)`.)

Note that `forward_log_det_jacobian` is the negative of this function,
evaluated at `g^{-1}(y)`.

#### Args:

* <b>`y`</b>: `Tensor`. The input to the "inverse" Jacobian evaluation.
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



