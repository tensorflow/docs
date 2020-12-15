description: Computes the approximate AUC (Area under the curve) via a Riemann sum.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.AUC" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="interpolate_pr_auc"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="update_state"/>
</div>

# tf.keras.metrics.AUC

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L1821-L2252">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the approximate AUC (Area under the curve) via a Riemann sum.

Inherits From: [`Metric`](../../../tf/keras/metrics/Metric.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.metrics.AUC`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.AUC`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.AUC(
    num_thresholds=200, curve='ROC', summation_method='interpolation', name=None,
    dtype=None, thresholds=None, multi_label=(False), label_weights=None
)
</code></pre>



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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_thresholds`
</td>
<td>
(Optional) Defaults to 200. The number of thresholds to
use when discretizing the roc curve. Values must be > 1.
</td>
</tr><tr>
<td>
`curve`
</td>
<td>
(Optional) Specifies the name of the curve to be computed, 'ROC'
[default] or 'PR' for the Precision-Recall-curve.
</td>
</tr><tr>
<td>
`summation_method`
</td>
<td>
(Optional) Specifies the [Riemann summation method](
https://en.wikipedia.org/wiki/Riemann_sum) used.
'interpolation' (default) applies mid-point summation scheme for `ROC`.
For PR-AUC, interpolates (true/false) positives but not the ratio that
is precision (see Davis & Goadrich 2006 for details);
'minoring' applies left summation
for increasing intervals and right summation for decreasing intervals;
'majoring' does the opposite.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional) string name of the metric instance.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(Optional) data type of the metric result.
</td>
</tr><tr>
<td>
`thresholds`
</td>
<td>
(Optional) A list of floating point values to use as the
thresholds for discretizing the curve. If set, the `num_thresholds`
parameter is ignored. Values should be in [0, 1]. Endpoint thresholds
equal to {-epsilon, 1+epsilon} for a small positive epsilon value will
be automatically included with these to correctly handle predictions
equal to exactly 0 or 1.
</td>
</tr><tr>
<td>
`multi_label`
</td>
<td>
boolean indicating whether multilabel data should be
treated as such, wherein AUC is computed separately for each label and
then averaged across labels, or (when False) if the data should be
flattened into a single label before AUC computation. In the latter
case, when multilabel data is passed to AUC, each label-prediction pair
is treated as an individual data point. Should be set to False for
multi-class data.
</td>
</tr><tr>
<td>
`label_weights`
</td>
<td>
(optional) list, array, or tensor of non-negative weights
used to compute AUCs for multilabel data. When `multi_label` is True,
the weights are applied to the individual label AUCs when they are
averaged to produce the multi-label AUC. When it's False, they are used
to weight the individual label predictions in computing the confusion
matrix on the flattened data. Note that this is unlike class_weights in
that class_weights weights the example depending on the value of its
label, whereas label_weights depends only on the index of that label
before flattening; therefore `label_weights` should not be used for
multi-class data.
</td>
</tr>
</table>



#### Standalone usage:



```
>>> m = tf.keras.metrics.AUC(num_thresholds=3)
>>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9])
>>> # threshold values are [0 - 1e-7, 0.5, 1 + 1e-7]
>>> # tp = [2, 1, 0], fp = [2, 0, 0], fn = [0, 1, 2], tn = [0, 2, 2]
>>> # recall = [1, 0.5, 0], fp_rate = [1, 0, 0]
>>> # auc = ((((1+0.5)/2)*(1-0))+ (((0.5+0)/2)*(0-0))) = 0.75
>>> m.result().numpy()
0.75
```

```
>>> m.reset_states()
>>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9],
...                sample_weight=[1, 0, 0, 1])
>>> m.result().numpy()
1.0
```

Usage with `compile()` API:

```python
model.compile(optimizer='sgd', loss='mse', metrics=[tf.keras.metrics.AUC()])
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`thresholds`
</td>
<td>
The thresholds used for evaluating AUC.
</td>
</tr>
</table>



## Methods

<h3 id="interpolate_pr_auc"><code>interpolate_pr_auc</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2093-L2172">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>interpolate_pr_auc()
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`pr_auc`
</td>
<td>
an approximation of the area under the P-R curve.
</td>
</tr>
</table>



<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2226-L2233">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states()
</code></pre>

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2174-L2224">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>result()
</code></pre>

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L2033-L2091">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    y_true, y_pred, sample_weight=None
)
</code></pre>

Accumulates confusion matrix statistics.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`y_true`
</td>
<td>
The ground truth values.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
The predicted values.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional weighting of each example. Defaults to 1. Can be a
`Tensor` whose rank is either 0, or the same rank as `y_true`, and must
be broadcastable to `y_true`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Update op.
</td>
</tr>

</table>





