

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.poisson_regression_head

``` python
tf.contrib.estimator.poisson_regression_head(
    weight_column=None,
    label_dimension=1,
    loss_reduction=losses.Reduction.SUM,
    compute_full_loss=True,
    name=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/estimator/python/estimator/head.py).

Creates a `_Head` for poisson regression using `tf.nn.log_poisson_loss`.

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

This is implemented as a generalized linear model, see
https://en.wikipedia.org/wiki/Generalized_linear_model.

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
* <b>`compute_full_loss`</b>: Whether to include the constant `log(z!)` term in
    computing the poisson loss. See `tf.nn.log_poisson_loss` for the full
    documentation.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`. Also used as `name_scope` when creating ops.


#### Returns:

An instance of `_Head` for poisson regression.


#### Raises:

* <b>`ValueError`</b>: If `label_dimension` or `loss_reduction` is invalid.