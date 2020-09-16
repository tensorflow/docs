description: Creates a new <a href="../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> which has given metrics.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.add_metrics" />
<meta itemprop="path" content="Stable" />
</div>

# tf.estimator.add_metrics

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/extenders.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a new <a href="../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> which has given metrics.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.add_metrics`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.add_metrics(
    estimator, metric_fn
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```python
  def my_auc(labels, predictions):
    auc_metric = tf.keras.metrics.AUC(name="my_auc")
    auc_metric.update_state(y_true=labels, y_pred=predictions['logistic'])
    return {'auc': auc_metric}

  estimator = tf.estimator.DNNClassifier(...)
  estimator = tf.estimator.add_metrics(estimator, my_auc)
  estimator.train(...)
  estimator.evaluate(...)
```
Example usage of custom metric which uses features:

```python
  def my_auc(labels, predictions, features):
    auc_metric = tf.keras.metrics.AUC(name="my_auc")
    auc_metric.update_state(y_true=labels, y_pred=predictions['logistic'],
                            sample_weight=features['weight'])
    return {'auc': auc_metric}

  estimator = tf.estimator.DNNClassifier(...)
  estimator = tf.estimator.add_metrics(estimator, my_auc)
  estimator.train(...)
  estimator.evaluate(...)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`estimator`
</td>
<td>
A <a href="../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> object.
</td>
</tr><tr>
<td>
`metric_fn`
</td>
<td>
A function which should obey the following signature:
- Args: can only have following four arguments in any order:
* predictions: Predictions `Tensor` or dict of `Tensor` created by given
`estimator`.
* features: Input `dict` of `Tensor` objects created by `input_fn` which
is given to `estimator.evaluate` as an argument.
* labels:  Labels `Tensor` or dict of `Tensor` created by `input_fn`
which is given to `estimator.evaluate` as an argument.
* config: config attribute of the `estimator`.
- Returns: Dict of metric results keyed by name. Final metrics are a
union of this and `estimator's` existing metrics. If there is a name
conflict between this and `estimator`s existing metrics, this will
override the existing one. The values of the dict are the results of
calling a metric function, namely a `(metric_tensor, update_op)` tuple.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A new <a href="../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> which has a union of original metrics with
given ones.
</td>
</tr>

</table>

