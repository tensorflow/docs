

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.regression_head

``` python
tf.contrib.learn.regression_head(
    label_name=None,
    weight_column_name=None,
    label_dimension=1,
    enable_centered_bias=False,
    head_name=None,
    link_fn=None
)
```



Defined in [`tensorflow/contrib/learn/python/learn/estimators/head.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/learn/python/learn/estimators/head.py).

Creates a `Head` for linear regression. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.contrib.estimator.*_head.

#### Args:

* <b>`label_name`</b>: String, name of the key in label dict. Can be null if label
      is a tensor (single headed models).
* <b>`weight_column_name`</b>: A string defining feature column name representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`label_dimension`</b>: Number of regression labels per example. This is the size
    of the last dimension of the labels `Tensor` (typically, this has shape
    `[batch_size, label_dimension]`).
* <b>`enable_centered_bias`</b>: A bool. If True, estimator will learn a centered
    bias variable for each class. Rest of the model structure learns the
    residual after centered bias.
* <b>`head_name`</b>: name of the head. If provided, predictions, summary and metrics
    keys will be suffixed by `"/" + head_name` and the default variable scope
    will be `head_name`.
* <b>`link_fn`</b>: link function to convert logits to predictions. If provided,
    this link function will be used instead of identity.


#### Returns:

An instance of `Head` for linear regression.