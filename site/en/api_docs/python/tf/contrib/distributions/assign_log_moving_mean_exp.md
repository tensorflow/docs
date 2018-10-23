

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.assign_log_moving_mean_exp

``` python
tf.contrib.distributions.assign_log_moving_mean_exp(
    log_mean_exp_var,
    log_value,
    decay,
    name=None
)
```



Defined in [`tensorflow/contrib/distributions/python/ops/moving_stats.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/distributions/python/ops/moving_stats.py).

Compute the log of the exponentially weighted moving mean of the exp.

If `log_value` is a draw from a stationary random variable, this function
approximates `log(E[exp(log_value)])`, i.e., a weighted log-sum-exp. More
precisely, a `tf.Variable`, `log_mean_exp_var`, is updated by `log_value`
using the following identity:

```none
log_mean_exp_var =
= log(decay exp(log_mean_exp_var) + (1 - decay) exp(log_value))
= log(exp(log_mean_exp_var + log(decay)) + exp(log_value + log1p(-decay)))
= log_mean_exp_var
  + log(  exp(log_mean_exp_var   - log_mean_exp_var + log(decay))
        + exp(log_value - log_mean_exp_var + log1p(-decay)))
= log_mean_exp_var
  + log_sum_exp([log(decay), log_value - log_mean_exp_var + log1p(-decay)]).
```

In addition to numerical stability, this formulation is advantageous because
`log_mean_exp_var` can be updated in a lock-free manner, i.e., using
`assign_add`. (Note: the updates are not thread-safe; it's just that the
update to the tf.Variable is presumed efficient due to being lock-free.)

#### Args:

* <b>`log_mean_exp_var`</b>: `float`-like `Variable` representing the log of the
    exponentially weighted moving mean of the exp. Same shape as `log_value`.
* <b>`log_value`</b>: `float`-like `Tensor` representing a new (streaming) observation.
    Same shape as `log_mean_exp_var`.
* <b>`decay`</b>: A `float`-like `Tensor`. The moving mean decay. Typically close to
    `1.`, e.g., `0.999`.
* <b>`name`</b>: Optional name of the returned operation.


#### Returns:

* <b>`log_mean_exp_var`</b>: A reference to the input 'Variable' tensor with the
    `log_value`-updated log of the exponentially weighted moving mean of exp.


#### Raises:

* <b>`TypeError`</b>: if `log_mean_exp_var` does not have float type `dtype`.
* <b>`TypeError`</b>: if `log_mean_exp_var`, `log_value`, `decay` have different
    `base_dtype`.