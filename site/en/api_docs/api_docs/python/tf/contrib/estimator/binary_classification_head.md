

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.binary_classification_head

``` python
binary_classification_head(
    weight_column=None,
    thresholds=None,
    label_vocabulary=None,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for single label binary classification.

This head uses `sigmoid_cross_entropy_with_logits` loss.

This head expects to be fed float labels of shape `(batch_size, 1)`.

#### Args:

* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    `tf.feature_column.numeric_column` defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`thresholds`</b>: Iterable of floats in the range `(0, 1)`. For binary
    classification metrics such as precision and recall, an eval metric is
    generated for each threshold value. This threshold is applied to the
    logistic values to determine the binary classification (i.e., above the
    threshold is `true`, below is `false`.
* <b>`label_vocabulary`</b>: A list of strings represents possible label values. If it
    is not given, that means labels are already encoded within [0, 1]. If
    given, labels must be string type and have any value in
    `label_vocabulary`. Also there will be errors if vocabulary is not
    provided and labels are string.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`.


#### Returns:

An instance of `_Head` for binary classification.


#### Raises:

* <b>`ValueError`</b>: if `thresholds` contains a value outside of `(0, 1)`.