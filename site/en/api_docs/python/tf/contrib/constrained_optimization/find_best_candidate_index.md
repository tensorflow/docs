page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.constrained_optimization.find_best_candidate_index

``` python
tf.contrib.constrained_optimization.find_best_candidate_index(
    objective_vector,
    constraints_matrix,
    rank_objectives=False
)
```



Defined in [`tensorflow/contrib/constrained_optimization/python/candidates.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/constrained_optimization/python/candidates.py).

Heuristically finds the best candidate solution to a constrained problem.

This function deals with the constrained problem:

> minimize f(w)
> s.t. g_i(w) <= 0 for all i in {0,1,...,m-1}

Here, f(w) is the "objective function", and g_i(w) is the ith (of m)
"constraint function". Given a set of n "candidate solutions"
{w_0,w_1,...,w_{n-1}}, this function finds the "best" solution according
to the following heuristic:

  1. Across all models, the ith constraint violations (i.e. max{0, g_i(0)})
     are ranked, as are the objectives (if rank_objectives=True).
  2. Each model is then associated its MAXIMUM rank across all m constraints
     (and the objective, if rank_objectives=True).
  3. The model with the minimal maximum rank is then identified. Ties are
     broken using the objective function value.
  4. The index of this "best" model is returned.

The `objective_vector` parameter should be a numpy array with shape (n,), for
which objective_vector[i] = f(w_i). Likewise, `constraints_matrix` should be a
numpy array with shape (m,n), for which constraints_matrix[i,j] = g_i(w_j).

For more specifics, please refer to:

> Cotter, Jiang and Sridharan. "Two-Player Games for Efficient Non-Convex
> Constrained Optimization".
> [https://arxiv.org/abs/1804.06500](https://arxiv.org/abs/1804.06500)

This function implements the heuristic used for hyperparameter search in the
experiments of Section 5.2.

#### Args:

* <b>`objective_vector`</b>: numpy array of shape (n,), where n is the number of
    "candidate solutions". Contains the objective function values.
* <b>`constraints_matrix`</b>: numpy array of shape (m,n), where m is the number of
    constraints and n is the number of "candidate solutions". Contains the
    constraint violation magnitudes.
* <b>`rank_objectives`</b>: bool, whether the objective function values should be
    included in the initial ranking step. If True, both the objective and
    constraints will be ranked. If False, only the constraints will be ranked.
    In either case, the objective function values will be used for
    tiebreaking.


#### Returns:

The index (in {0,1,...,n-1}) of the "best" model according to the above
  heuristic.


#### Raises:

* <b>`ValueError`</b>: If `objective_vector` and `constraints_matrix` have inconsistent
    shapes.
* <b>`ImportError`</b>: If we're unable to import `scipy.stats`.