page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.multi_label_head

Creates a Head for multi label classification. (deprecated)

``` python
tf.contrib.learn.multi_label_head(
    n_classes,
    label_name=None,
    weight_column_name=None,
    enable_centered_bias=False,
    head_name=None,
    thresholds=None,
    metric_class_ids=None,
    loss_fn=None
)
```



Defined in [`contrib/learn/python/learn/estimators/head.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/learn/python/learn/estimators/head.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.contrib.estimator.*_head.

Multi-label classification handles the case where each example may have zero
or more associated labels, from a discrete set.  This is distinct from
`multi_class_head` which has exactly one label from a discrete set.

This head by default uses sigmoid cross entropy loss, which expects as input
a multi-hot tensor of shape `(batch_size, num_classes)`.

#### Args:


* <b>`n_classes`</b>: Integer, number of classes, must be >= 2
* <b>`label_name`</b>: String, name of the key in label dict. Can be null if label
    is a tensor (single headed models).
* <b>`weight_column_name`</b>: A string defining feature column name representing
  weights. It is used to down weight or boost examples during training. It
  will be multiplied by the loss of the example.
* <b>`enable_centered_bias`</b>: A bool. If True, estimator will learn a centered
  bias variable for each class. Rest of the model structure learns the
  residual after centered bias.
* <b>`head_name`</b>: name of the head. If provided, predictions, summary and metrics
  keys will be suffixed by `"/" + head_name` and the default variable scope
  will be `head_name`.
* <b>`thresholds`</b>: thresholds for eval metrics, defaults to [.5]
* <b>`metric_class_ids`</b>: List of class IDs for which we should report per-class
  metrics. Must all be in the range `[0, n_classes)`.
* <b>`loss_fn`</b>: Optional function that takes (`labels`, `logits`, `weights`) as
  parameter and returns a weighted scalar loss. `weights` should be
  optional. See <a href="../../../tf/losses"><code>tf.losses</code></a>


#### Returns:

An instance of `Head` for multi label classification.



#### Raises:


* <b>`ValueError`</b>: If n_classes is < 2
* <b>`ValueError`</b>: If loss_fn does not have expected signature.