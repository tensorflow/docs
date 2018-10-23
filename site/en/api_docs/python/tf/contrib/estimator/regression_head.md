

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.regression_head

``` python
tf.contrib.estimator.regression_head(
    weight_column=None,
    label_dimension=1,
    loss_reduction=losses.Reduction.SUM,
    loss_fn=None,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for regression using the `mean_squared_error` loss.

The loss is the weighted sum over all input dimensions. Namely, if the input
labels have shape `[batch_size, label_dimension]`, the loss is the weighted
sum over both `batch_size` and `label_dimension`.

The head expects `logits` with shape `[D0, D1, ... DN, label_dimension]`.
In many applications, the shape is `[batch_size, label_dimension]`.

The `labels` shape must match `logits`, namely
`[D0, D1, ... DN, label_dimension]`. If `label_dimension=1`, shape
`[D0, D1, ... DN]` is also supported.

If `weight_column` is specified, weights must be of shape
`[D0, D1, ... DN]`, `[D0, D1, ... DN, 1]` or
`[D0, D1, ... DN, label_dimension]`.

Also supports custom `loss_fn`. `loss_fn` takes `(labels, logits)` or
`(labels, logits, features)` as arguments and returns unreduced loss with
shape `[D0, D1, ... DN, label_dimension]`.

#### Args:

* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    `tf.feature_column.numeric_column` defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`label_dimension`</b>: Number of regression labels per example. This is the size
    of the last dimension of the labels `Tensor` (typically, this has shape
    `[batch_size, label_dimension]`).
* <b>`loss_reduction`</b>: One of `tf.losses.Reduction` except `NONE`. Describes how to
    reduce training loss over batch. Defaults to `SUM`.
* <b>`loss_fn`</b>: Optional loss function.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`. Also used as `name_scope` when creating ops.


#### Returns:

An instance of `_Head` for linear regression.


#### Raises:

* <b>`ValueError`</b>: If `label_dimension` or `loss_reduction` is invalid.