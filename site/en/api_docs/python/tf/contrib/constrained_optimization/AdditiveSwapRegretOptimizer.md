page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.constrained_optimization.AdditiveSwapRegretOptimizer

## Class `AdditiveSwapRegretOptimizer`

A `ConstrainedOptimizer` based on swap-regret minimization.





Defined in [`contrib/constrained_optimization/python/swap_regret_optimizer.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/constrained_optimization/python/swap_regret_optimizer.py).

<!-- Placeholder for "Used in" -->

This `ConstrainedOptimizer` uses the given <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>s to
jointly
minimize over the model parameters, and maximize over constraint/objective
weight matrix (the analogue of Lagrange multipliers), with the latter
maximization using additive updates and an algorithm that minimizes swap
regret.

For more specifics, please refer to:

> Cotter, Jiang and Sridharan. "Two-Player Games for Efficient Non-Convex
> Constrained Optimization".
> [https://arxiv.org/abs/1804.06500](https://arxiv.org/abs/1804.06500)

The formulation used by this optimizer can be found in Definition 2, and is
discussed in Section 4. It is most similar to Algorithm 2 in Section 4, with
the differences being that it uses <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>s, instead of
SGD, for
the "inner" updates, and performs additive (instead of multiplicative) updates
of the stochastic matrix.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    optimizer,
    constraint_optimizer=None
)
```

Constructs a new `AdditiveSwapRegretOptimizer`.


#### Args:


* <b>`optimizer`</b>: tf.compat.v1.train.Optimizer, used to optimize the objective
  and proxy_constraints portion of ConstrainedMinimizationProblem. If
  constraint_optimizer is not provided, this will also be used to optimize
  the Lagrange multiplier analogues.
* <b>`constraint_optimizer`</b>: optional tf.compat.v1.train.Optimizer, used to
  optimize the Lagrange multiplier analogues.


#### Returns:

A new `AdditiveSwapRegretOptimizer`.




## Properties

<h3 id="constraint_optimizer"><code>constraint_optimizer</code></h3>

Returns the <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a> used for the matrix.


<h3 id="optimizer"><code>optimizer</code></h3>

Returns the <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a> used for optimization.




## Methods

<h3 id="minimize"><code>minimize</code></h3>

``` python
minimize(
    minimization_problem,
    unconstrained_steps=None,
    global_step=None,
    var_list=None,
    gate_gradients=train_optimizer.Optimizer.GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    name=None,
    grad_loss=None
)
```

Returns an `Operation` for minimizing the constrained problem.

This method combines the functionality of `minimize_unconstrained` and
`minimize_constrained`. If global_step < unconstrained_steps, it will
perform an unconstrained update, and if global_step >= unconstrained_steps,
it will perform a constrained update.

The reason for this functionality is that it may be best to initialize the
constrained optimizer with an approximate optimum of the unconstrained
problem.

#### Args:


* <b>`minimization_problem`</b>: ConstrainedMinimizationProblem, the problem to
  optimize.
* <b>`unconstrained_steps`</b>: int, number of steps for which we should perform
  unconstrained updates, before transitioning to constrained updates.
* <b>`global_step`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`var_list`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`gate_gradients`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`aggregation_method`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize`
  method.
* <b>`colocate_gradients_with_ops`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s
  `minimize` method.
* <b>`name`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`grad_loss`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.


#### Returns:

`Operation`, the train_op.



#### Raises:


* <b>`ValueError`</b>: If unconstrained_steps is provided, but global_step is not.

<h3 id="minimize_constrained"><code>minimize_constrained</code></h3>

``` python
minimize_constrained(
    minimization_problem,
    global_step=None,
    var_list=None,
    gate_gradients=train_optimizer.Optimizer.GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    name=None,
    grad_loss=None
)
```

Returns an `Operation` for minimizing the constrained problem.

Unlike `minimize_unconstrained`, this function attempts to find a solution
that minimizes the `objective` portion of the minimization problem while
satisfying the `constraints` portion.

#### Args:


* <b>`minimization_problem`</b>: ConstrainedMinimizationProblem, the problem to
  optimize.
* <b>`global_step`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`var_list`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`gate_gradients`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`aggregation_method`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize`
  method.
* <b>`colocate_gradients_with_ops`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s
  `minimize` method.
* <b>`name`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`grad_loss`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.


#### Returns:

`Operation`, the train_op.


<h3 id="minimize_unconstrained"><code>minimize_unconstrained</code></h3>

``` python
minimize_unconstrained(
    minimization_problem,
    global_step=None,
    var_list=None,
    gate_gradients=train_optimizer.Optimizer.GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    name=None,
    grad_loss=None
)
```

Returns an `Operation` for minimizing the unconstrained problem.

Unlike `minimize_constrained`, this function ignores the `constraints` (and
`proxy_constraints`) portion of the minimization problem entirely, and only
minimizes `objective`.

#### Args:


* <b>`minimization_problem`</b>: ConstrainedMinimizationProblem, the problem to
  optimize.
* <b>`global_step`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`var_list`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`gate_gradients`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`aggregation_method`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize`
  method.
* <b>`colocate_gradients_with_ops`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s
  `minimize` method.
* <b>`name`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.
* <b>`grad_loss`</b>: as in <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>'s `minimize` method.


#### Returns:

`Operation`, the train_op.




