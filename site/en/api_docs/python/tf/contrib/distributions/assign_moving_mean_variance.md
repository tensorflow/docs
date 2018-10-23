

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.assign_moving_mean_variance

``` python
tf.contrib.distributions.assign_moving_mean_variance(
    mean_var,
    variance_var,
    value,
    decay,
    name=None
)
```



Defined in [`tensorflow/contrib/distributions/python/ops/moving_stats.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/distributions/python/ops/moving_stats.py).

Compute exponentially weighted moving {mean,variance} of a streaming value.

The `value` updated exponentially weighted moving `mean_var` and
`variance_var` are given by the following recurrence relations:

```python
variance_var = decay * (variance_var + (1-decay) * (value - mean_var)**2)
mean_var     = decay * mean_var + (1 - decay) * value
```

Note: `mean_var` is updated *after* `variance_var`, i.e., `variance_var` uses
the lag-1 mean.

For derivation justification, see equation 143 of:
  T. Finch, Feb 2009. "Incremental calculation of weighted mean and variance".
  http://people.ds.cam.ac.uk/fanf2/hermes/doc/antiforgery/stats.pdf

#### Args:

* <b>`mean_var`</b>: `float`-like `Variable` representing the exponentially weighted
    moving mean. Same shape as `variance_var` and `value`.
* <b>`variance_var`</b>: `float`-like `Variable` representing the
    exponentially weighted moving variance. Same shape as `mean_var` and
    `value`.
* <b>`value`</b>: `float`-like `Tensor`. Same shape as `mean_var` and `variance_var`.
* <b>`decay`</b>: A `float`-like `Tensor`. The moving mean decay. Typically close to
    `1.`, e.g., `0.999`.
* <b>`name`</b>: Optional name of the returned operation.


#### Returns:

* <b>`mean_var`</b>: `Variable` representing the `value`-updated exponentially weighted
    moving mean.
* <b>`variance_var`</b>: `Variable` representing the `value`-updated
    exponentially weighted moving variance.


#### Raises:

* <b>`TypeError`</b>: if `mean_var` does not have float type `dtype`.
* <b>`TypeError`</b>: if `mean_var`, `variance_var`, `value`, `decay` have different
    `base_dtype`.