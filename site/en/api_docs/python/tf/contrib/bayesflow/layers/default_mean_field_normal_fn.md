

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.layers.default_mean_field_normal_fn

``` python
tf.contrib.bayesflow.layers.default_mean_field_normal_fn(
    is_singular=False,
    loc_initializer=None,
    untransformed_scale_initializer=None,
    loc_regularizer=None,
    untransformed_scale_regularizer=None,
    loc_constraint=None,
    untransformed_scale_constraint=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/layers_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/bayesflow/python/ops/layers_util.py).

Creates a function to build Normal distributions with trainable params.

This function produces a closure which produces `tf.distributions.Normal`
parameterized by a loc` and `scale` each created using `tf.get_variable`. The
produced closure accepts the following arguments:

  name: Python `str` name prepended to any created (or existing)
    `tf.Variable`s.
  shape: Python `list`-like representing the parameter's event shape.
  dtype: Type of parameter's event.
  trainable: Python `bool` indicating all created `tf.Variable`s should be
    added to the graph collection `GraphKeys.TRAINABLE_VARIABLES`.
  add_variable_fn: `tf.get_variable`-like `callable` used to create (or
    access existing) `tf.Variable`s.

#### Args:

* <b>`is_singular`</b>: Python `bool` if `True`, forces the special case limit of
    `scale->0`, i.e., a `Deterministic` distribution.
* <b>`loc_initializer`</b>: Initializer function for the `loc` parameters.
    If `None` (default), values are initialized using the default
    initializer used by `tf.get_variable`.
* <b>`untransformed_scale_initializer`</b>: Initializer function for the `scale`
    parameters. If `None` (default), values are initialized using the default
    initializer used by `tf.get_variable`.
* <b>`loc_regularizer`</b>: Regularizer function for the `loc` parameters.
* <b>`untransformed_scale_regularizer`</b>: Regularizer function for the `scale`
    parameters.
* <b>`loc_constraint`</b>: An optional projection function to be applied to the
    loc after being updated by an `Optimizer`. The function must take as input
    the unprojected variable and must return the projected variable (which
    must have the same shape). Constraints are not safe to use when doing
    asynchronous distributed training.
* <b>`untransformed_scale_constraint`</b>: An optional projection function to be
    applied to the `scale` parameters after being updated by an `Optimizer`
    (e.g. used to implement norm constraints or value constraints). The
    function must take as input the unprojected variable and must return the
    projected variable (which must have the same shape). Constraints are not
    safe to use when doing asynchronous distributed training.


#### Returns:

* <b>`make_normal_fn`</b>: Python `callable` which creates a `tf.distributions.Normal`
    using from args: `dtype, shape, name, trainable, add_variable_fn`.