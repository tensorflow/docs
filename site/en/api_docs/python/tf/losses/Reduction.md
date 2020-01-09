page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.Reduction


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/losses/losses_impl.py#L38-L72">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Reduction`

Types of loss reduction.



### Aliases:

* Class <a href="/api_docs/python/tf/losses/Reduction"><code>tf.compat.v1.losses.Reduction</code></a>


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/losses/losses_impl.py#L59-L67">View source</a>

``` python
@classmethod
all(cls)
```




<h3 id="validate"><code>validate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/losses/losses_impl.py#L69-L72">View source</a>

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
