page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.ExternalOptimizerInterface


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/external_optimizer.py#L32-L296">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ExternalOptimizerInterface`

Base class for interfaces with external optimization algorithms.



<!-- Placeholder for "Used in" -->

Subclass this and implement `_minimize` in order to wrap a new optimization
algorithm.

`ExternalOptimizerInterface` should not be instantiated directly; instead use
e.g. `ScipyOptimizerInterface`.



<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/external_optimizer.py#L46-L140">View source</a>

``` python
__init__(
    loss,
    var_list=None,
    equalities=None,
    inequalities=None,
    var_to_bounds=None,
    **optimizer_kwargs
)
```

Initialize a new interface instance.


#### Args:


* <b>`loss`</b>: A scalar `Tensor` to be minimized.
* <b>`var_list`</b>: Optional `list` of `Variable` objects to update to minimize
  `loss`.  Defaults to the list of variables collected in the graph
  under the key <a href="/api_docs/python/tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a>.
* <b>`equalities`</b>: Optional `list` of equality constraint scalar `Tensor`s to be
  held equal to zero.
* <b>`inequalities`</b>: Optional `list` of inequality constraint scalar `Tensor`s
  to be held nonnegative.
* <b>`var_to_bounds`</b>: Optional `dict` where each key is an optimization
  `Variable` and each corresponding value is a length-2 tuple of
  `(low, high)` bounds. Although enforcing this kind of simple constraint
  could be accomplished with the `inequalities` arg, not all optimization
  algorithms support general inequality constraints, e.g. L-BFGS-B. Both
  `low` and `high` can either be numbers or anything convertible to a
  NumPy array that can be broadcast to the shape of `var` (using
  `np.broadcast_to`). To indicate that there is no bound, use `None` (or
  `+/- np.infty`). For example, if `var` is a 2x3 matrix, then any of
  the following corresponding `bounds` could be supplied:
  * `(0, np.infty)`: Each element of `var` held positive.
  * `(-np.infty, [1, 2])`: First column less than 1, second column less
    than 2.
  * `(-np.infty, [[1], [2], [3]])`: First row less than 1, second row less
    than 2, etc.
  * `(-np.infty, [[1, 2, 3], [4, 5, 6]])`: Entry `var[0, 0]` less than 1,
    `var[0, 1]` less than 2, etc.
* <b>`**optimizer_kwargs`</b>: Other subclass-specific keyword arguments.



## Methods

<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/external_optimizer.py#L142-L216">View source</a>

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
<a href="/api_docs/python/tf/keras/optimizers/Optimizer#minimize"><code>Optimizer.minimize()</code></a>; instead it actually performs minimization by
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
* <b>`**run_kwargs`</b>: kwargs to pass to `session.run`.
