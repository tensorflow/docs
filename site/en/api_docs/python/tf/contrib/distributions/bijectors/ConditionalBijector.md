

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.bijectors.ConditionalBijector

## Class `ConditionalBijector`

Inherits From: [`Bijector`](../../../../tf/distributions/bijectors/Bijector)



Defined in [`tensorflow/contrib/distributions/python/ops/bijectors/conditional_bijector.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/distributions/python/ops/bijectors/conditional_bijector.py).

Conditional Bijector is a Bijector that allows intrinsic conditioning.

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


#### Raises:

* <b>`ValueError`</b>:  If a member of `graph_parents` is not a `Tensor`.

<h3 id="forward"><code>forward</code></h3>

``` python
forward(
    *args,
    **kwargs
)
```

##### `kwargs`:

*  `**condition_kwargs`: Named arguments forwarded to subclass implementation.

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
    *args,
    **kwargs
)
```

##### `kwargs`:

*  `**condition_kwargs`: Named arguments forwarded to subclass implementation.

<h3 id="inverse"><code>inverse</code></h3>

``` python
inverse(
    *args,
    **kwargs
)
```

##### `kwargs`:

*  `**condition_kwargs`: Named arguments forwarded to subclass implementation.

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
    *args,
    **kwargs
)
```

##### `kwargs`:

*  `**condition_kwargs`: Named arguments forwarded to subclass implementation.



