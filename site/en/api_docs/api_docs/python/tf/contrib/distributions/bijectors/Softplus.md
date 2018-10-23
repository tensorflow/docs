

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.bijectors.Softplus

## Class `Softplus`

Inherits From: [`Bijector`](../../../../tf/distributions/bijectors/Bijector)



Defined in [`tensorflow/contrib/distributions/python/ops/bijectors/softplus_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/distributions/python/ops/bijectors/softplus_impl.py).

See the guide: [Random variable transformations (contrib) > Bijectors](../../../../../../api_guides/python/contrib.distributions.bijectors#Bijectors)

Bijector which computes `Y = g(X) = Log[1 + exp(X)]`.

The softplus `Bijector` has the following two useful properties:

* The domain is the positive real numbers
* `softplus(x) approx x`, for large `x`, so it does not overflow as easily as
  the `Exp` `Bijector`.

The optional nonzero `hinge_softness` parameter changes the transition at
zero.  With `hinge_softness = c`, the bijector is:

>     
>     r large `x >> 1`, `c * Log[1 + exp(x / c)] approx c * Log[exp(x / c)] = x`,
>      the behavior for large `x` is the same as the standard softplus.
>     
>      `c > 0` approaches 0 from the right, `f_c(x)` becomes less and less soft,
>     proaching `max(0, x)`.
>     
>     `c = 1` is the default.
>     `c > 0` but small means `f(x) approx ReLu(x) = max(0, x)`.
>     `c < 0` flips sign and reflects around the `y-axis`: `f_{-c}(x) = -f_c(-x)`.
>     `c = 0` results in a non-bijective transformation and triggers an exception.
>     
>     Example Use:
>     
  # Create the Y=g(X)=softplus(X) transform which works only on Tensors with 1
  # batch ndim and 2 event ndims (i.e., vector of matrices).
  softplus = Softplus(event_ndims=2)
  x = [[[1., 2],
        [3, 4]],
       [[5, 6],
        [7, 8]]]
  log(1 + exp(x)) == softplus.forward(x)
  log(exp(x) - 1) == softplus.inverse(x)
>     
>     Note: log(.) and exp(.) are applied element-wise but the Jacobian is a
>     reduction over the event space.
>     
>      Properties
>     
>     3 id="dtype"><code>dtype</code></h3>
>     
>     ype of `Tensor`s transformable by this distribution.
>     
>     3 id="event_ndims"><code>event_ndims</code></h3>
>     
>     turns then number of event dimensions this bijector operates on.
>     
>     3 id="graph_parents"><code>graph_parents</code></h3>
>     
>     turns this `Bijector`'s graph_parents as a Python list.
>     
>     3 id="hinge_softness"><code>hinge_softness</code></h3>
>     
>     
>     
>     3 id="is_constant_jacobian"><code>is_constant_jacobian</code></h3>
>     
>     turns true iff the Jacobian is not a function of x.
>     
>     te: Jacobian is either constant for both forward and inverse or neither.
>     
>     ## Returns:
>     
>     <b>`is_constant_jacobian`</b>: Python `bool`.
>     
>     3 id="name"><code>name</code></h3>
>     
>     turns the string name of this `Bijector`.
>     
>     3 id="validate_args"><code>validate_args</code></h3>
>     
>     turns True if Tensor arguments will be validated.
>     
>     
>     
>      Methods
>     
>     3 id="__init__"><code>__init__</code></h3>
>     

``` python
__init__(
    *args,
    **kwargs
)
```

##### `kwargs`:

*  `hinge_softness`: Nonzero floating point `Tensor`.  Controls the softness of what would otherwise be a kink at the origin.  Default is 1.0

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



