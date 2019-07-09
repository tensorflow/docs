page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.constrained_optimization.ConstrainedMinimizationProblem

## Class `ConstrainedMinimizationProblem`





Defined in [`tensorflow/contrib/constrained_optimization/python/constrained_minimization_problem.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/constrained_optimization/python/constrained_minimization_problem.py).

Abstract class representing a `ConstrainedMinimizationProblem`.

A ConstrainedMinimizationProblem consists of an objective function to
minimize, and a set of constraint functions that are constrained to be
nonpositive.

In addition to the constraint functions, there may (optionally) be proxy
constraint functions: a ConstrainedOptimizer will attempt to penalize these
proxy constraint functions so as to satisfy the (non-proxy) constraints. Proxy
constraints could be used if the constraints functions are difficult or
impossible to optimize (e.g. if they're piecewise constant), in which case the
proxy constraints should be some approximation of the original constraints
that is well-enough behaved to permit successful optimization.

## Properties

<h3 id="constraints"><code>constraints</code></h3>

Returns the vector of constraint functions.

Letting g_i be the ith element of the constraints vector, the ith constraint
will be g_i <= 0.

#### Returns:

A tensor of constraint functions.

<h3 id="num_constraints"><code>num_constraints</code></h3>

Returns the number of constraints.

#### Returns:

An int containing the number of constraints.


#### Raises:

* <b>`ValueError`</b>: If the constraints (or proxy_constraints, if present) do not
    have fully-known shapes, OR if proxy_constraints are present, and the
    shapes of constraints and proxy_constraints are fully-known, but they're
    different.

<h3 id="objective"><code>objective</code></h3>

Returns the objective function.

#### Returns:

A 0d tensor that should be minimized.

<h3 id="pre_train_ops"><code>pre_train_ops</code></h3>

Returns a list of `Operation`s to run before the train_op.

When a `ConstrainedOptimizer` creates a train_op (in `minimize`
`minimize_unconstrained`, or `minimize_constrained`), it will include these
ops before the main training step.

#### Returns:

A list of `Operation`s.

<h3 id="proxy_constraints"><code>proxy_constraints</code></h3>

Returns the optional vector of proxy constraint functions.

The difference between `constraints` and `proxy_constraints` is that, when
proxy constraints are present, the `constraints` are merely EVALUATED during
optimization, whereas the `proxy_constraints` are DIFFERENTIATED. If there
are no proxy constraints, then the `constraints` are both evaluated and
differentiated.

For example, if we want to impose constraints on step functions, then we
could use these functions for `constraints`. However, because a step
function has zero gradient almost everywhere, we can't differentiate these
functions, so we would take `proxy_constraints` to be some differentiable
approximation of `constraints`.

#### Returns:

A tensor of proxy constraint functions.



