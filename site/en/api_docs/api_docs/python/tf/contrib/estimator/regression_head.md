

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.regression_head

``` python
regression_head(
    weight_column=None,
    label_dimension=1,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for regression using the mean squared loss.

Uses `mean_squared_error` loss.

#### Args:

* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    `tf.feature_column.numeric_column` defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`label_dimension`</b>: Number of regression labels per example. This is the size
    of the last dimension of the labels `Tensor` (typically, this has shape
    `[batch_size, label_dimension]`).
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`.


#### Returns:

An instance of `_Head` for linear regression.