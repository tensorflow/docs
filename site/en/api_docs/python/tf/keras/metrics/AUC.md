page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.AUC


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics/AUC">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1589-L1869">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `AUC`

Computes the approximate AUC (Area under the curve) via a Riemann sum.

Inherits From: [`Metric`](../../../tf/keras/metrics/Metric)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/metrics/AUC"><code>tf.compat.v1.keras.metrics.AUC</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/AUC"><code>tf.compat.v2.keras.metrics.AUC</code></a>
* Class <a href="/api_docs/python/tf/keras/metrics/AUC"><code>tf.compat.v2.metrics.AUC</code></a>


<!-- Placeholder for "Used in" -->

This metric creates four local variables, `true_positives`, `true_negatives`,
`false_positives` and `false_negatives` that are used to compute the AUC.
To discretize the AUC curve, a linearly spaced set of thresholds is used to
compute pairs of recall and precision values. The area under the ROC-curve is
therefore computed using the height of the recall values by the false positive
rate, while the area under the PR-curve is the computed using the height of
the precision values by the recall.

This value is ultimately returned as `auc`, an idempotent operation that
computes the area under a discretized curve of precision versus recall values
(computed using the aforementioned variables). The `num_thresholds` variable
controls the degree of discretization with larger numbers of thresholds more
closely approximating the true AUC. The quality of the approximation may vary
dramatically depending on `num_thresholds`. The `thresholds` parameter can be
used to manually specify thresholds which split the predictions more evenly.

For best results, `predictions` should be distributed approximately uniformly
in the range [0, 1] and not peaked around 0 or 1. The quality of the AUC
approximation may be poor if this is not the case. Setting `summation_method`
to 'minoring' or 'majoring' can help quantify the error in the approximation
by providing lower or upper bound estimate of the AUC.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.AUC(num_thresholds=3)
m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9])

# threshold values are [0 - 1e-7, 0.5, 1 + 1e-7]
# tp = [2, 1, 0], fp = [2, 0, 0], fn = [0, 1, 2], tn = [0, 2, 2]
# recall = [1, 0.5, 0], fp_rate = [1, 0, 0]
# auc = ((((1+0.5)/2)*(1-0))+ (((0.5+0)/2)*(0-0))) = 0.75

print('Final result: ', m.result().numpy())  # Final result: 0.75
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss='mse', metrics=[tf.keras.metrics.AUC()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1639-L1728">View source</a>

``` python
__init__(
    num_thresholds=200,
    curve='ROC',
    summation_method='interpolation',
    name=None,
    dtype=None,
    thresholds=None
)
```

Creates an `AUC` instance.


#### Args:


* <b>`num_thresholds`</b>: (Optional) Defaults to 200. The number of thresholds to
  use when discretizing the roc curve. Values must be > 1.
* <b>`curve`</b>: (Optional) Specifies the name of the curve to be computed, 'ROC'
  [default] or 'PR' for the Precision-Recall-curve.
* <b>`summation_method`</b>: (Optional) Specifies the Riemann summation method used
  (https://en.wikipedia.org/wiki/Riemann_sum): 'interpolation' [default],
    applies mid-point summation scheme for `ROC`. For PR-AUC, interpolates
    (true/false) positives but not the ratio that is precision (see Davis
    & Goadrich 2006 for details); 'minoring' that applies left summation
    for increasing intervals and right summation for decreasing intervals;
    'majoring' that does the opposite.
* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`thresholds`</b>: (Optional) A list of floating point values to use as the
  thresholds for discretizing the curve. If set, the `num_thresholds`
  parameter is ignored. Values should be in [0, 1]. Endpoint thresholds
  equal to {-epsilon, 1+epsilon} for a small positive epsilon value will
  be automatically included with these to correctly handle predictions
  equal to exactly 0 or 1.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L145-L161">View source</a>

``` python
__new__(
    cls,
    *args,
    **kwargs
)
```

Create and return a new object.  See help(type) for accurate signature.




## Methods

<h3 id="interpolate_pr_auc"><code>interpolate_pr_auc</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1750-L1817">View source</a>

``` python
interpolate_pr_auc()
```

Interpolation formula inspired by section 4 of Davis & Goadrich 2006.

https://www.biostat.wisc.edu/~page/rocpr.pdf

Note here we derive & use a closed formula not present in the paper
as follows:

  Precision = TP / (TP + FP) = TP / P

Modeling all of TP (true positive), FP (false positive) and their sum
P = TP + FP (predicted positive) as varying linearly within each interval
[A, B] between successive thresholds, we get

  Precision slope = dTP / dP
                  = (TP_B - TP_A) / (P_B - P_A)
                  = (TP - TP_A) / (P - P_A)
  Precision = (TP_A + slope * (P - P_A)) / P

The area within the interval is (slope / total_pos_weight) times

  int_A^B{Precision.dP} = int_A^B{(TP_A + slope * (P - P_A)) * dP / P}
  int_A^B{Precision.dP} = int_A^B{slope * dP + intercept * dP / P}

where intercept = TP_A - slope * P_A = TP_B - slope * P_B, resulting in

  int_A^B{Precision.dP} = TP_B - TP_A + intercept * log(P_B / P_A)

Bringing back the factor (slope / total_pos_weight) we'd put aside, we get

  slope * [dTP + intercept *  log(P_B / P_A)] / total_pos_weight

where dTP == TP_B - TP_A.

Note that when P_A == 0 the above calculation simplifies into

  int_A^B{Precision.dTP} = int_A^B{slope * dTP} = slope * (TP_B - TP_A)

which is really equivalent to imputing constant precision throughout the
first bucket having >0 true positives.

#### Returns:


* <b>`pr_auc`</b>: an approximation of the area under the P-R curve.

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1854-L1856">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1819-L1852">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/metrics.py#L1730-L1748">View source</a>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates confusion matrix statistics.


#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be a
  `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
  be broadcastable to `y_true`.


#### Returns:

Update op.
