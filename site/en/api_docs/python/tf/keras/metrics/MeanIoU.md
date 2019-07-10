page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.metrics.MeanIoU

## Class `MeanIoU`

Computes the mean Intersection-Over-Union metric.

Inherits From: [`Metric`](../../../tf/keras/metrics/Metric)

### Aliases:

* Class `tf.compat.v1.keras.metrics.MeanIoU`
* Class `tf.compat.v2.keras.metrics.MeanIoU`
* Class `tf.compat.v2.metrics.MeanIoU`
* Class `tf.keras.metrics.MeanIoU`



Defined in [`python/keras/metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/metrics.py).

<!-- Placeholder for "Used in" -->

Mean Intersection-Over-Union is a common evaluation metric for semantic image
segmentation, which first computes the IOU for each semantic class and then
computes the average over classes. IOU is defined as follows:
  IOU = true_positive / (true_positive + false_positive + false_negative).
The predictions are accumulated in a confusion matrix, weighted by
`sample_weight` and the metric is then calculated from it.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

#### Usage:



```python
m = tf.keras.metrics.MeanIoU(num_classes=2)
m.update_state([0, 0, 1, 1], [0, 1, 0, 1])

  # cm = [[1, 1],
          [1, 1]]
  # sum_row = [2, 2], sum_col = [2, 2], true_positives = [1, 1]
  # iou = true_positives / (sum_row + sum_col - true_positives))
  # result = (1 / (2 + 2 - 1) + 1 / (2 + 2 - 1)) / 2 = 0.33
print('Final result: ', m.result().numpy())  # Final result: 0.33
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
  'sgd',
  loss='mse',
  metrics=[tf.keras.metrics.MeanIoU(num_classes=2)])
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_classes,
    name=None,
    dtype=None
)
```

Creates a `MeanIoU` instance.


#### Args:


* <b>`num_classes`</b>: The possible number of labels the prediction task can have.
  This value must be provided, since a confusion matrix of dimension =
  [num_classes, num_classes] will be allocated.
* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states()
```




<h3 id="result"><code>result</code></h3>

``` python
result()
```

Compute the mean intersection-over-union via the confusion matrix.


<h3 id="update_state"><code>update_state</code></h3>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates the confusion matrix statistics.


#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be a
  `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
  be broadcastable to `y_true`.


#### Returns:

Update op.




