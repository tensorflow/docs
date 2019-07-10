page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.Reduction

## Class `Reduction`

Types of loss reduction.



### Aliases:

* Class `tf.compat.v1.losses.Reduction`
* Class `tf.losses.Reduction`



Defined in [`python/ops/losses/losses_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/losses/losses_impl.py).

<!-- Placeholder for "Used in" -->

Contains the following values:

* `NONE`: Un-reduced weighted losses with the same shape as input.
* `SUM`: Scalar sum of weighted losses.
* `MEAN`: Scalar `SUM` divided by sum of weights. DEPRECATED.
* `SUM_OVER_BATCH_SIZE`: Scalar `SUM` divided by number of elements in losses.
* `SUM_OVER_NONZERO_WEIGHTS`: Scalar `SUM` divided by number of non-zero
   weights. DEPRECATED.
* `SUM_BY_NONZERO_WEIGHTS`: Same as `SUM_OVER_NONZERO_WEIGHTS`. DEPRECATED.

## Methods

<h3 id="all"><code>all</code></h3>

``` python
@classmethod
all(cls)
```




<h3 id="validate"><code>validate</code></h3>

``` python
@classmethod
validate(
    cls,
    key
)
```






## Class Members

* `MEAN = 'weighted_mean'` <a id="MEAN"></a>
* `NONE = 'none'` <a id="NONE"></a>
* `SUM = 'weighted_sum'` <a id="SUM"></a>
* `SUM_BY_NONZERO_WEIGHTS = 'weighted_sum_by_nonzero_weights'` <a id="SUM_BY_NONZERO_WEIGHTS"></a>
* `SUM_OVER_BATCH_SIZE = 'weighted_sum_over_batch_size'` <a id="SUM_OVER_BATCH_SIZE"></a>
* `SUM_OVER_NONZERO_WEIGHTS = 'weighted_sum_by_nonzero_weights'` <a id="SUM_OVER_NONZERO_WEIGHTS"></a>
