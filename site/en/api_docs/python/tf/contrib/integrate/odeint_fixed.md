page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.integrate.odeint_fixed

``` python
tf.contrib.integrate.odeint_fixed(
    func,
    y0,
    t,
    dt=None,
    method='rk4',
    name=None
)
```



Defined in [`tensorflow/contrib/integrate/python/ops/odes.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/integrate/python/ops/odes.py).

ODE integration on a fixed grid (with no step size control).

Useful in certain scenarios to avoid the overhead of adaptive step size
control, e.g. when differentiation of the integration result is desired and/or
the time grid is known a priori to be sufficient.

#### Args:

* <b>`func`</b>: Function that maps a Tensor holding the state `y` and a scalar Tensor
    `t` into a Tensor of state derivatives with respect to time.
* <b>`y0`</b>: N-D Tensor giving starting value of `y` at time point `t[0]`.
* <b>`t`</b>: 1-D Tensor holding a sequence of time points for which to solve for
    `y`. The initial time point should be the first element of this sequence,
    and each time must be larger than the previous time. May have any floating
    point dtype.
* <b>`dt`</b>: 0-D or 1-D Tensor providing time step suggestion to be used on time
    integration intervals in `t`. 1-D Tensor should provide values
    for all intervals, must have 1 less element than that of `t`.
    If given a 0-D Tensor, the value is interpreted as time step suggestion
    same for all intervals. If passed None, then time step is set to be the
    t[1:] - t[:-1]. Defaults to None. The actual step size is obtained by
    insuring an integer number of steps per interval, potentially reducing the
    time step.
* <b>`method`</b>: One of 'midpoint' or 'rk4'.
* <b>`name`</b>: Optional name for the resulting operation.


#### Returns:

* <b>`y`</b>: (N+1)-D tensor, where the first dimension corresponds to different
    time points. Contains the solved value of y for each desired time point in
    `t`, with the initial value `y0` being the first element along the first
    dimension.


#### Raises:

* <b>`ValueError`</b>: Upon caller errors.