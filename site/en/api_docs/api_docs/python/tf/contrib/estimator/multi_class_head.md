

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



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for multi class classification.

Uses `sparse_softmax_cross_entropy` loss.

This head expects to be fed integer labels specifying the class index.

#### Args:

* <b>`n_classes`</b>: Number of classes, must be greater than 2 (for 2 classes, use
    `binary_classification_head`).
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    `tf.feature_column.numeric_column` defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`label_vocabulary`</b>: A list of strings represents possible label values. If it
    is not given, that means labels are already encoded as integer within
    [0, n_classes). If given, labels must be string type and have any value in
    `label_vocabulary`. Also there will be errors if vocabulary is not
    provided and labels are string.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`.


#### Returns:

An instance of `_Head` for multi class classification.


#### Raises:

* <b>`ValueError`</b>: if `n_classes`, `metric_class_ids` or `label_keys` is invalid.