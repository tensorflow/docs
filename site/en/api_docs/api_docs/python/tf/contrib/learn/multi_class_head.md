

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.multi_class_head

``` python
tf.contrib.learn.multi_class_head(
    n_classes,
    label_name=None,
    weight_column_name=None,
    enable_centered_bias=False,
    head_name=None,
    thresholds=None,
    metric_class_ids=None,
    loss_fn=None,
    label_keys=None
)
```



Defined in [`tensorflow/contrib/learn/python/learn/estimators/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/learn/python/learn/estimators/head.py).

Creates a `Head` for multi class single label classification. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.contrib.estimator.*_head.

The Head uses softmax cross entropy loss.

This head expects to be fed integer labels specifying the class index. But
if `label_keys` is specified, then labels must be strings from this
vocabulary, and the predicted classes will be strings from the same
vocabulary.

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
    metrics. Must all be in the range `[0, n_classes)`. Invalid if
    `n_classes` is 2.
* <b>`loss_fn`</b>: Optional function that takes (`labels`, `logits`, `weights`) as
    parameter and returns a weighted scalar loss. `weights` should be
    optional. See <a href="../../../tf/losses"><code>tf.losses</code></a>
* <b>`label_keys`</b>: Optional list of strings with size `[n_classes]` defining the
    label vocabulary. Only supported for `n_classes` > 2.


#### Returns:

An instance of `Head` for multi class classification.


#### Raises:

* <b>`ValueError`</b>: if `n_classes` is < 2.
* <b>`ValueError`</b>: If `metric_class_ids` is provided when `n_classes` is 2.
* <b>`ValueError`</b>: If `len(label_keys) != n_classes`.