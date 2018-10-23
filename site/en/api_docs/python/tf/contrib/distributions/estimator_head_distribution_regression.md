

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.distributions.estimator_head_distribution_regression

``` python
estimator_head_distribution_regression(
    make_distribution_fn,
    label_dimension=1,
    logits_dimension=None,
    label_name=None,
    weight_column_name=None,
    enable_centered_bias=False,
    head_name=None
)
```



Defined in [`tensorflow/contrib/distributions/python/ops/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/distributions/python/ops/estimator.py).

Creates a `Head` for regression under a generic distribution.

#### Args:

* <b>`make_distribution_fn`</b>: Python `callable` which returns a `tf.Distribution`
    instance created using only logits.
* <b>`label_dimension`</b>: Number of regression labels per example. This is the size
    of the last dimension of the labels `Tensor` (typically, this has shape
    `[batch_size, label_dimension]`).
* <b>`logits_dimension`</b>: Number of logits per example. This is the size of the last
    dimension of the logits `Tensor` (typically, this has shape
    `[batch_size, logits_dimension]`).
    Default value: `label_dimension`.
* <b>`label_name`</b>: Python `str`, name of the key in label `dict`. Can be `None` if
    label is a `Tensor` (single headed models).
* <b>`weight_column_name`</b>: Python `str` defining feature column name representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`enable_centered_bias`</b>: Python `bool`. If `True`, estimator will learn a
    centered bias variable for each class. Rest of the model structure learns
    the residual after centered bias.
* <b>`head_name`</b>: Python `str`, name of the head. Predictions, summary and metrics
    keys are suffixed by `"/" + head_name` and the default variable scope is
    `head_name`.


#### Returns:

An instance of `Head` for generic regression.