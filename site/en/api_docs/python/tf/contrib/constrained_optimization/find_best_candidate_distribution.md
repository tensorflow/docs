page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.constrained_optimization.find_best_candidate_distribution


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/constrained_optimization/python/candidates.py#L138-L221">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Finds a distribution minimizing an objective subject to constraints.

``` python
tf.contrib.constrained_optimization.find_best_candidate_distribution(
    objective_vector,
    constraints_matrix,
    epsilon=0.0
)
```



<!-- Placeholder for "Used in" -->

This function deals with the constrained problem:

> minimize f(w)
> s.t. g_i(w) <= 0 for all i in {0,1,...,m-1}

Here, f(w) is the "objective function", and g_i(w) is the ith (of m)
"constraint function". Given a set of n "candidate solutions"
{w_0,w_1,...,w_{n-1}}, this function finds a distribution over these n
candidates that, in expectation, minimizes the objective while violating
the constraints by the smallest possible amount (with the amount being found
via bisection search).

The `objective_vector` parameter should be a numpy array with shape (n,), for
which objective_vector[i] = f(w_i). Likewise, `constraints_matrix` should be a
numpy array with shape (m,n), for which constraints_matrix[i,j] = g_i(w_j).

This function will return a distribution for which at most m+1 probabilities,
and often fewer, are nonzero.

For more specifics, please refer to:

> Cotter, Jiang and Sridharan. "Two-Player Games for Efficient Non-Convex
> Constrained Optimization".
> [https://arxiv.org/abs/1804.06500](https://arxiv.org/abs/1804.06500)

This function implements the approach described in Lemma 3.

#### Args:


* <b>`objective_vector`</b>: numpy array of shape (n,), where n is the number of
  "candidate solutions". Contains the objective function values.
* <b>`constraints_matrix`</b>: numpy array of shape (m,n), where m is the number of
  constraints and n is the number of "candidate solutions". Contains the
  constraint violation magnitudes.
* <b>`epsilon`</b>: nonnegative float, the threshold at which to terminate the binary
  search while searching for the minimal expected constraint violation
  magnitude.


#### Returns:

The optimal distribution, as a numpy array of shape (n,).



#### Raises:


* <b>`ValueError`</b>: If `objective_vector` and `constraints_matrix` have inconsistent
  shapes, or if `epsilon` is negative.
* <b>`ImportError`</b>: If we're unable to import `scipy.optimize`.
