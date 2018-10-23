

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.multi_label_head

``` python
multi_label_head(
    n_classes,
    weight_column=None,
    thresholds=None,
    label_vocabulary=None,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for multi-label classification.

Multi-label classification handles the case where each example may have zero
or more associated labels, from a discrete set. This is distinct from
`multi_class_head` which has exactly one label per example.

Uses `sigmoid_cross_entropy` loss averaged over classes. Expects labels as a
multi-hot tensor of shape `[batch_size, n_classes]`, or as an integer
`SparseTensor` of class indices.

#### Args:

* <b>`n_classes`</b>: Number of classes, must be greater than 1 (for 1 class, use
    `binary_classification_head`).
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    `tf.feature_column.numeric_column` defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`thresholds`</b>: Iterable of floats in the range `(0, 1)`. Accuracy, precision
    and recall metrics are evaluated for each threshold value. The threshold
    is applied to the predicted probabilities, i.e. above the threshold is
    `true`, below is `false`.
* <b>`label_vocabulary`</b>: A list of strings represents possible label values. If it
    is not given, that means labels are already encoded as integer within
    [0, n_classes) or multi-hot Tensor. If given, labels must be SparseTensor
    string type and have any value in `label_vocabulary`. Also there will be
    errors if vocabulary is not provided and labels are string.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`.


#### Returns:

An instance of `_Head` for multi-label classification.


#### Raises:

* <b>`ValueError`</b>: if `n_classes` or `thresholds` is invalid.