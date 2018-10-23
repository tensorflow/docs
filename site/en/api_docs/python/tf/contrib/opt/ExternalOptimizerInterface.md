

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.opt.ExternalOptimizerInterface

### `class tf.contrib.opt.ExternalOptimizerInterface`



Defined in [`tensorflow/contrib/opt/python/training/external_optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/opt/python/training/external_optimizer.py).

Base class for interfaces with external optimization algorithms.

Subclass this and implement `_minimize` in order to wrap a new optimization
algorithm.

`ExternalOptimizerInterface` should not be instantiated directly; instead use
e.g. `ScipyOptimizerInterface`.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    loss,
    var_list=None,
    equalities=None,
    inequalities=None,
    **optimizer_kwargs
)
```

Initialize a new interface instance.

#### Args:

* <b>`loss`</b>: A scalar `Tensor` to be minimized.
* <b>`var_list`</b>: Optional list of `Variable` objects to update to minimize
    `loss`.  Defaults to the list of variables collected in the graph
    under the key `GraphKeys.TRAINABLE_VARIABLES`.
* <b>`equalities`</b>: Optional list of equality constraint scalar `Tensor`s to be
    held equal to zero.
* <b>`inequalities`</b>: Optional list of inequality constraint scalar `Tensor`s
    to be kept nonnegative.
  **optimizer_kwargs: Other subclass-specific keyword arguments.

<h3 id="minimize"><code>minimize</code></h3>

``` python
minimize(
    session=None,
    feed_dict=None,
    fetches=None,
    step_callback=None,
    loss_callback=None,
    **run_kwargs
)
```

Minimize a scalar `Tensor`.

Variables subject to optimization are updated in-place at the end of
optimization.

Note that this method does *not* just return a minimization `Op`, unlike
`Optimizer.minimize()`; instead it actually performs minimization by
executing commands to control a `Session`.

#### Args:

* <b>`session`</b>: A `Session` instance.
* <b>`feed_dict`</b>: A feed dict to be passed to calls to `session.run`.
* <b>`fetches`</b>: A list of `Tensor`s to fetch and supply to `loss_callback`
    as positional arguments.
* <b>`step_callback`</b>: A function to be called at each optimization step;
    arguments are the current values of all optimization variables
    flattened into a single vector.
* <b>`loss_callback`</b>: A function to be called every time the loss and gradients
    are computed, with evaluated fetches supplied as positional arguments.
  **run_kwargs: kwargs to pass to `session.run`.



