

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.multi_class_head

``` python
multi_class_head(
    n_classes,
    weight_column=None,
    label_vocabulary=None,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for multi class classification.

Uses `sparse_softmax_cross_entropy` loss.

The head expects `logits` with shape `[D0, D1, ... DN, n_classes]`.
In many applications, the shape is `[batch_size, n_classes]`.

`labels` must be a dense `Tensor` with shape matching `logits`, namely
`[D0, D1, ... DN, 1]`. If `label_vocabulary` given, `labels` must be a string
`Tensor` with values from the vocabulary. If `label_vocabulary` is not given,
`labels` must be an integer `Tensor` with values specifying the class index.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]`, or `[D0, D1, ... DN, 1]`.

The loss is the weighted sum over the input dimensions. Namely, if the input
labels have shape `[batch_size, 1]`, the loss is the weighted sum over
`batch_size`.

#### Args:

* <b>`n_classes`</b>: Number of classes, must be greater than 2 (for 2 classes, use
    `binary_classification_head`).
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    `tf.feature_column.numeric_column` defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`label_vocabulary`</b>: A list or tuple of strings representing possible label
    values. If it is not given, that means labels are already encoded as an
    integer within [0, n_classes). If given, labels must be of string type and
    have any value in `label_vocabulary`. Note that errors will be raised if
    `label_vocabulary` is not provided but labels are strings.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`. Also used as `name_scope` when creating ops.


#### Returns:

An instance of `_Head` for multi class classification.


#### Raises:

* <b>`ValueError`</b>: if `n_classes`, `metric_class_ids` or `label_keys` is invalid.