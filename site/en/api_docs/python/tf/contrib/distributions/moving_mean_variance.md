page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distributions.moving_mean_variance


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distributions/python/ops/moving_stats.py#L176-L246">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute exponentially weighted moving {mean,variance} of a streaming value.

``` python
tf.contrib.distributions.moving_mean_variance(
    value,
    decay,
    collections=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The exponentially-weighting moving `mean_var` and `variance_var` are updated
by `value` according to the following recurrence:

```python
variance_var = decay * (variance_var + (1-decay) * (value - mean_var)**2)
mean_var     = decay * mean_var + (1 - decay) * value
```

Note: `mean_var` is updated *after* `variance_var`, i.e., `variance_var` uses
the lag-`1` mean.

For derivation justification, see [Finch (2009; Eq. 143)][1].

Unlike `assign_moving_mean_variance`, this function handles
variable creation.

#### Args:


* <b>`value`</b>: `float`-like `Tensor`. Same shape as `mean_var` and `variance_var`.
* <b>`decay`</b>: A `float`-like `Tensor`. The moving mean decay. Typically close to
  `1.`, e.g., `0.999`.
* <b>`collections`</b>: Python list of graph-collections keys to which the internal
  variables `mean_var` and `variance_var` are added.
  Default value is `[GraphKeys.GLOBAL_VARIABLES]`.
* <b>`name`</b>: Optional name of the returned operation.


#### Returns:


* <b>`mean_var`</b>: `Variable` representing the `value`-updated exponentially weighted
  moving mean.
* <b>`variance_var`</b>: `Variable` representing the `value`-updated
  exponentially weighted moving variance.


#### Raises:


* <b>`TypeError`</b>: if `value_var` does not have float type `dtype`.
* <b>`TypeError`</b>: if `value`, `decay` have different `base_dtype`.

#### References

[1]: Tony Finch. Incremental calculation of weighted mean and variance.
     _Technical Report_, 2009.
     http://people.ds.cam.ac.uk/fanf2/hermes/doc/antiforgery/stats.pdf
